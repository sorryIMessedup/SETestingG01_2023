package org.example.Pages;

import org.example.Setting;
import org.openqa.selenium.Keys;
import org.openqa.selenium.By;


public class Vistor extends BasicPage{

    public Vistor(){
        pageUrl = Setting.VistorPageUrl;
        title = Setting.VistorPageTitle;
    }

    /**
     * @param name 搜索的名字
     * */
    public String searchFor(String name) throws InterruptedException {
        verify();
        driver.findElement(By.cssSelector(".el-input:nth-child(2) > .el-input__inner")).clear();
        driver.findElement(By.cssSelector(".el-input:nth-child(2) > .el-input__inner")).sendKeys(name);
        driver.findElement(By.cssSelector(".el-input:nth-child(2) > .el-input__inner")).sendKeys(Keys.ENTER);
        Thread.sleep(Setting.timeout);
        try {
            return driver.findElement(By.cssSelector(".tableAvatar > span:nth-child(2)")).getText();
        }catch (Exception e){
            return "";
        }
    }

    /**
     * 禁用
     * */
    public void ban() {
        verify();
        driver.findElement(By.cssSelector(".tableBtn")).click();
        driver.findElement(By.cssSelector(".el-button--default:nth-child(2)")).click();
    }

    @Override
    public void moveTo() {
        driver.findElement(By.cssSelector(".el-menu-item:nth-child(4)")).click();
    }
}
