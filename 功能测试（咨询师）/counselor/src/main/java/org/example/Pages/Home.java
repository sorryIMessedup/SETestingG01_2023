package org.example.Pages;

import org.example.Setting;
import org.openqa.selenium.By;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.interactions.Actions;

public class Home extends BasicPage{
    public Home(){
        pageUrl = Setting.HomePageUrl;
        title = Setting.HomePageTitle;
    }

    /**
     * 修改密码
     * */
    public void changePassword(String old_password, String new_password, String again_new_password) throws InterruptedException {
        verify();
        {
            WebElement element = driver.findElement(By.cssSelector(".userMenuBar"));
            Actions builder = new Actions(driver);
            builder.moveToElement(element).perform();
        }
        driver.findElement(By.cssSelector(".menuActionItem > span:nth-child(1)")).click();
        driver.findElement(By.cssSelector(".el-row:nth-child(1) .el-input__inner")).click();
        driver.findElement(By.cssSelector(".el-row:nth-child(1) .el-input__inner")).clear();
        driver.findElement(By.cssSelector(".el-row:nth-child(1) .el-input__inner")).sendKeys(old_password);
        driver.findElement(By.cssSelector(".el-row:nth-child(2) .el-input__inner")).click();
        driver.findElement(By.cssSelector(".el-row:nth-child(2) .el-input__inner")).clear();
        driver.findElement(By.cssSelector(".el-row:nth-child(2) .el-input__inner")).sendKeys(new_password);
        driver.findElement(By.cssSelector(".el-row:nth-child(3) .el-input__inner")).click();
        driver.findElement(By.cssSelector(".el-row:nth-child(3) .el-input__inner")).clear();
        driver.findElement(By.cssSelector(".el-row:nth-child(3) .el-input__inner")).sendKeys(again_new_password);
        driver.findElement(By.cssSelector(".el-dialog__footer:nth-child(3) .confirm")).click();
        try {driver.findElement(By.cssSelector(".el-dialog__footer:nth-child(3) .cancel > span")).click();}
        catch (Exception e){}
        Thread.sleep(Setting.timeout);
    }

    /**
     * 登出
     * */
    public void logout(){
        verify();
        {
            WebElement element = driver.findElement(By.cssSelector(".userMenuBar"));
            Actions builder = new Actions(driver);
            builder.moveToElement(element).perform();
        }
        driver.findElement(By.cssSelector(".menuActionItem > span:nth-child(2)")).click();
        new Login().verify();
    }

    /**
     * @param num 直接设置的次数
     * @param n2 点击添加按钮的次数
     * @param n3 点击减少按钮的次数
     * */
    public void setConsultantNumber(String num,int n2,int n3) throws InterruptedException {
        driver.findElement(By.cssSelector(".referSet > span")).click();
        driver.findElement(By.cssSelector(".el-input__inner")).clear();
        driver.findElement(By.cssSelector(".el-input__inner")).sendKeys(num+"");
        for(int i = 0; i < n2; i ++ ){
            driver.findElement(By.cssSelector(".el-icon-plus")).click();
        }
        for(int i = 0; i < n3; i ++ ){
            driver.findElement(By.cssSelector(".el-icon-minus")).click();
        }
        driver.findElement(By.cssSelector(".el-dialog__footer:nth-child(3) .confirm")).click();
        Thread.sleep(Setting.timeout);
    }
    @Override
    public void moveTo(){
        driver.findElement(By.cssSelector(".el-menu-item:nth-child(1)")).click();
    }
}
