package InterfaceTest;

import io.restassured.http.ContentType;
import io.restassured.response.Response;
import org.junit.jupiter.api.Test;

import java.security.MessageDigest;

import static io.restassured.RestAssured.given;
import static org.hamcrest.Matchers.*;

public class api39 {
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
    public void configTest1(){
        String sessionId = getLoginSession("ecnu_admin","pl,okm123");
        given().
                cookie("JSESSIONID",sessionId).
        when().
                get(url + "/config").
        then().
                statusCode(200).
                body("code",equalTo(0)).
                body("result.mode.activeMode",equalTo("sei-test")).
                body("result.conversationType.size()",equalTo(2)).
                body("result.userRoles.size()",equalTo(2)).
                body("result.counselor.maxConsults",greaterThanOrEqualTo(1)).
                body("result.userType.size()",equalTo(3)).
                body("result.conversationStatus.size()",equalTo(3)).
                body("result.conversationStatus.IN_PROGRESS",equalTo("进行中"));
        logout(sessionId);
    }

    @Test
    public void configTest2(){
        String sessionId = getLoginSession("ecnu_admin","pl,okm123");
        given().
                cookie("JSESSIONID",sessionId).
        when().
                get(url + "/config").
        then().
                body("result.information.name",notNullValue()).
                body("result.information.find{it}.attrs.class",equalTo("richText")).
                body("result.information.find{it}.children.size()",equalTo(33)).
                body("result.information.find{it}.children.name",hasItems("br")).
                body("result.information.find{it}.children.type",hasItems("text")).
                body("result.information.find{it}.children.findAll{it.name=='br'}.size()",equalTo(16)).
                body("result.information.find{it}.children.findAll{it.type=='text'}.size()",equalTo(17)).
                body("result.information.find{it}.children.text",hasItems("1. 每次语音通话时间上限为40分钟，文字沟通时间上线1小时。"));
        logout(sessionId);
    }
}
