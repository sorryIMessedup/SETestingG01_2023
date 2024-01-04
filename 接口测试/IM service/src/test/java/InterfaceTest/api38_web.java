package InterfaceTest;

import io.restassured.http.ContentType;
import io.restassured.response.Response;
import org.junit.jupiter.api.Test;

import java.security.MessageDigest;

import static io.restassured.RestAssured.given;
import static org.hamcrest.Matchers.*;
import static org.hamcrest.Matchers.hasItems;

public class api38_web {
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
    public void correctConversationTest(){
        String sessionId = getLoginSession("ecnu_admin","pl,okm123");
        given().
                cookie("JSESSIONID",sessionId).
                queryParam("conversationId","2c9349977d3970d4017da9ccd44c002f").
        when().
                get(url + "/message/conversation/web").
        then().
                statusCode(200).
                body("code",equalTo(0)).
                body("count",greaterThan(1)).
                body("result.from",hasItems("ozF5r5ZAbLWALUYe4GRmBrfjYX0w")).
                body("result.find{it.from=='ozF5r5ZAbLWALUYe4GRmBrfjYX0w'}.to",equalTo("zixunshi1")).
                body("result.findAll{it.status=='success'}.ID",hasItems("2c9349977d3970d4017da9cd2d5e0030")).
                body("result.payload.text",notNullValue()).
                body("result.isDeleted",hasItems(false));
        logout(sessionId);
    }

    @Test
    public void correctConversationTest2(){
        String sessionId = getLoginSession("ecnu_admin","pl,okm123");
        given().
                cookie("JSESSIONID",sessionId).
                queryParam("conversationId","2c9349977d3970d4017dcdcf18fc00ec").
        when().
                get(url + "/message/conversation/web").
        then().
                body("message",equalTo("OK")).
                body("count",greaterThan(2)).
                body("result.conversationType",hasItems("TIM.TYPES.CONV_C2C")).
                body("result.find{it.to=='zixunshi1'}.from",equalTo("ozF5r5ZAbLWALUYe4GRmBrfjYX0w")).
                body("result.findAll{it.isDeleted==false}.isModified",hasItems(true)).
                body("result.time",notNullValue()).
                body("result.status",hasItems("success"));
        logout(sessionId);
    }

    @Test
    public void correctConversationTest3(){
        String sessionId = getLoginSession("ecnu_admin","pl,okm123");
        given().
                cookie("JSESSIONID",sessionId).
                queryParam("conversationId","2c9349977d3970d4017dcc972a9300c5").
        when().
                get(url + "/message/conversation/web").
        then().
                body("result.type",hasItems("TIMTextElem")).
                body("count",equalTo(8)).
                body("result.ID",hasItems("2c9349977d3970d4017dcc97618800c6")).
                body("result.find{it.isPeerRead==true}.flow",equalTo("out")).
                body("result.findAll{it.nick==''}.isRevoked",hasItems(false)).
                body("result.payload.uuid",hasItems("1400586680-ozF5r5ZAbLWALUYe4GRmBrfjYX0w-ZeXRiG5uhk1eT2rjIHJ2RzhCLHA5zstN")).
                body("result.payload.imageinfoarray.size()",lessThan(10));
        logout(sessionId);
    }

    @Test
    public void correctConversationTest4(){
        String sessionId = getLoginSession("ecnu_admin","pl,okm123");
        given().
                cookie("JSESSIONID",sessionId).
                queryParam("conversationId","2c9349977d3970d4017dc8c58eb700b2").
        when().
                get(url + "/message/conversation/web").
        then().
                body("result.priority",hasItems("TIM.TYPES.MSG_PRIORITY_NORMAL")).
                body("count",equalTo(5)).
                body("result.cloudCustomData",hasItems("2c9349977d3970d4017dc8c58eb700b2")).
                body("result.find{it.avatar==''}.status",equalTo("success")).
                body("result.findAll{it.isModified==true}.from",hasItems("ozF5r5ZAbLWALUYe4GRmBrfjYX0w")).
                body("result.payload.text",notNullValue()).
                body("result.payload.desc",hasItems("3"));
        logout(sessionId);
    }

    @Test
    public void wrongConversationIdTest(){
        String sessionId = getLoginSession("ecnu_admin","pl,okm123");
        given().
                cookie("JSESSIONID",sessionId).
                queryParam("conversationId","c58eb70900b972392c34977dd17dc408").
        when().
                get(url + "/message/conversation/web").
        then().
                body("code",equalTo(-1)).
                body("message",equalTo("conversation not find: c58eb70900b972392c34977dd17dc408")).
                body("result",nullValue());
        logout(sessionId);
    }

    @Test
    public void wrongConversationIdWithPageAndSizeTest(){
        String sessionId = getLoginSession("ecnu_admin","pl,okm123");
        given().
                cookie("JSESSIONID",sessionId).
                queryParam("conversationId","900b979c3c58eb7sdviklf047dc77dd1").
                queryParam("page",1).
                queryParam("size",5).
        when().
                get(url + "/message/conversation/web").
        then().
                body("code",equalTo(-1)).
                body("message",equalTo("conversation not find: 900b979c3c58eb7sdviklf047dc77dd1")).
                body("result",nullValue());
        logout(sessionId);
    }

    @Test
    public void conversationWithPageTest(){
        String sessionId = getLoginSession("ecnu_admin","pl,okm123");
        given().
                cookie("JSESSIONID",sessionId).
                queryParam("conversationId","2c9349977d3970d4017dc8c58eb700b2").
                queryParam("page",1).
        when().
                get(url + "/message/conversation/web").
        then().
                statusCode(200).
                body("code",equalTo(0)).
                body("message",equalTo("OK")).
                body("result.size()",equalTo(0)).
                body("count",equalTo(5)).
                body("next",nullValue());
        logout(sessionId);
    }

    @Test
    public void conversationWithSizeTest(){
        String sessionId = getLoginSession("ecnu_admin","pl,okm123");
        given().
                cookie("JSESSIONID",sessionId).
                queryParam("conversationId","2c9349977d3970d4017dc8c58eb700b2").
                queryParam("size",5).
        when().
                get(url + "/message/conversation/web").
        then().
                statusCode(200).
                body("code",equalTo(0)).
                body("message",equalTo("OK")).
                body("result.size()",equalTo(5)).
                body("count",equalTo(5)).
                body("next",nullValue());
        logout(sessionId);
    }

    @Test
    public void conversationWithPageAndSizeTest(){
        String sessionId = getLoginSession("ecnu_admin","pl,okm123");
        given().
                cookie("JSESSIONID",sessionId).
                queryParam("conversationId","2c9349977d3970d4017dc8c58eb700b2").
                queryParam("page",1).
                queryParam("size",5).
        when().
                get(url + "/message/conversation/web").
        then().
                statusCode(200).
                body("code",equalTo(0)).
                body("message",equalTo("OK")).
                body("result.size()",equalTo(0)).
                body("count",equalTo(5)).
                body("next",nullValue());
        logout(sessionId);
    }
}
