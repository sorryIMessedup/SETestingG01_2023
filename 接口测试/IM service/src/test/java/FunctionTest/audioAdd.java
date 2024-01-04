package FunctionTest;

import Functions.Communication;
import Functions.Page;
import org.junit.After;
import org.junit.Before;
import org.junit.Test;
import org.openqa.selenium.By;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.WebDriver;

import java.util.Map;

import static Functions.Driver.*;
import static org.hamcrest.CoreMatchers.is;
import static org.junit.Assert.assertThat;
import static org.junit.Assert.assertTrue;

public class audioAdd {
    private WebDriver driver;
    private Map<String, Object> vars;
    JavascriptExecutor js;

    Page page = new Page();
    Communication communication = new Communication();

    @Before
    public void setUp() {
        driver = getDriver();
        js = getJs();
        vars = getVars();
    }

    @After
    public void tearDown() {
        driver.quit();
    }

    @Test
    public void audioAddTest(){
        page.openUrl();
        page.login("zixunshi1","123456");
        int size = communication.getElementSize(".name > span:nth-child(2)");
        assert(size > 0);
        page.goIntoConsult();
        assertThat(driver.findElement(By.cssSelector(".message-content > img")).getText(), is("[调皮]"));
        communication.focusOnElement(".message-content > img");
        size = communication.getElementSize(".icon-xiaolian");
        assert(size > 0);
        communication.focusOnElement(".icon-xiaolian");
        size = communication.getElementSize(".emoji:nth-child(25) > img");
        assert(size > 0);
        communication.focusOnElement(".emoji:nth-child(25) > img");
        boolean isEditable = communication.isEditable(".text-input");
        assertTrue(isEditable);
        communication.focusOnElement(".text-input");
        size = communication.getElementSize(".icon-voice");
        assert(size > 0);
        communication.focusOnElement(".icon-voice");
        communication.focusOnElement(".sound-element-wrapper");
        page.findElementByCss(".el-tooltip > .el-button");
        page.findElementByTag("body");
        size = communication.getElementSize(".image-element");
        assert(size > 0);
        communication.focusOnElement(".image-element");
        communication.focusOnElement(".el-icon-back");
        communication.focusOnElement(".image-wrapper");
        size = communication.getElementSize(".close-button");
        assert(size > 0);
        communication.focusOnElement(".close-button");
        communication.focusOnElement(".text-input");
        js.executeScript("window.scrollTo(0,0)");
        communication.focusOnElement(".focusing .iconfont");
        assertThat(driver.findElement(By.cssSelector(".message-wrapper:nth-child(7) .sound-element-wrapper")).getText(), is("能解决吗"));
        communication.focusOnElement(".message-wrapper:nth-child(7) .sound-element-wrapper");
        size = communication.getElementSize(".message-wrapper:nth-child(8) .date");
        assert(size > 0);
        communication.focusOnElement(".message-wrapper:nth-child(8) .date");
        communication.focusOnElement(".text-input");
        js.executeScript("window.scrollTo(0,0)");
        communication.focusOnElement(".focusing span");
        size = communication.getElementSize(".tim-icon-close");
        assert(size > 0);
        communication.focusOnElement(".tim-icon-close");
        communication.focusOnElement(".el-button--default:nth-child(2) > span");
        page.findElementByCss(".el-button--default:nth-child(2)");
        page.findElementByTag("body");
    }

    @Test
    public void audioAddTest2(){
        page.openUrl();
        page.login("zixunshi1","123456");
        int size = communication.getElementSize(".name > span:nth-child(2)");
        assert(size > 0);
        page.goIntoConsult();
        assertThat(driver.findElement(By.cssSelector(".message-content > span")).getText(), is("哈哈"));
        communication.focusOnElement(".message-content > span");
        size = communication.getElementSize(".icon-xiaolian");
        assert(size > 0);
        communication.focusOnElement(".icon-xiaolian");
        boolean isEditable = communication.isEditable(".text-input");
        assertTrue(isEditable);
        communication.focusOnElement(".text-input");
        size = communication.getElementSize(".message-send > img");
        assert(size > 0);
        communication.focusOnElement(".message-send > img");
        size = communication.getElementSize(".el-button--mini:nth-child(2) > span");
        assert(size > 0);
        communication.focusOnElement(".el-button--mini:nth-child(2) > span");
        page.findElementByCss(".el-tooltip > .el-button");
        page.findElementByTag("body");
        communication.focusOnElement("path");
        communication.focusOnElement(".el-button--text > span");
        size = communication.getElementSize(".icon-voice");
        assert(size > 0);
        communication.focusOnElement(".icon-voice");
        communication.focusOnElement(".sound-element-wrapper");
        communication.focusOnElement(".text-input");
        js.executeScript("window.scrollTo(0,0)");
        communication.focusOnElement(".focusing .iconfont");
        communication.focusOnElement(".focusing img");
        assertThat(driver.findElement(By.cssSelector(".message-wrapper:nth-child(11) .content-wrapper span")).getText(), is("哼"));
        communication.focusOnElement(".message-wrapper:nth-child(11) .content-wrapper span");
        size = communication.getElementSize(".message-wrapper:nth-child(11) .col-2 img");
        assert(size > 0);
        communication.focusOnElement(".message-wrapper:nth-child(11) .col-2 img");
        communication.focusOnElement(".name > span:nth-child(2)");
        communication.focusOnElement(".tim-icon-close");
        page.findElementByCss(".el-button--default:nth-child(2)");
        page.findElementByTag("body");
    }
}
