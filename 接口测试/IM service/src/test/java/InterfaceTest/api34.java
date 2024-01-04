package InterfaceTest;

import io.restassured.http.ContentType;
import io.restassured.response.Response;
import org.junit.jupiter.api.Test;

import java.security.MessageDigest;

import static io.restassured.RestAssured.given;
import static org.hamcrest.Matchers.equalTo;

public class api34 {
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
    public void correctSessionExportTest(){
        String sessionId = getLoginSession("ecnu_admin","pl,okm123");
        given().
                cookie("JSESSIONID",sessionId).
        when().
                post(url + "/conversation/export/2c9349977d3970d4017db862c4df0084").
        then().
                statusCode(200);
        logout(sessionId);
    }

    @Test
    public void correctSessionExportTest2(){
        String sessionId = getLoginSession("ecnu_admin","pl,okm123");
        given().
                cookie("JSESSIONID",sessionId).
        when().
                post(url + "/conversation/export/2c9349977d3970d4017db8637f150086").
        then().
                statusCode(200);
        logout(sessionId);
    }

    @Test
    public void wrongSessionExportTest(){
        String sessionId = getLoginSession("ecnu_admin","pl,okm123");
        given().
                cookie("JSESSIONID",sessionId).
        when().
                post(url + "/conversation/export/2c9349jhbv3970d4017db86185650086").
        then().
                statusCode(200);
        logout(sessionId);
    }

    @Test
    public void wrongSessionExportTest2(){
        String sessionId = getLoginSession("ecnu_admin","pl,okm123");
        given().
                cookie("JSESSIONID",sessionId).
        when().
                post(url + "/conversation/export/2c93dj5v97db86jhd185fh5c36bv3970").
        then().
                statusCode(200);
        logout(sessionId);
    }
}
