package InterfaceTest;

import io.restassured.http.ContentType;
import io.restassured.response.Response;
import org.junit.jupiter.api.Test;

import java.security.MessageDigest;

import static io.restassured.RestAssured.given;
import static org.hamcrest.Matchers.*;

public class api29 {
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
    public void currentSessionTest(){
        String sessionId = getLoginSession("ecnu_admin","pl,okm123");
        given().
                cookie("JSESSIONID",sessionId).
        when().
                get(url + "/conversation/current").
        then().
                statusCode(200).
                body("code",equalTo(0)).
                body("message",equalTo("OK")).
                body("count",greaterThan(1)).
                body("next",nullValue());
        logout(sessionId);
    }

    @Test
    public void currentSessionResultTest(){
        String sessionId = getLoginSession("ecnu_admin","pl,okm123");
        given().
                cookie("JSESSIONID",sessionId).
        when().
                get(url + "/conversation/current").
        then().
                body("result.id",hasItems("2c9349977d3970d4017ddccb80a00161")).
                body("result.status",hasItems("FINISHED")).
                body("result.duration",hasItems(836542)).
                body("result.conversationType",hasItems("COUNSELING_SESSION"));
        logout(sessionId);
    }

    @Test
    public void currentSessionResultUserTest(){
        String sessionId = getLoginSession("ecnu_admin","pl,okm123");
        given().
                cookie("JSESSIONID",sessionId).
        when().
                get(url + "/conversation/current").
        then().
                body("result.user.id",hasItems("2c9349977d395626017d39564ca20029")).
                body("result.user.institutionCode",hasItems("ecnu")).
                body("result.user.state",hasItems(nullValue())).
                body("result.user.activated",hasItems(false)).
                body("result.user.maxConsults",hasItems(5));
        logout(sessionId);
    }

    @Test
    public void currentSessionResultCounselorTest(){
        String sessionId = getLoginSession("ecnu_admin","pl,okm123");
        given().
                cookie("JSESSIONID",sessionId).
        when().
                get(url + "/conversation/current").
        then().
                body("result.counselor.id",hasItems("2c9349977d3970d4017db40cc0a0006e")).
                body("result.counselor.username",hasItems("yoyi")).
                body("result.counselor.gender",hasItems("女")).
                body("result.counselor.idNumber",hasItems("230103200107031346")).
                body("result.counselor.activateTime",hasItems(nullValue()));
        logout(sessionId);
    }
}
