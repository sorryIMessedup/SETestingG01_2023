package org.example.Pages;

import org.openqa.selenium.WebDriver;
import org.openqa.selenium.edge.EdgeDriver;

import java.util.HashMap;
import java.util.Map;
import java.util.Set;

public class Driver {
    static { System.setProperty("webdriver.edge.driver","D:\\Java\\jdk1.8.0_251\\bin\\msedgedriver.exe"); }
    private static WebDriver driver = new EdgeDriver();
    private static Map<String, Object> vars = new HashMap<>();

    private Driver() {
    }

    public static WebDriver getInstance() {
        return driver;
    }

    public static Map<String, Object> getVars(){return vars;};

    public static String waitForWindow(int timeout){
        try{
            Thread.sleep((timeout));
        } catch (InterruptedException e){
            e.printStackTrace();
        }
        Set<String> whNow = driver.getWindowHandles();
        Set<String> whThen = (Set<String>) vars.get("window_handles");
        if(whNow.size() > whThen.size()){
            whNow.removeAll(whThen);
        }
        return whNow.iterator().next();
    }
}
