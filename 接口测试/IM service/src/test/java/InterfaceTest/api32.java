package InterfaceTest;

import io.restassured.http.ContentType;
import io.restassured.response.Response;
import org.junit.Test;

import java.security.MessageDigest;

import static io.restassured.RestAssured.given;
import static org.hamcrest.Matchers.*;

public class api32 {
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
    public void evaluateRankTest(){
        String sessionId = getLoginSession("ecnu_admin","pl,okm123");
        given().
                cookie("JSESSIONID",sessionId).
        when().
                get(url + "/conversation/ratedranking").
        then().
                statusCode(200).
                body("code",equalTo(0)).
                body("message",equalTo("OK"));
        logout(sessionId);
    }

    @Test
    public void evaluateRankResultTest(){
        String sessionId = getLoginSession("ecnu_admin","pl,okm123");
        given().
                cookie("JSESSIONID",sessionId).
        when().
                get(url + "/conversation/ratedranking").
        then().
                body("result.size()",greaterThan(1)).
                body("result.rate.sum()",greaterThanOrEqualTo(6)).
                body("result.gender",hasItems("女")).
                body("result.name",hasItems("yoyi")).
                body("result.find{it.name=='yoyi'}.rate",lessThan(6)).
                body("result.find{it.rate>4}.name",equalTo("yoyi")).
                body("result.findAll{it.gender=='女'}.rate.sum()",lessThan(20));
        logout(sessionId);
    }
}
