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

public class textInput {
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
    public void textInputTest(){
        page.openUrl();
        page.login("zixunshi1","123456");
        page.findElementByCss(".el-button > span");
        page.findElementByTag("body");
        page.findElementByCss(".el-button > span");
        page.enterSession();
        assertThat(driver.findElement(By.cssSelector(".message-content > span")).getText(), is("我来了"));
        boolean isEditable = communication.isEditable(".text-input");
        assertTrue(isEditable);
        communication.focusOnElement(".text-input");
        page.findElementByCss(".el-tooltip > .el-button");
        page.findElementByTag("body");
        communication.sendMessage(".text-input","你好");
        int size = communication.getElementSize(".el-tooltip > .el-button");
        assert(size > 0);
        communication.focusOnElement(".el-tooltip > .el-button");
        communication.focusOnElement(".message-send > span");
        communication.focusOnElement(".message-status > span");
        assertThat(driver.findElement(By.cssSelector(".message-wrapper:nth-child(3) .content-wrapper span")).getText(), is("咨询一下。"));
        communication.focusOnElement(".text-input");
        size = communication.getElementSize(".free > span");
        assert(size > 0);
        communication.focusOnElement(".free > span");
        page.findElementByCss(".free > span");
        page.findElementByTag("body");
        communication.focusOnElement(".text-input");
        communication.sendMessage(".text-input","知道了。");
        communication.focusOnElement(".el-tooltip span");
        page.findElementByCss(".el-tooltip span");
        page.findElementByTag("body");
        assertThat(driver.findElement(By.cssSelector(".message-wrapper:nth-child(6) .content-wrapper span")).getText(), is("怎么样？"));
        communication.focusOnElement(".text-input");
        communication.focusOnElement(".noActive");
        size = communication.getElementSize(".btns > div:nth-child(2)");
        assert(size > 0);
        communication.focusOnElement(".btns > div:nth-child(2)");
        communication.focusOnElement(".el-menu-vertical-demo:nth-child(1) > .el-menu-item:nth-child(2)");
        communication.focusOnElement(".name > span:nth-child(2)");
        size = communication.getElementSize(".el-table__row:nth-child(2) .el-button:nth-child(1) > span");
        assert(size > 0);
        communication.focusOnElement(".el-table__row:nth-child(2) .el-button:nth-child(1) > span");
    }

    @Test
    public void textInputTest2(){
        page.openUrl();
        page.login("zixunshi1","123456");
        page.findElementByCss(".el-button > span");
        page.enterSession();
        page.findElementByCss(".el-tooltip > .el-button");
        page.findElementByTag("body");
        assertThat(driver.findElement(By.cssSelector(".message-content > span")).getText(), is("什么意思？"));
        communication.focusOnElement(".el-tooltip span");
        page.findElementByCss(".el-tooltip span");
        page.findElementByTag("body");
        int size = communication.getElementSize(".message-send > span");
        assert(size > 0);
        communication.focusOnElement(".message-send > span");
        communication.focusOnElement(".text-input");
        size = communication.getElementSize(".seleModal > .el-dialog__footer:nth-child(3) .el-button");
        assert(size > 0);
        communication.focusOnElement(".seleModal > .el-dialog__footer:nth-child(3) .el-button");
        communication.focusOnElement(".btns > div:nth-child(2)");
        communication.focusOnElement(".el-table__row:nth-child(2) .el-button:nth-child(1) > span");
    }

