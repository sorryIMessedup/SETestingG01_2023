package Functions;

import org.openqa.selenium.*;
import org.openqa.selenium.interactions.Actions;

import java.util.Map;

import static Functions.Driver.*;

public class Page {
    private WebDriver driver;
    private Map<String, Object> vars;
    private JavascriptExecutor js;

    public Page(){
        driver = getDriver();
        vars = getVars();
        js = getJs();
    }

    public void openUrl(){
        driver.get("https://sei-test.021hqit.com/group-4/");
        driver.manage().window().setSize(new Dimension(1053, 808));
    }

    public void login(String username, String password){
        driver.findElement(By.cssSelector(".el-form-item:nth-child(1) .el-input__inner")).click();
        driver.findElement(By.cssSelector(".el-form-item:nth-child(1) .el-input__inner")).sendKeys(username);
        driver.findElement(By.cssSelector(".el-form-item:nth-child(2) .el-input__inner")).click();
        driver.findElement(By.cssSelector(".el-form-item:nth-child(2) .el-input__inner")).sendKeys(password);
        driver.findElement(By.cssSelector(".el-button > span")).click();
    }

    public void findElementByCss(String css){
        WebElement element = driver.findElement(By.cssSelector(css));
        Actions builder = new Actions(driver);
        builder.moveToElement(element).perform();
    }

    public void findElementByTag(String tag){
        WebElement element = driver.findElement(By.tagName(tag));
        Actions builder = new Actions(driver);
        builder.moveToElement(element, 0, 0).perform();
    }

    public void enterSession(){
        driver.findElement(By.cssSelector(".textOverFlow")).click();
    }

    public void goIntoConsult(){
        driver.findElement(By.cssSelector(".name > span:nth-child(2)")).click();
    }
}
