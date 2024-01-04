package UserTest;

import io.restassured.http.ContentType;
import io.restassured.response.Response;
import org.junit.Test;

import java.security.MessageDigest;

import static io.restassured.RestAssured.given;
import static org.hamcrest.Matchers.equalTo;
import static org.hamcrest.Matchers.nullValue;

public class AddInfromation {

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
    public void correctAddTest(){
        String sessionId = getLoginSession("ecnu_admin","pl,okm123");

        String request = "{\n" +
                "  \"username\": \"quanxingrun\",\n" +
                "  \"password\": \"173afad5992a3f73a472fc09b05b1fb7\",\n" +
                "  \"role\":\"ROLE_SUPERVISOR\",\n" +
                "  \"idNumber\" : \"222222200212032222\",\n" +
                "  \"phoneNumber\" : \"18343337087\",\n" +
                "  \"name\" : \"一样迁徙\"\n" +
                "}\n";
        given().
                cookie("JSESSIONID",sessionId).
                body(request).contentType(ContentType.JSON).
                when().
                put(url + "/user/ms/supervisor").
                then().
                statusCode(200).
                body("code",equalTo(0)).
                body("message",equalTo("OK"));
        logout(sessionId);
    }

    @Test
    public void AddRepeatedTest(){
        String sessionId = getLoginSession("ecnu_admin","pl,okm123");
        String request = "{\n" +
                "  \"username\": \"quanxingrun\",\n" +
                "  \"password\": \"173afad5992a3f73a472fc09b05b1fb7\",\n" +
                "  \"role\":\"ROLE_SUPERVISOR\",\n" +
                "  \"idNumber\" : \"222222200212032222\",\n" +
                "  \"phoneNumber\" : \"18343337087\",\n" +
                "  \"name\" : \"一样迁徙\"\n" +
                "}\n";
        given().
                cookie("JSESSIONID",sessionId).
                body(request).contentType(ContentType.JSON).
                when().
                put(url + "/user/ms/supervisor").
                then().
                statusCode(200).
                body("code",equalTo(-2)).
                body("message",equalTo("用户名已存在")).
                body("result",nullValue());
        logout(sessionId);
    }

    @Test
    public void nullUsernameTest(){
        String sessionId = getLoginSession("ecnu_admin","pl,okm123");
        String request =  "{\n" +
                "  \"username\": \"\",\n" +
                "  \"password\": \"173afad5992a3f73a472fc09b05b1fb7\",\n" +
                "  \"role\":\"ROLE_SUPERVISOR\",\n" +
                "  \"idNumber\" : \"222222200212032222\",\n" +
                "  \"phoneNumber\" : \"18343337087\",\n" +
                "  \"name\" : \"一样迁徙\"\n" +
                "}\n";
        given().
                cookie("JSESSIONID",sessionId).
                body(request).contentType(ContentType.JSON).
                when().
                put(url + "/user/ms/supervisor").
                then().
                body("code",equalTo(-1)).
                body("message",equalTo("key [username] failed on checker com.cloume.ecnu.psy.hotline.controller.MSUserController$$Lambda$1754/1086034286@546787b6 with value []")).
                body("result",nullValue());
        logout(sessionId);
    }

    @Test
    public void wrongPasswordTest(){
        String sessionId = getLoginSession("ecnu_admin","pl,okm123");
        String request ="{\n" +
                "  \"username\": \"\",\n" +
                "  \"password\": \"173a\",\n" +
                "  \"role\":\"ROLE_SUPERVISOR\",\n" +
                "  \"idNumber\" : \"222222200212032222\",\n" +
                "  \"phoneNumber\" : \"18343337087\",\n" +
                "  \"name\" : \"一样迁徙\"\n" +
                "}\n";
        given().
                cookie("JSESSIONID",sessionId).
                body(request).contentType(ContentType.JSON).
                when().
                post(url + "/user/password").
                then().
                body("code",equalTo(-1)).
                body("message",equalTo("key [password] failed on checker com.cloume.ecnu.psy.hotline.controller.MSUserController$$Lambda$1754/1086034286@546787b6 with value 173a")).
                body("result",nullValue());
        logout(sessionId);
    }

}
