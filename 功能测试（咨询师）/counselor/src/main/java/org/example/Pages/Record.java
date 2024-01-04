package org.example.Pages;

import org.example.Setting;
import org.openqa.selenium.By;


public class Record extends BasicPage{

    public Record(){
        pageUrl = Setting.RecordPageUrl;
        title = Setting.RecordPageTitle;
    }

    /**
     * @param name 搜索访客的姓名
     * @param from 开始日期
     * @param ftime 当日时间
     * @param to 结束日期
     * @param ttime 结束当日时间
     * */
    public void searchForRecords(String name,String from, String ftime, String to, String ttime) throws InterruptedException {
        verify();
        driver.findElement(By.cssSelector(".nameInput > .el-input__inner")).clear();
        driver.findElement(By.cssSelector(".nameInput > .el-input__inner")).sendKeys(name);
        driver.findElement(By.cssSelector(".el-range-input:nth-child(2)")).click();
        driver.findElement(By.cssSelector(".el-date-range-picker__editors-wrap:nth-child(1) > " +
                ".el-date-range-picker__time-picker-wrap:nth-child(1) .el-input__inner")).clear();
        driver.findElement(By.cssSelector(".el-date-range-picker__editors-wrap:nth-child(1) > " +
                ".el-date-range-picker__time-picker-wrap:nth-child(1) .el-input__inner")).sendKeys(from);
        driver.findElement(By.cssSelector(".el-date-range-picker__editors-wrap:nth-child(1) > " +
                ".el-date-range-picker__time-picker-wrap:nth-child(2) .el-input__inner")).clear();
        driver.findElement(By.cssSelector(".el-date-range-picker__editors-wrap:nth-child(1) > " +
                ".el-date-range-picker__time-picker-wrap:nth-child(2) .el-input__inner")).sendKeys(ftime);
        driver.findElement(By.cssSelector(".is-right > .el-date-range-picker__time-picker-wrap:nth-child(1)" +
                " .el-input__inner")).clear();
        driver.findElement(By.cssSelector(".is-right > .el-date-range-picker__time-picker-wrap:nth-child(1)" +
                " .el-input__inner")).sendKeys(to);
        driver.findElement(By.cssSelector(".is-right > .el-date-range-picker__time-picker-wrap:nth-child(2)" +
                " .el-input__inner")).clear();
        driver.findElement(By.cssSelector(".is-right > .el-date-range-picker__time-picker-wrap:nth-child(2)" +
                " .el-input__inner")).sendKeys(ttime);
        driver.findElement(By.cssSelector(".is-plain")).click();
    }

    /**
     * 检查查找到的数据是否一致
     * */
    public String checkFirstRecordName() throws InterruptedException {
        verify();
        driver.findElement(By.cssSelector(".tableBtn:nth-child(1)")).click();
        Thread.sleep(Setting.timeout);
        return driver.findElement(By.cssSelector(".userCard span:nth-child(1)")).getText();
    }

    @Override
    public void moveTo(){
        driver.findElement(By.cssSelector(".el-menu-item:nth-child(2)")).click();
    }
}
