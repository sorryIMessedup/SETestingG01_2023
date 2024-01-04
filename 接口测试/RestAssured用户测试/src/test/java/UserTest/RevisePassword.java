package UserTest;

import io.restassured.http.ContentType;
import io.restassured.response.Response;
import org.junit.Test;

import java.security.MessageDigest;

import static io.restassured.RestAssured.given;
import static org.hamcrest.Matchers.equalTo;
import static org.hamcrest.Matchers.nullValue;

public class RevisePassword {

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
        public void correctRevisepasswordTest(){
            String sessionId = getLoginSession("ecnu_admin","pl,okm123");

            String request = "{" +
                    " \"oldPassword\": \"e10adc3949ba59abbe56e057f20f883e\",\n" +
                    " \"newPassword\": \"fcea920f7412b5da7be0cf42b8c93759\"\n" +
                    "}";
            given().
                    cookie("JSESSIONID",sessionId).
                    body(request).contentType(ContentType.JSON).
                    when().
                    post(url + "/user/password").
                    then().
                    statusCode(200).
                    body("code",equalTo(0)).
                    body("message",equalTo("OK"));
            logout(sessionId);
        }

        @Test
        public void nullOldPasswordRevisePasswordTest(){
            String sessionId = getLoginSession("ecnu_admin","pl,okm123");
            String request = "{" +
                    " \"oldPassword\": \"\",\n" +
                    " \"password\": \"fcea920f7412b5da7be0cf42b8c93759\"\n" +
                    "}";
            given().
                    cookie("JSESSIONID",sessionId).
                    body(request).contentType(ContentType.JSON).
                    when().
                    post(url + "/user/password").
                    then().
                    statusCode(200).
                    body("code",equalTo(-1)).
                    body("message",equalTo("key [oldPassword] failed on checker com.cloume.ecnu.psy.hotline.controller.MSUserController$$Lambda$1747/261441945@265be8d7 with value []")).
                    body("result",nullValue());
            logout(sessionId);
        }

        @Test
        public void nullPasswordRevisePasswordTest(){
            String sessionId = getLoginSession("ecnu_admin","pl,okm123");
            String request =  "{" +
                    " \"oldPassword\": \"e10adc3949ba59abbe56e057f20f883e\",\n" +
                    " \"password\": \"\"\n" +
                    "}";
            given().
                    cookie("JSESSIONID",sessionId).
                    body(request).contentType(ContentType.JSON).
                    when().
                    post(url + "/user/password").
                    then().
                    body("code",equalTo(-1)).
                    body("message",equalTo("key [oldPassword] failed on checker com.cloume.ecnu.psy.hotline.controller.MSUserController$$Lambda$1747/261441945@265be8d7 with value []")).
                    body("result",nullValue());
            logout(sessionId);
        }

        @Test
        public void wrongPasswordTest(){
            String sessionId = getLoginSession("ecnu_admin","pl,okm123");
            String request = "{" +
                    " \"oldPassword\": \"e10adc3949ba59abbe56e057f20f883e\",\n" +
                    " \"newPassword\": \"fcea920f7412b5da7be0cf42b8c93759\"\n" +
                    "}";
            given().
                    cookie("JSESSIONID",sessionId).
                    body(request).contentType(ContentType.JSON).
                    when().
                    post(url + "/user/password").
                    then().
                    body("code",equalTo(-1)).
                    body("message",equalTo("原密码错误")).
                    body("result",nullValue());
            logout(sessionId);
        }





}
