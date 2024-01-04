package InterfaceTest;

import io.restassured.http.ContentType;
import io.restassured.response.Response;
import org.junit.jupiter.api.Test;

import java.security.MessageDigest;

import static io.restassured.RestAssured.given;
import static org.hamcrest.Matchers.*;

public class api35 {
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
    public void correctBatchExportTest(){
        String sessionId = getLoginSession("ecnu_admin","pl,okm123");
        String request = "[\"2c9349977d3970d4017da9ccd44c002f\",\"2c9349977d3970d4017db8637f150086\",\"2c9349977d3970d4017db862c4df0084\"]";
        given().
                cookie("JSESSIONID",sessionId).
                body(request).
        when().
                post(url + "/conversation/batchexport").
        then().
                statusCode(200);
        logout(sessionId);
    }

    @Test
    public void wrongBatchExportTest(){
        String sessionId = getLoginSession("ecnu_admin","pl,okm123");
        String request = "[\"2c90d401d44ca9cc7734997dd397002f\",\"2c704017dbdf150349986379d3977086\",\"77d4c4df67020d42c017db8934083999\"]";
        given().
                cookie("JSESSIONID",sessionId).
                body(request).
        when().
                post(url + "/conversation/batchexport").
        then().
                body("message",equalTo("")).
                body("status",equalTo(415)).
                body("error",equalTo("Unsupported Media Type")).
                body("path",equalTo("/conversation/batchexport"));
        logout(sessionId);
    }
}
