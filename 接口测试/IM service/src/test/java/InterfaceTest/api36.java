package InterfaceTest;

import io.restassured.http.ContentType;
import io.restassured.response.Response;
import org.junit.jupiter.api.Test;

import java.security.MessageDigest;

import static io.restassured.RestAssured.given;
import static org.hamcrest.Matchers.*;

public class api36 {
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
    public void correctIdDeleteTest(){
        String sessionId = getLoginSession("ecnu_admin","pl,okm123");
        given().
                cookie("JSESSIONID",sessionId).
        when().
                delete(url + "/conversation/2c9349977d3970d4017ddccb80a00161").
        then().
                statusCode(200).
                body("code",equalTo(0)).
                body("message",equalTo("OK"));
        logout(sessionId);
    }

    @Test
    public void wrongIdDeleteTest(){
        String sessionId = getLoginSession("ecnu_admin","pl,okm123");
        given().
                cookie("JSESSIONID",sessionId).
        when().
                delete(url + "/conversation/2c9440707da941d437dccd99c397002f").
        then().
                body("status",equalTo(500)).
                body("error",equalTo("Internal Server Error")).
                body("message",equalTo("")).
                body("path",equalTo("/conversation/2c9440707da941d437dccd99c397002f"));
        logout(sessionId);
    }
}
