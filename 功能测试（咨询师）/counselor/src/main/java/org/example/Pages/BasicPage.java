package org.example.Pages;

import org.example.Setting;
import org.openqa.selenium.WebDriver;
import static org.junit.Assert.*;

import java.util.Map;

public abstract class BasicPage {
    public String pageUrl = Setting.BasicPageUrl;
    public String title = "";
    public Map<String, Object> vars = Driver.getVars();
    public WebDriver driver = Driver.getInstance();
    public void assertIsCurrentPage(){
        assertEquals("页面",pageUrl,driver.getCurrentUrl());
    }
    public void verifyTitle(){
        assertEquals("标题",title,driver.getTitle());
    }

    /**
     * 用于验证当前页面是否为目标页面以及title是否相同
     * */
    public void verify(){
        assertIsCurrentPage();
        verifyTitle();
    }

    /**
     * 判断现在的页面是不是当前页面
     * */
    public boolean isCurrentPage(){
        if(pageUrl.equals(driver.getCurrentUrl()) && title.equals(driver.getTitle())) return true;
        return false;
    }

    /**
     * 移动到当前页面
     * */
    public abstract void moveTo();

}
