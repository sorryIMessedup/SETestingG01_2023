package InterfaceTest;

import io.restassured.http.ContentType;
import io.restassured.response.Response;
import org.junit.Test;

import java.security.MessageDigest;

import static io.restassured.RestAssured.given;
import static org.hamcrest.Matchers.*;

public class api27 {
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
    public void allCorrectTest(){
        String sessionId = getLoginSession("ecnu_admin","pl,okm123");
        given().
                cookie("JSESSIONID",sessionId).
                queryParam("supervise","2c9349977d3970d4017db393b4060056").
                queryParam("conversationId","2c9349977d3970d4017ddccb80a00161").
        when().
                put(url + "/conversation/supervise").
        then().
                statusCode(200).
                body("code",equalTo(0)).
                body("message",equalTo("OK")).
                body("result.id",equalTo("2c9349977d3970d4017ddccb80a00161")).
                body("result.user.id",equalTo("2c9349977d395626017d39564ca20029"));
        logout(sessionId);
    }

    @Test
    public void wrongSuperviseTest(){
        String sessionId = getLoginSession("ecnu_admin","pl,okm123");
        given().
                cookie("JSESSIONID",sessionId).
                queryParam("supervise","2c93499asfv970d401742653b4060056").
                queryParam("conversationId","2c9349977d3970d4017ddccb80a00161").
        when().
                put(url + "/conversation/supervise").
        then().
                body("code",equalTo(-3)).
                body("message",equalTo("supervisor not find")).
                body("result",nullValue());
        logout(sessionId);
    }

    @Test
    public void wrongIdTest(){
        String sessionId = getLoginSession("ecnu_admin","pl,okm123");
        given().
                cookie("JSESSIONID",sessionId).
                queryParam("supervise","2c9349977d3970d4017db393b4060056").
                queryParam("conversationId","2c93499sdvc970d4014126cb80a00161").
        when().
                put(url + "/conversation/supervise").
        then().
                body("code",equalTo(-1)).
                body("message",equalTo("会话未找到：2c93499sdvc970d4014126cb80a00161")).
                body("result",nullValue());
        logout(sessionId);
    }

    @Test
    public void allWrongTest(){
        String sessionId = getLoginSession("ecnu_admin","pl,okm123");
        given().
                cookie("JSESSIONID",sessionId).
                queryParam("supervise","2c93499asfjfkvd401742653462k0056").
                queryParam("conversationId","2csdko977d3970d452g6dccb80a00661").
        when().
                put(url + "/conversation/supervise").
        then().
                body("code",equalTo(-3)).
                body("message",equalTo("supervisor not find")).
                body("result",nullValue());
        logout(sessionId);
    }
}
