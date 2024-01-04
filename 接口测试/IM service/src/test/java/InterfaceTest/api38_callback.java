package InterfaceTest;

import io.restassured.http.ContentType;
import io.restassured.response.Response;
import org.junit.jupiter.api.Test;

import java.security.MessageDigest;

import static io.restassured.RestAssured.given;
import static org.hamcrest.Matchers.equalTo;
import static org.hamcrest.Matchers.notNullValue;

public class api38_callback {
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
    public void messageCallBackTest(){
        String sessionId = getLoginSession("ecnu_admin","pl,okm123");
        String queryData = "{ \"CallbackCommand\": \"C2C.CallbackAfterSendMsg\",\n" +
                " \"From_Account\": \"2c9349977d3970d4017d8ea6d5650002\",\n" +
                " \"To_Account\": \"2c9349977d3970d4017d9a11ba8d0006\",\n" +
                " \"MsgSeq\": 80496,\n" +
                " \"MsgRandom\": 5419745,\n" +
                " \"MsgTime\": 2123185490,\n" +
                " \"MsgKey\": \"80496_5419745_2123185490\",\n" +
                " \"OnlineOnlyFlag\": 1,\n" +
                " \"SendMsgResult\": 0,\n" +
                " \"ErrorInfo\": \"send msg succeed\",\n" +
                " \"UnreadMsgNum\": 0,\n" +
                " \"MsgBody\": [{\"MsgType\": \"text\",\n" +
                " \"MsgContent\": {\n" +
                " \"Text\": \"我\"}\n}],\n" +
                " \"CloudCustomData\": \"2c9349977d3970d4017da9ccd44c002f\"}";
        given().
                cookie("JSESSIONID",sessionId).
                body(queryData).contentType(ContentType.JSON).
        when().
                post(url + "/message/callback?SdkAppid=1400586680&CallbackCommand=C2C.CallbackAfterSendMsg" +
                        "&contentType=JSON&OptPlatform=RESTAPI").
        then().
                statusCode(200).
                body("code",equalTo(0)).
                body("message",equalTo("OK")).
                body("result",equalTo("ok"));
        logout(sessionId);
    }

    @Test
    public void correctCallBackTest(){
        String sessionId = getLoginSession("ecnu_admin","pl,okm123");
        String queryData = "{ \"CallbackCommand\": \"C2C.CallbackAfterSendMsg\",\n" +
                " \"From_Account\": \"2c9349977d3970d4017d8ea6d5650002\",\n" +
                " \"To_Account\": \"2c9349977d3970d4017d9a11ba8d0006\",\n" +
                " \"MsgSeq\": 80496,\n" +
                " \"MsgRandom\": 5419745,\n" +
                " \"MsgTime\": 2123185490,\n" +
                " \"MsgKey\": \"80496_5419745_2123185490\",\n" +
                " \"OnlineOnlyFlag\": 1,\n" +
                " \"SendMsgResult\": 0,\n" +
                " \"ErrorInfo\": \"send msg succeed\",\n" +
                " \"UnreadMsgNum\": 0,\n" +
                " \"MsgBody\": [{\"MsgType\": \"text\",\n" +
                " \"MsgContent\": {\n" +
                " \"Text\": \"我\"}\n}],\n" +
                " \"CloudCustomData\": \"2c9349977d3970d4017da9ccd44c002f\"}";
        given().
                cookie("JSESSIONID",sessionId).
                body(queryData).contentType(ContentType.JSON).
        when().
                post(url + "/message/callback?SdkAppid=1400586680&CallbackCommand=C2C.CallbackAfterSendMsg" +
                        "&contentType=JSON&OptPlatform=RESTAPI").
        then().
                statusCode(200).
                body("ErrorCode",equalTo(0)).
                body("ActionStatus",equalTo("OK")).
                body("ErrorInfo",equalTo(""));
        logout(sessionId);
    }

    @Test
    public void wrongCallBackTest(){
        String sessionId = getLoginSession("ecnu_admin","pl,okm123");
        String queryData = "{ \"CallbackCommand\": \"C2C.CallbackAfterSendMsg\",\n" +
                " \"From_Account\": \"2c93d8e7d390da6d4756549970170002\",\n" +
                " \"To_Account\": \"2c9349dd8d0bad39709a110179774006\",\n" +
                " \"MsgSeq\": 52096,\n" +
                " \"MsgRandom\": 5498145,\n" +
                " \"MsgTime\": 2563141290,\n" +
                " \"MsgKey\": \"52096_5498145_2563141290\",\n" +
                " \"OnlineOnlyFlag\": 0,\n" +
                " \"SendMsgResult\": 1,\n" +
                " \"ErrorInfo\": \"send msg succeed\",\n" +
                " \"UnreadMsgNum\": 2,\n" +
                " \"MsgBody\": [{\"MsgType\": \"text\",\n" +
                " \"MsgContent\": {\n" +
                " \"Text\": \"wo\"}\n}],\n" +
                " \"CloudCustomData\": \"00017da2c9349949c9707d3fd2cd44c7\"}";
        given().
                cookie("JSESSIONID",sessionId).
                body(queryData).contentType(ContentType.JSON).
        when().
                post(url + "/message/callback?SdkAppid=1400586680&CallbackCommand=C2C.CallbackAfterSendMsg" +
                        "&contentType=JSON&OptPlatform=RESTAPI").
        then().
                statusCode(200).
                body("ErrorCode",equalTo(1)).
                body("ActionStatus",equalTo("FAIL")).
                body("ErrorInfo",notNullValue());
        logout(sessionId);
    }
}
