package Functions;

import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;

import java.util.HashMap;
import java.util.Map;
import java.util.Set;

public class Driver {
    private static WebDriver driver;
    private static Map<String, Object> vars;
    private static JavascriptExecutor js;

    private Driver(){}

    public static WebDriver getDriver(){
        if(driver == null){
            System.setProperty("webdriver.chrome.driver","E:\\ChromeDriver\\chromedriver.exe");
            driver = new ChromeDriver();
        }
        return driver;
    }

    public static Map<String, Object> getVars() {
        if(vars == null){
            vars = new HashMap<String, Object>();
        }
        return vars;
    }

    public static JavascriptExecutor getJs(){
        if(js == null){
            js = (JavascriptExecutor) driver;
        }
        return js;
    }

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
