package org.example.Pages;

import org.example.Setting;
import org.openqa.selenium.By;


public class Login extends BasicPage{

    /**
     * 设置基本参数
     * */
    public Login(){
        pageUrl = Setting.LoginPageUrl;
        title = Setting.LoginPageTitle;
    }

    /**
     * 当测试别的功能的时候，需要正常登录
     * */
    public void login() throws InterruptedException {
        login(Setting.CorrectUserName, Setting.CorrectPassWord);
    }

    /**
     * @param username 待测试的用户名
     * @param password 待测试的密码
     * */
    public void login(String username, String password) throws InterruptedException {
        verify();
        driver.findElement(By.cssSelector(".el-form-item:nth-child(1) .el-input__inner")).click();
        driver.findElement(By.cssSelector(".el-form-item:nth-child(1) .el-input__inner")).sendKeys(username);
        driver.findElement(By.cssSelector(".el-form-item:nth-child(2) .el-input__inner")).click();
        driver.findElement(By.cssSelector(".el-form-item:nth-child(2) .el-input__inner")).sendKeys(password);
        driver.findElement(By.cssSelector(".el-button")).click();
        Thread.sleep(Setting.timeout);
    }

    @Override
    public void moveTo() {}
}