    @Test
    public void textInputTest3(){
        page.openUrl();
        page.login("zixunshi1","123456");
        page.findElementByCss(".el-button");
        int size = communication.getElementSize(".textOverFlow");
        assert(size > 0);
        page.enterSession();
        assertThat(driver.findElement(By.cssSelector(".message-content > span")).getText(), is("你好"));
        communication.focusOnElement(".message-content > span");
        boolean isEditable = communication.isEditable(".text-input");
        assertTrue(isEditable);
        communication.focusOnElement(".text-input");
        page.findElementByCss(".el-tooltip > .el-button");
        page.findElementByTag("body");
        communication.sendMessage(".text-input","怎么了");
        communication.focusOnElement(".el-tooltip span");
        communication.focusOnElement("img:nth-child(2)");
        communication.focusOnElement(".focusing span");
        assertThat(driver.findElement(By.cssSelector(".message-wrapper:nth-child(5) .content-wrapper span")).getText(), is("我不能接受"));
        communication.focusOnElement(".message-wrapper:nth-child(5) .content-wrapper span");
        communication.focusOnElement(".text-input");
        communication.focusOnElement(".focusing span");
        assertThat(driver.findElement(By.cssSelector(".message-wrapper:nth-child(7) .content-wrapper span")).getText(), is("?"));
        communication.focusOnElement(".message-wrapper:nth-child(7) .content-wrapper span");
        size = communication.getElementSize(".image-preview");
        assert(size > 0);
        communication.focusOnElement(".image-preview");
        page.findElementByCss(".el-button--default:nth-child(2) > span");
        page.findElementByTag("body");
        communication.focusOnElement(".el-table__row:nth-child(2) .el-button:nth-child(1) > span");
    }

    @Test
    public void textInputTest4(){
        page.openUrl();
        page.login("zixunshi1","123456");
        int size = communication.getElementSize(".name > span:nth-child(2)");
        assert(size > 0);
        page.enterSession();
        assertThat(driver.findElement(By.cssSelector(".message-content > span")).getText(), is("哈哈"));
        communication.focusOnElement(".message-content > span");
        boolean isEditable = communication.isEditable(".text-input");
        assertTrue(isEditable);
        communication.focusOnElement(".text-input");
        size = communication.getElementSize(".message-send > span");
        assert(size > 0);
        communication.focusOnElement(".message-send > span");
        size = communication.getElementSize(".el-button--mini:nth-child(2) > span");
        assert(size > 0);
        communication.focusOnElement(".el-button--mini:nth-child(2) > span");
        page.findElementByCss(".el-tooltip > .el-button");
        page.findElementByTag("body");
        js.executeScript("window.scrollTo(0,0)");
        communication.focusOnElement(".focusing .iconfont");
        assertThat(driver.findElement(By.cssSelector(".message-wrapper:nth-child(7) .sound-element-wrapper")).getText(), is("能解决吗"));
        communication.focusOnElement(".message-wrapper:nth-child(7) .sound-element-wrapper");
        communication.focusOnElement(".focusing span");
        assertThat(driver.findElement(By.cssSelector(".message-wrapper:nth-child(10) .content-wrapper span")).getText(), is("？？"));
        communication.focusOnElement(".message-wrapper:nth-child(10) .content-wrapper span");
        communication.focusOnElement(".focusing img");
        assertThat(driver.findElement(By.cssSelector(".message-wrapper:nth-child(11) .content-wrapper span")).getText(), is("哼"));
        communication.focusOnElement(".message-wrapper:nth-child(11) .content-wrapper span");
        communication.focusOnElement(".el-button--default:nth-child(2) > span");
        page.findElementByCss(".el-button--default:nth-child(2)");
        page.findElementByTag("body");
    }

    @Test
    public void textInputTest5(){
        page.openUrl();
        page.login("zixunshi1","123456");
        page.findElementByCss(".el-button");
        page.findElementByCss(".el-button");
        page.enterSession();
        communication.focusOnElement(".text-input");
        int size = communication.getElementSize(".btns > div:nth-child(1)");
        assert(size > 0);
        communication.focusOnElement(".btns > div:nth-child(1)");
        assertThat(driver.findElement(By.cssSelector(".footer:nth-child(3) > #message-send-box-wrapper .text-input")).getText(), is("不要怕"));
        communication.focusOnElement(".footer:nth-child(3) > #message-send-box-wrapper .text-input");
        assertThat(driver.findElement(By.cssSelector(".footer:nth-child(7) > #message-send-box-wrapper .text-input")).getText(), is("好吧"));
        communication.focusOnElement(".footer:nth-child(7) > #message-send-box-wrapper .text-input");
        page.findElementByCss(".footer:nth-child(3) > #message-send-box-wrapper > .bottom .el-button");
        page.findElementByTag("body");
        size = communication.getElementSize(".btns > div:nth-child(2)");
        assert(size > 0);
        communication.focusOnElement(".btns > div:nth-child(2)");
        communication.focusOnElement(".el-button--default:nth-child(2) > span");
    }
}
