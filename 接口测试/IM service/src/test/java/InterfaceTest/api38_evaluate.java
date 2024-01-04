package InterfaceTest;

import io.restassured.http.ContentType;
import io.restassured.response.Response;
import org.junit.jupiter.api.Test;

import java.security.MessageDigest;

import static io.restassured.RestAssured.given;
import static org.hamcrest.Matchers.*;

public class api38_evaluate {
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
    public void addNewEvaluationTest(){
        String sessionId = getLoginSession("ecnu_admin","pl,okm123");
        String data = "{\n" +
                " \"conversationId\":\"2c9349977d3970d4017dcdc14ee800d5\",\n" +
                " \"objectType\":\"CONVERSATION\"\n" +
                "}\n";
        given().
                cookie("JSESSIONID",sessionId).
                body(data).contentType(ContentType.JSON).
        when().
                put(url + "/evaluate").
        then().
                statusCode(200).
                body("code",equalTo(0)).
                body("message",equalTo("OK")).
                body("result",notNullValue()).
                body("result.creator",equalTo("2c9349977d395626017d39564ca20029")).
                body("result.objectType",equalTo("CONVERSATION"));
        logout(sessionId);
    }

    @Test
    public void addExistedEvaluationTest(){
        String sessionId = getLoginSession("ecnu_admin","pl,okm123");
        String data = "{\n" +
                " \"conversationId\":\"2c9349977d3970d4017db8637f150086\",\n" +
                " \"objectType\":\"CONVERSATION\"\n" +
                "}\n";
        given().
                cookie("JSESSIONID",sessionId).
                body(data).contentType(ContentType.JSON).
        when().
                put(url + "/evaluate").
        then().
                statusCode(200).
                body("code",equalTo(-1)).
                body("message",equalTo("评价已存在")).
                body("result",nullValue());
        logout(sessionId);
    }

    @Test
    public void wrongConversationIdTest(){
        String sessionId = getLoginSession("ecnu_admin","pl,okm123");
        String data = "{\n" +
                " \"conversationId\":\"9400862c93397717d70db81506d7f493\",\n" +
                " \"objectType\":\"CONVERSATION\"\n" +
                "}\n";
        given().
                cookie("JSESSIONID",sessionId).
                body(data).contentType(ContentType.JSON).
        when().
                put(url + "/evaluate").
        then().
                statusCode(500).
                body("error",equalTo("Internal Server Error")).
                body("message",equalTo("")).
                body("path",equalTo("/evaluate"));
        logout(sessionId);
    }

    @Test
    public void wrongObjectTypeTest(){
        String sessionId = getLoginSession("ecnu_admin","pl,okm123");
        String data = "{\n" +
                " \"conversationId\":\"9400862c93397717d70db81506d7f493\",\n" +
                " \"objectType\":\"VERSATION\"\n" +
                "}\n";
        given().
                cookie("JSESSIONID",sessionId).
                body(data).contentType(ContentType.JSON).
        when().
                put(url + "/evaluate").
        then().
                statusCode(500).
                body("error",equalTo("Internal Server Error")).
                body("message",equalTo("")).
                body("path",equalTo("/evaluate"));
        logout(sessionId);
    }

    @Test
    public void allWrongTest(){
        String sessionId = getLoginSession("ecnu_admin","pl,okm123");
        String data = "{\n" +
                " \"conversationId\":\"d706933797c0f49398624817db1005d7\",\n" +
                " \"objectType\":\"SATION\"\n" +
                "}\n";
        given().
                cookie("JSESSIONID",sessionId).
                body(data).contentType(ContentType.JSON).
        when().
                put(url + "/evaluate").
        then().
                statusCode(500).
                body("error",equalTo("Internal Server Error")).
                body("message",equalTo("")).
                body("path",equalTo("/evaluate"));
        logout(sessionId);
    }
}
