package FunctionTest;

import Functions.Communication;
import Functions.Page;
import org.junit.After;
import org.junit.Before;
import org.junit.Test;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.WebDriver;

import java.util.Map;

import static Functions.Driver.*;
import static org.junit.Assert.assertTrue;

public class addRecord {
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
    public void addRecordTest(){
        page.openUrl();
        page.login("zixunshi1","123456");
        page.findElementByCss(".el-button > span");
        page.findElementByTag("body");
        page.findElementByCss(".el-button > span");
        page.enterSession();
        boolean isEditable = communication.isEditable(".text-input");
        assertTrue(isEditable);
        communication.focusOnElement(".text-input");
        isEditable = communication.isEditable(".customShareMessage > span:nth-child(2)");
        assertTrue(isEditable);
        communication.focusOnElement(".customShareMessage > span:nth-child(2)");
        int size = communication.getElementSize(".free > span");
        assert(size > 0);
        communication.focusOnElement(".free > span");
        page.findElementByCss(".free > span");
        page.findElementByTag("body");
        size = communication.getElementSize(".seleHistoruModal > .el-dialog__footer:nth-child(3) .el-button");
        assert(size > 0);
        communication.focusOnElement(".seleHistoruModal > .el-dialog__footer:nth-child(3) .el-button");
        size = communication.getElementSize(".seleModal > .el-dialog__footer:nth-child(3) .el-button");
        assert(size > 0);
        communication.focusOnElement(".seleModal > .el-dialog__footer:nth-child(3) .el-button");
        communication.focusOnElement(".text-input");
        size = communication.getElementSize(".el-menu-vertical-demo:nth-child(1) > .el-menu-item:nth-child(2)");
        assert(size > 0);
        communication.focusOnElement(".el-menu-vertical-demo:nth-child(1) > .el-menu-item:nth-child(2)");
        communication.focusOnElement(".name > span:nth-child(2)");
        communication.focusOnElement(".el-table__row:nth-child(2) .el-button:nth-child(1) > span");
    }

    @Test
    public void addRecordTest2(){
        page.openUrl();
        page.login("zixunshi1","123456");
        page.findElementByCss(".el-button");
        page.findElementByCss(".el-button");
        page.enterSession();
        communication.focusOnElement(".text-input");
        int size = communication.getElementSize(".customShareMessage > span:nth-child(2)");
        assert(size > 0);
        communication.focusOnElement(".customShareMessage > span:nth-child(2)");
        communication.focusOnElement(".free > span");
        communication.focusOnElement(".focusing .text");
        size = communication.getElementSize(".seleHistoruModal > .el-dialog__footer:nth-child(3) span");
        assert(size > 0);
        communication.focusOnElement(".seleHistoruModal > .el-dialog__footer:nth-child(3) span");
        size = communication.getElementSize(".seleModal > .el-dialog__footer:nth-child(3) .el-button");
        assert(size > 0);
        communication.focusOnElement(".seleModal > .el-dialog__footer:nth-child(3) .el-button");
        size = communication.getElementSize(".btns > div:nth-child(1)");
        assert(size > 0);
        communication.focusOnElement(".btns > div:nth-child(1)");
        page.findElementByTag("body");
        js.executeScript("window.scrollTo(0,0)");
        size = communication.getElementSize(".el-button--default:nth-child(2) > span");
        assert(size > 0);
        communication.focusOnElement(".el-button--default:nth-child(2) > span");
        communication.focusOnElement(".focusing span");
        communication.focusOnElement(".el-button--default:nth-child(2) > span");
    }
}
