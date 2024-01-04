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

public class emojiInput {
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
    public void emojiInputTest(){
        page.openUrl();
        page.login("zixunshi1","123456");
        page.findElementByCss(".el-button");
        page.findElementByCss(".el-button");
        page.goIntoConsult();
        assertThat(driver.findElement(By.cssSelector(".message-wrapper:nth-child(2) .content-wrapper span")).getText(), is("[呲牙]"));
        int size = communication.getElementSize(".icon-xiaolian");
        assert(size > 0);
        communication.focusOnElement(".icon-xiaolian");
        size = communication.getElementSize(".emoji:nth-child(25) > img");
        assert(size > 0);
        communication.focusOnElement(".emoji:nth-child(25) > img");
        page.findElementByCss(".el-tooltip > .el-button");
        page.findElementByTag("body");
        communication.focusOnElement(".el-tooltip span");
        communication.focusOnElement(".icon-xiaolian");
        size = communication.getElementSize(".emoji:nth-child(21) > img");
        assert(size > 0);
        communication.focusOnElement(".emoji:nth-child(21) > img");
        size = communication.getElementSize(".emoji:nth-child(65) > img");
        assert(size > 0);
        communication.focusOnElement(".emoji:nth-child(65) > img");
        communication.focusOnElement(".text-input");
        assertThat(driver.findElement(By.cssSelector(".message-wrapper:nth-child(5) .content-wrapper span")).getText(), is("[流泪][大哭]可以的"));
        communication.focusOnElement(".el-tooltip span");
        communication.focusOnElement(".icon-xiaolian");
        size = communication.getElementSize(".emoji:nth-child(100) > img");
        assert(size > 0);
        communication.focusOnElement(".emoji:nth-child(100) > img");
        size = communication.getElementSize(".emoji:nth-child(114) > img");
        assert(size > 0);
        communication.focusOnElement(".emoji:nth-child(114) > img");
        communication.focusOnElement(".text-input");
        communication.sendMessage(".text-input","[街舞][彩带]好的");
        communication.focusOnElement(".el-tooltip span");
        page.findElementByCss(".el-tooltip span");
        js.executeScript("window.scrollTo(0,0)");
        page.findElementByTag("body");
        assertThat(driver.findElement(By.cssSelector(".message-wrapper:nth-child(7) .content-wrapper span")).getText(), is("[强][弱][骷髅]"));
        communication.focusOnElement(".btns > div:nth-child(1)");
        communication.focusOnElement(".btns > div:nth-child(2)");
        communication.focusOnElement(".el-table__row:nth-child(2) .el-button:nth-child(1) > span");
        communication.focusOnElement(".focusing img");
        communication.focusOnElement(".message-content > span:nth-child(1)");
        communication.focusOnElement(".focusing img:nth-child(2)");
    }

    @Test
    public void emojiInputTest2(){
        page.openUrl();
        page.login("zixunshi1","123456");
        page.findElementByCss(".el-button");
        int size = communication.getElementSize(".textOverFlow");
        assert(size > 0);
        page.goIntoConsult();
        boolean isEditable = communication.isEditable(".text-input");
        assertTrue(isEditable);
        communication.focusOnElement(".text-input");
        page.findElementByCss(".el-tooltip > .el-button");
        page.findElementByTag("body");
        communication.focusOnElement(".el-tooltip span");
        assertThat(driver.findElement(By.cssSelector(".message-content > img:nth-child(1)")).getText(), is("[流泪]"));
        communication.focusOnElement(".message-content > img:nth-child(1)");
        assertThat(driver.findElement(By.cssSelector("img:nth-child(2)")).getText(), is("[大哭]"));
        communication.focusOnElement("img:nth-child(2)");
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
        size = communication.getElementSize(".image-element");
        assert(size > 0);
        communication.focusOnElement(".image-element");
        size = communication.getElementSize(".close-button");
        assert(size > 0);
        communication.focusOnElement(".close-button");
        communication.focusOnElement(".btns > div:nth-child(1)");
        communication.focusOnElement(".btns > div:nth-child(2)");
        communication.focusOnElement(".el-table__row:nth-child(2) .el-button:nth-child(1) > span");
    }

    @Test
    public void emojiInputTest3(){
        page.openUrl();
        page.login("zixunshi1","123456");
        page.findElementByCss(".el-button");
        int size = communication.getElementSize(".textOverFlow");
        assert(size > 0);
        page.goIntoConsult();
        boolean isEditable = communication.isEditable(".text-input");
        assertTrue(isEditable);
        communication.focusOnElement(".text-input");
        size = communication.getElementSize(".emoji:nth-child(109) > img");
        assert(size > 0);
        communication.focusOnElement(".emoji:nth-child(109) > img");
        size = communication.getElementSize(".el-icon-right");
        assert(size > 0);
        communication.focusOnElement(".el-icon-right");
        communication.focusOnElement(".image-preview");
        size = communication.getElementSize(".btns > div:nth-child(1)");
        assert(size > 0);
        communication.focusOnElement(".btns > div:nth-child(1)");
        size = communication.getElementSize(".el-button--default:nth-child(2) > span");
        assert(size > 0);
        communication.focusOnElement(".el-button--default:nth-child(2) > span");
        communication.focusOnElement(".focusing img");
        communication.focusOnElement(".focusing img:nth-child(2)");
    }

    @Test
    public void emojiInputTest4(){
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
        communication.focusOnElement(".sound-element-wrapper");
        size = communication.getElementSize(".el-button--mini:nth-child(2) > span");
        assert(size > 0);
        communication.focusOnElement(".el-button--mini:nth-child(2) > span");
        page.findElementByCss(".el-tooltip > .el-button");
        page.findElementByTag("body");
        communication.focusOnElement(".focusing .iconfont");
        communication.focusOnElement(".text-input");
        js.executeScript("window.scrollTo(0,0)");
        communication.focusOnElement(".focusing span");
        assertThat(driver.findElement(By.cssSelector(".message-wrapper:nth-child(11) .col-2 img")).getText(), is("[敲打]"));
        communication.focusOnElement(".message-wrapper:nth-child(11) .col-2 img");
        communication.focusOnElement(".tim-icon-close");
        communication.focusOnElement(".el-button--default:nth-child(2) > span");
        page.findElementByCss(".el-button--default:nth-child(2)");
        page.findElementByTag("body");
    }

    @Test
    public void emojiInputTest5(){
        page.openUrl();
        page.login("zixunshi1","123456");
        page.findElementByCss(".el-button");
        page.findElementByCss(".el-button");
        int size = communication.getElementSize(".name > span:nth-child(2)");
        assert(size > 0);
        page.goIntoConsult();
        communication.focusOnElement(".text-input");
        communication.focusOnElement(".noActive");
        assertThat(driver.findElement(By.cssSelector("#el-popover-3547 .emoji:nth-child(81) > img")).getText(), is("[ok]"));
        communication.focusOnElement("#el-popover-3547 .emoji:nth-child(81) > img");
        assertThat(driver.findElement(By.cssSelector("#el-popover-3547 .emoji:nth-child(88) > img")).getText(), is("[猪头]"));
        communication.focusOnElement("#el-popover-3547 .emoji:nth-child(88) > img");
        size = communication.getElementSize(".el-button--default:nth-child(2) > span");
        assert(size > 0);
        communication.focusOnElement(".el-button--default:nth-child(2) > span");
        communication.focusOnElement(".focusing span");
        communication.focusOnElement(".btns > div:nth-child(2)");
        communication.focusOnElement(".message-content > span:nth-child(1)");
        communication.focusOnElement(".focusing img:nth-child(2)");
    }
}
