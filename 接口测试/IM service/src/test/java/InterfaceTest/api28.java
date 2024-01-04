package InterfaceTest;

import io.restassured.http.ContentType;
import io.restassured.response.Response;
import org.junit.jupiter.api.Test;

import java.security.MessageDigest;

import static io.restassured.RestAssured.given;
import static org.hamcrest.Matchers.*;
import static org.hamcrest.Matchers.hasItems;

public class api28 {
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
    public void consultListTest(){
        String sessionId = getLoginSession("ecnu_admin","pl,okm123");
        given().
                cookie("JSESSIONID",sessionId).
        when().
                get(url + "/conversation/consultlist").
        then().
                statusCode(200).
                body("code",equalTo(0)).
                body("message",equalTo("OK")).
                body("result.status",hasItems("FINISHED")).
                body("result.findAll{it.status=='FINISHED'}.id",hasItems("2c9349977d3970d4017db862c4df0084")).
                body("result.conversationType.collect{it.length()}.sum()",greaterThan(10)).
                body("result.findAll{it.user.type=='VISITOR'}.user.username",hasItems("ozF5r5ZAbLWALUYe4GRmBrfjYX0w"));
        logout(sessionId);
    }

    @Test
    public void consultListTest2(){
        String sessionId = getLoginSession("ecnu_admin","pl,okm123");
        given().
                cookie("JSESSIONID",sessionId).
        when().
                get(url + "/conversation/consultlist").
        then().
                body("result.evaluate.objectType",hasItems("CONVERSATION")).
                body("result.findAll{it.status=='FINISHED'}.id",hasItems("2c9349977d3970d4017dcdc971bd00e4")).
                body("result.user.institutionCode.collect{it.length()}.sum()",greaterThan(40)).
                body("result.findAll{it.user.name=='我'}.counselor.username",hasItems("zixunshi1"));
        logout(sessionId);
    }

    @Test
    public void consultListTest3(){
        String sessionId = getLoginSession("ecnu_admin","pl,okm123");
        given().
                cookie("JSESSIONID",sessionId).
        when().
                get(url + "/conversation/consultlist").
        then().
                body("result.duration",hasItems(124248)).
                body("result.evaluate.content",hasItems("好评")).
                body("result.counselor.maxConsults",hasItems(5)).
                body("result.findAll{it.counselor.institutionCode=='ecnu'}.user.state",hasItems("NORMAL"));
        logout(sessionId);
    }

    @Test
    public void consultListWithVisitorNameTest(){
        String sessionId = getLoginSession("ecnu_admin","pl,okm123");
        String request = "{" +
                " \"visitorName\": \"我\"\n" +
                "}";
        given().
                cookie("JSESSIONID",sessionId).
                body(request).contentType(ContentType.JSON).
        when().
                get(url + "/conversation/consultlist").
        then().
                statusCode(200).
                body("code",equalTo(0)).
                body("message",equalTo("OK")).
                body("result.findAll{it.status=='FINISHED'}.id",hasItems("2c9349977d3970d4017db862c4df0084")).
                body("result.evaluate.content",hasItems("好评")).
                body("result.findAll{it.user.type=='VISITOR'}.user.username",hasItems("ozF5r5ZAbLWALUYe4GRmBrfjYX0w")).
                body("result.status",hasItems("FINISHED"));
        logout(sessionId);
    }

    @Test
    public void consultListWithCounselorNameTest(){
        String sessionId = getLoginSession("ecnu_admin","pl,okm123");
        String request = "{" +
                " \"counselorName\": \"大数据\"\n" +
                "}";
        given().
                cookie("JSESSIONID",sessionId).
                body(request).contentType(ContentType.JSON).
        when().
                get(url + "/conversation/consultlist").
        then().
                statusCode(200).
                body("code",equalTo(0)).
                body("message",equalTo("OK")).
                body("result.conversationType.collect{it.length()}.sum()",greaterThan(10)).
                body("result.findAll{it.counselor.institutionCode=='ecnu'}.user.state",hasItems("NORMAL")).
                body("result.counselor.maxConsults",hasItems(5)).
                body("result.evaluate.objectType",hasItems("CONVERSATION"));
        logout(sessionId);
    }

