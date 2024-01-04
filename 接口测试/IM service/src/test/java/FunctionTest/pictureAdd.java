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

public class pictureAdd {
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
    public void pictureAddTest(){
        page.openUrl();
        page.login("zixunshi1","123456");
        page.findElementByCss(".el-button");
        int size = communication.getElementSize(".textOverFlow");
        assert(size > 0);
        page.enterSession();
        boolean isEditable = communication.isEditable(".text-input");
        assertTrue(isEditable);
        communication.focusOnElement(".text-input");
        page.findElementByCss(".el-tooltip > .el-button");
        page.findElementByTag("body");
        communication.sendMessage(".text-input","怎么了");
        communication.focusOnElement(".el-tooltip span");
        assertThat(driver.findElement(By.cssSelector(".message-content > img:nth-child(1)")).getText(), is("[流泪]"));
        communication.focusOnElement(".message-content > img:nth-child(1)");
        communication.focusOnElement(".focusing span");
        assertThat(driver.findElement(By.cssSelector(".message-wrapper:nth-child(5) .col-2 img")).getText(), is("[委屈]"));
        communication.focusOnElement(".message-wrapper:nth-child(5) .col-2 img");
        communication.focusOnElement(".text-input");
        communication.focusOnElement(".icon-xiaolian");
        size = communication.getElementSize(".emoji:nth-child(70) > img");
        assert(size > 0);
        communication.focusOnElement(".emoji:nth-child(70) > img");
        communication.focusOnElement(".text-input");
        communication.focusOnElement(".focusing span");
        assertThat(driver.findElement(By.cssSelector(".message-wrapper:nth-child(7) .content-wrapper span")).getText(), is("?"));
        communication.focusOnElement(".message-wrapper:nth-child(7) .content-wrapper span");
        size = communication.getElementSize(".image-element");
        assert(size > 0);
        communication.focusOnElement(".image-element");
        size = communication.getElementSize(".el-icon-right");
        assert(size > 0);
        communication.focusOnElement(".el-icon-right");
        communication.focusOnElement(".image-preview");
        size = communication.getElementSize(".close-button");
        assert(size > 0);
        communication.focusOnElement(".close-button");
        size = communication.getElementSize(".btns > div:nth-child(1)");
        assert(size > 0);
        communication.focusOnElement(".btns > div:nth-child(1)");
        size = communication.getElementSize(".el-button--default:nth-child(2) > span");
        assert(size > 0);
        communication.focusOnElement(".el-button--default:nth-child(2) > span");
        page.findElementByCss(".el-button--default:nth-child(2) > span");
        page.findElementByTag("body");
    }

    @Test
    public void pictureAddTest2(){
        page.openUrl();
        page.login("zixunshi1","123456");
        int size = communication.getElementSize(".name > span:nth-child(2)");
        assert(size > 0);
        page.enterSession();
        boolean isEditable = communication.isEditable(".text-input");
        assertTrue(isEditable);
        communication.focusOnElement(".text-input");
        size = communication.getElementSize(".message-send > img");
        assert(size > 0);
        communication.focusOnElement(".message-send > img");
        communication.focusOnElement(".message-send > span");
        page.findElementByCss(".el-tooltip > .el-button");
        page.findElementByTag("body");
        communication.focusOnElement("path");
        communication.focusOnElement(".el-button--text > span");
        size = communication.getElementSize(".image-element");
        assert(size > 0);
        communication.focusOnElement(".image-element");
        communication.focusOnElement(".el-icon-back");
        communication.focusOnElement(".image-wrapper");
        size = communication.getElementSize(".close-button");
        assert(size > 0);
        communication.focusOnElement(".close-button");
        communication.focusOnElement(".focusing .iconfont");
        communication.focusOnElement(".message-wrapper:nth-child(8) .date");
        communication.focusOnElement(".focusing span");
        size = communication.getElementSize(".focusing img");
        assert(size > 0);
        communication.focusOnElement(".focusing img");
        communication.focusOnElement(".name > span:nth-child(2)");
        page.findElementByCss(".el-button--default:nth-child(2) > span");
        page.findElementByTag("body");
    }
}
