package Functions;

import org.openqa.selenium.By;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;

import java.util.List;
import java.util.Map;

import static Functions.Driver.*;

public class Communication {
    private WebDriver driver;
    private Map<String, Object> vars;
    private JavascriptExecutor js;

    public Communication(){
        driver = getDriver();
        vars = getVars();
        js = getJs();
    }

    public void focusOnElement(String css){
        driver.findElement(By.cssSelector(css)).click();
    }

    public boolean isEditable(String css){
        WebElement element = driver.findElement(By.cssSelector(css));
        boolean editable = element.isEnabled() && element.getAttribute("readonly") == null;
        return editable;
    }

    public int getElementSize(String css){
        List<WebElement> elements = driver.findElements(By.cssSelector(css));
        return elements.size();
    }

    public void sendMessage(String css, String message){
        driver.findElement(By.cssSelector(css)).sendKeys(message);
    }
}
