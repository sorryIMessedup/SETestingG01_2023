package org.example.Pages;

import org.example.Setting;
import org.openqa.selenium.By;

public class Schedule extends BasicPage{
    public Schedule(){
        pageUrl = Setting.SchedulePageUrl;
        title = Setting.SchedulePageTitle;
    }

    /**
     * 访问对应日期当中的咨询师和督导的记录
     * */
    public void checkDate(int[] num){
        for(int i = 0; i < num.length; i ++ ){
            driver.findElement(By.cssSelector(".dateItem:nth-child(" + num[i] + ")")).click();
            driver.findElement(By.cssSelector(".el-col:nth-child(1)")).click();
            driver.findElement(By.cssSelector(".el-col:nth-child(2)")).click();
        }
    }

    @Override
    public void moveTo() {
        driver.findElement(By.cssSelector(".el-menu-item:nth-child(3)")).click();
    }
}