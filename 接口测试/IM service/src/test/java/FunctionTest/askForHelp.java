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

public class askForHelp {
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
    public void askForHelpTest(){
        page.openUrl();
        page.login("zixunshi1","123456");
        page.findElementByCss(".el-button");
        page.findElementByCss(".el-button");
        int size = communication.getElementSize(".name > span:nth-child(2)");
        assert(size > 0);
        page.goIntoConsult();
        boolean isEditable = communication.isEditable(".text-input");
        assertTrue(isEditable);
        communication.focusOnElement(".text-input");
        size = communication.getElementSize(".customShareMessage > span:nth-child(2)");
        assert(size > 0);
        communication.focusOnElement(".customShareMessage > span:nth-child(2)");
        communication.focusOnElement(".free > span");
        size = communication.getElementSize(".focusing .text");
        assert(size > 0);
        communication.focusOnElement(".focusing .text");
        size = communication.getElementSize(".seleHistoruModal > .el-dialog__footer:nth-child(3) span");
        assert(size > 0);
        communication.focusOnElement(".seleHistoruModal > .el-dialog__footer:nth-child(3) span");
        communication.focusOnElement(".seleModal > .el-dialog__footer:nth-child(3) .el-button");
        communication.focusOnElement(".el-button--default:nth-child(2) > span");
        page.findElementByCss(".footer:nth-child(2) > #message-send-box-wrapper > .bottom .el-button");
        communication.focusOnElement(".noActive");
        assertThat(driver.findElement(By.cssSelector("#el-popover-3547 .emoji:nth-child(88) > img")).getText(), is("[猪头]"));
        communication.focusOnElement("#el-popover-3547 .emoji:nth-child(88) > img");
        assertThat(driver.findElement(By.cssSelector(".footer:nth-child(7) > #message-send-box-wrapper .text-input")).getText(), is("好吧"));
        communication.focusOnElement(".footer:nth-child(7) > #message-send-box-wrapper .text-input");
        page.findElementByCss(".footer:nth-child(3) > #message-send-box-wrapper > .bottom .el-button");
        page.findElementByTag("body");
        js.executeScript("window.scrollTo(0,0)");
        communication.focusOnElement(".finished > .finishIcon");
        size = communication.getElementSize(".el-button--default:nth-child(2) > span");
        assert(size > 0);
        communication.focusOnElement(".el-button--default:nth-child(2) > span");
        communication.focusOnElement(".focusing span");
        communication.focusOnElement(".btns > div:nth-child(2)");
        communication.focusOnElement(".el-button--default:nth-child(2) > span");
    }

    @Test
    public void askForHelpTest2(){
        page.openUrl();
        page.login("zixunshi1","123456");
        page.findElementByCss(".el-button");
        page.findElementByCss(".el-button");
        int size = communication.getElementSize(".name > span:nth-child(2)");
        assert(size > 0);
        page.goIntoConsult();
        size = communication.getElementSize(".btns > div:nth-child(1)");
        assert(size > 0);
        communication.focusOnElement(".btns > div:nth-child(1)");
        boolean isEditable = communication.isEditable(".text-input");
        assertTrue(isEditable);
        communication.focusOnElement(".text-input");
        communication.focusOnElement(".free > span");
        size = communication.getElementSize(".el-button--default:nth-child(2) > span");
        assert(size > 0);
        communication.focusOnElement(".el-button--default:nth-child(2) > span");
        page.findElementByCss(".footer:nth-child(2) > #message-send-box-wrapper > .bottom .el-button");
        communication.focusOnElement(".noActive");
        assertThat(driver.findElement(By.cssSelector(".footer:nth-child(3) > #message-send-box-wrapper .text-input")).getText(), is("不要怕"));
        communication.focusOnElement(".footer:nth-child(3) > #message-send-box-wrapper .text-input");
        assertThat(driver.findElement(By.cssSelector("#el-popover-3547 .emoji:nth-child(81) > img")).getText(), is("[ok]"));
        communication.focusOnElement("#el-popover-3547 .emoji:nth-child(81) > img");
        size = communication.getElementSize(".finished > .finishIcon");
        assert(size > 0);
        communication.focusOnElement(".finished > .finishIcon");
        size = communication.getElementSize(".finished > .finishIcon");
        assert(size > 0);
        communication.focusOnElement(".finished > .finishIcon");
        size = communication.getElementSize(".btns > div:nth-child(2)");
        assert(size > 0);
        communication.focusOnElement(".btns > div:nth-child(2)");
        communication.focusOnElement(".el-button--default:nth-child(2) > span");
    }
}
