import org.example.Setting;
import org.example.Pages.Driver;
import org.junit.After;
import org.junit.Before;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.WebDriver;

import java.util.Map;

public class BasicTest {
    public WebDriver driver;
    public Map<String, Object> vars;
    JavascriptExecutor js;
    @Before
    public void setUp() {
        driver = Driver.getInstance();
        js = (JavascriptExecutor) driver;
        vars = Driver.getVars();
        driver.get(Setting.BasicPageUrl);
    }
    @After
    public void tearDown() {
        //driver.quit();
    }
}