    @Test
    public void consultListWithStartTimeTest(){
        String sessionId = getLoginSession("ecnu_admin","pl,okm123");
        String request = "{" +
                " \"startTime\": 10000000\n" +
                "}";
        given().
                cookie("JSESSIONID",sessionId).
                body(request).contentType(ContentType.JSON).
        when().
                get(url + "/conversation/consultlist").
        then().
                statusCode(200).
                body("code",equalTo(0)).
                body("message",equalTo("OK")).
                body("result.findAll{it.status=='FINISHED'}.id",hasItems("2c9349977d3970d4017db862c4df0084")).
                body("result.evaluate.content",hasItems("好评")).
                body("result.user.institutionCode.collect{it.length()}.sum()",greaterThan(40)).
                body("result.findAll{it.counselor.institutionCode=='ecnu'}.user.state",hasItems("NORMAL"));
        logout(sessionId);
    }

    @Test
    public void consultListWithEndTimeTest(){
        String sessionId = getLoginSession("ecnu_admin","pl,okm123");
        String request = "{" +
                " \"endTime\": 1234567890\n" +
                "}";
        given().
                cookie("JSESSIONID",sessionId).
                body(request).contentType(ContentType.JSON).
        when().
                get(url + "/conversation/consultlist").
        then().
                statusCode(200).
                body("code",equalTo(0)).
                body("message",equalTo("OK"));
        logout(sessionId);
    }

    @Test
    public void consultListWithPropertyTest(){
        String sessionId = getLoginSession("ecnu_admin","pl,okm123");
        String request = "{" +
                " \"property\": \"level\"\n" +
                "}";
        given().
                cookie("JSESSIONID",sessionId).
                body(request).contentType(ContentType.JSON).
        when().
                get(url + "/conversation/consultlist").
        then().
                statusCode(200).
                body("code",equalTo(0)).
                body("message",equalTo("OK")).
                body("result.findAll{it.user.type=='VISITOR'}.user.username",hasItems("ozF5r5ZAbLWALUYe4GRmBrfjYX0w")).
                body("result.evaluate.objectType",hasItems("CONVERSATION")).
                body("result.findAll{it.user.name=='我'}.counselor.username",hasItems("zixunshi1")).
                body("result.counselor.maxConsults",hasItems(5));
        logout(sessionId);
    }

    @Test
    public void consultListWithDirectionTest(){
        String sessionId = getLoginSession("ecnu_admin","pl,okm123");
        String request = "{" +
                " \"direction\": \"desc\"\n" +
                "}";
        given().
                cookie("JSESSIONID",sessionId).
                body(request).contentType(ContentType.JSON).
        when().
                get(url + "/conversation/consultlist").
        then().
                statusCode(200).
                body("code",equalTo(0)).
                body("message",equalTo("OK")).
                body("result.findAll{it.status=='FINISHED'}.id",hasItems("2c9349977d3970d4017db862c4df0084")).
                body("result.conversationType.collect{it.length()}.sum()",greaterThan(10)).
                body("result.duration",hasItems(124248)).
                body("result.evaluate.content",hasItems("好评"));
        logout(sessionId);
    }

    @Test
    public void consultListWithPageTest(){
        String sessionId = getLoginSession("ecnu_admin","pl,okm123");
        String request = "{" +
                " \"page\": 1\n" +
                "}";
        given().
                cookie("JSESSIONID",sessionId).
                body(request).contentType(ContentType.JSON).
        when().
                get(url + "/conversation/consultlist").
        then().
                statusCode(200).
                body("code",equalTo(0)).
                body("message",equalTo("OK"));
        logout(sessionId);
    }

    @Test
    public void consultListWithSizeTest(){
        String sessionId = getLoginSession("ecnu_admin","pl,okm123");
        String request = "{" +
                " \"size\": 4\n" +
                "}";
        given().
                cookie("JSESSIONID",sessionId).
                body(request).contentType(ContentType.JSON).
        when().
                get(url + "/conversation/consultlist").
        then().
                statusCode(200).
                body("code",equalTo(0)).
                body("message",equalTo("OK"));
        logout(sessionId);
    }
}
