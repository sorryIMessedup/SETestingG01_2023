package InterfaceTest;

import io.restassured.http.ContentType;
import io.restassured.response.Response;
import org.junit.Test;

import java.security.MessageDigest;

import static io.restassured.RestAssured.given;
import static org.hamcrest.Matchers.*;

public class api26 {
    public String url = "https://sei-test.021hqit.com/group-4/liwa-api";

    public String doMD5(String str){
        StringBuilder string = new StringBuilder();
        try{
            MessageDigest md = MessageDigest.getInstance("MD5");
            md.update(str.getBytes());
            byte[] hash = md.digest();
            for(int i=0;i<hash.length;i++){
                if((0xff & hash[i]) < 0x10)
                    string.append("0" + Integer.toHexString(0xFF & hash[i]));
                else
                    string.append(Integer.toHexString(0xFF & hash[i]));
            }
        }
        catch (Exception e){
            e.printStackTrace();
        }
        return string.toString();
    }

    public String getLoginSession(String username, String pwd){
        String password = doMD5(pwd);
        String data = "{" +
                " \"username\":\"" + username +"\",\n" +
                " \"password\":\"" + password +
                "\"}";
        Response response =
                given().
                        body(data).contentType(ContentType.JSON).
                when().
                        post(url + "/auth/login").
                then().
                        log().all().extract().response();
        return response.getCookie("JSESSIONID");
    }

    public void logout(String sessionId){
        given().
                cookie("JSESSIONID",sessionId).
        when().
                post(url + "/logout");
    }

    @Test
    public void correctCounselorTest(){
        String sessionId = getLoginSession("ecnu_admin","pl,okm123");
        String request = "{" +
                " \"counselor\": \"2c9349977d3970d4017db40cc0a0006e\"\n" +
                "}";
        given().
                cookie("JSESSIONID",sessionId).
                body(request).contentType(ContentType.JSON).
        when().
                put(url + "/conversation").
        then().
                statusCode(200).
                body("code",equalTo(0)).
                body("message",equalTo("OK"));
        logout(sessionId);
    }

    @Test
    public void anotherCorrectCounselorTest(){
        String sessionId = getLoginSession("ecnu_admin","pl,okm123");
        String request = "{" +
                " \"counselor\": \"2c9349977d3970d4017d9a11ba8d0006\"\n" +
                "}";
        given().
                cookie("JSESSIONID",sessionId).
                body(request).contentType(ContentType.JSON).
        when().
                put(url + "/conversation").
        then().
                statusCode(200).
                body("code",equalTo(-1)).
                body("message",equalTo("您正在咨询 大数据应用的场景, 请先结束当前会话")).
                body("result",nullValue());
        logout(sessionId);
    }

    @Test
    public void correctCounselorResultTest(){
        String sessionId = getLoginSession("ecnu_admin","pl,okm123");
        String request = "{" +
                " \"counselor\": \"2c9349977d3970d4017db40cc0a0006e\"\n" +
                "}";
        given().
                cookie("JSESSIONID",sessionId).
                body(request).contentType(ContentType.JSON).
        when().
                put(url + "/conversation").
        then().
                body("result.status",equalTo("IN_PROGRESS")).
                body("result.conversationType",equalTo("COUNSELING_SESSION")).
                body("result.avatarUrl",nullValue());
        logout(sessionId);
    }

    @Test
    public void correctCounselorUserTest(){
        String sessionId = getLoginSession("ecnu_admin","pl,okm123");
        String request = "{" +
                " \"counselor\": \"2c9349977d3970d4017db40cc0a0006e\"\n" +
                "}";
        given().
                cookie("JSESSIONID",sessionId).
                body(request).contentType(ContentType.JSON).
        when().
                put(url + "/conversation").
        then().
                body("result.user.id",equalTo("2c9349977d395626017d39564ca20029")).
                body("result.user.institutionCode",equalTo("ecnu")).
                body("result.user.username",equalTo("ecnu_admin")).
                body("result.user.department",nullValue()).
                body("result.user.type",equalTo("INSTITUTION")).
                body("result.user.qualificationCode",nullValue()).
                body("result.user.roles",equalTo("ROLE_INSTITUTION_ADMINISTRATOR")).
                body("result.user.enabled",equalTo(true));
        logout(sessionId);
    }

    @Test
    public void correctCounselorCounselorTest(){
        String sessionId = getLoginSession("ecnu_admin","pl,okm123");
        String request = "{" +
                " \"counselor\": \"2c9349977d3970d4017db40cc0a0006e\"\n" +
                "}";
        given().
                cookie("JSESSIONID",sessionId).
                body(request).contentType(ContentType.JSON).
        when().
                put(url + "/conversation").
        then().
                body("result.counselor.id",equalTo("2c9349977d3970d4017db40cc0a0006e")).
                body("result.counselor.institutionCode",equalTo("ecnu")).
                body("result.counselor.name",equalTo("yoyi")).
                body("result.counselor.gender",equalTo("女")).
                body("result.counselor.age",equalTo(20)).
                body("result.counselor.state",equalTo("NORMAL")).
                body("result.counselor.roles",equalTo("ROLE_COUNSELOR")).
                body("result.counselor.emergencyPhone",nullValue()).
                body("result.counselor.accountNonLocked",equalTo(true));
        logout(sessionId);
    }

    @Test
    public void wrongCounselorTest(){
        String sessionId = getLoginSession("ecnu_admin","pl,okm123");
        String request = "{" +
                " \"counselor\": \"2c9349sdfd3970d4fhndb40cc138006e\"\n" +
                "}";
        given().
                cookie("JSESSIONID",sessionId).
                body(request).contentType(ContentType.JSON).
        when().
                put(url + "/conversation").
        then().
                body("code",equalTo(-3)).
                body("message",equalTo("counselor not find")).
                body("result",nullValue());
        logout(sessionId);
    }

    @Test
    public void stopConversationCorrectIdTest(){
        String sessionId = getLoginSession("ecnu_admin","pl,okm123");
        given().
                cookie("JSESSIONID",sessionId).
        when().
                post(url + "/conversation/end/2c9349977d3970d4017ddcb049480142").
        then().
                statusCode(200).
                body("code",equalTo(0)).
                body("message",equalTo("OK")).
                body("result",equalTo("ok"));
        logout(sessionId);
    }

    @Test
    public void stopConversationCorrectIdTest2(){
        String sessionId = getLoginSession("ecnu_admin","pl,okm123");
        given().
                cookie("JSESSIONID",sessionId).
        when().
                post(url + "/conversation/end/2c9349977d3970d4017ddca35c31013c").
        then().
                statusCode(200).
                body("code",equalTo(0)).
                body("message",equalTo("OK")).
                body("result",equalTo("ok"));
        logout(sessionId);
    }

    @Test
    public void stopConversationWrongIdTest(){
        String sessionId = getLoginSession("ecnu_admin","pl,okm123");
        given().
                cookie("JSESSIONID",sessionId).
        when().
                post(url + "/conversation/end/2c93dsf77d316540d4017dffg31013c").
        then().
                body("code",equalTo(-1)).
                body("message",equalTo("会话未找到：2c93dsf77d316540d4017dffg31013c")).
                body("result",nullValue());
        logout(sessionId);
    }
}
