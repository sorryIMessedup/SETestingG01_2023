import org.example.Setting;
import org.example.Pages.Login;
import org.example.Pages.Vistor;
import org.junit.Test;

import org.junit.runner.RunWith;
import org.junit.runners.Parameterized;
import org.openqa.selenium.By;

import java.util.Arrays;
import java.util.Collection;

import static org.junit.Assert.*;


@RunWith(Parameterized.class)
public class SearchForVistorTest extends BasicTest{
    @Parameterized.Parameters
    public static Collection<Object[]> data() {
        return Arrays.asList(TestCases.SearchForVistorTestCases);
    }

    @Parameterized.Parameter
    public String input_username;

    @Parameterized.Parameter(1)
    public String expected_uername;

    @Parameterized.Parameter(2)
    public boolean checkBan;

    Vistor vistor;

    /**
     * 测试搜索访问者的功能
     * */
    @Test
    public void searchForVistor() throws InterruptedException {
        new Login().login();
        vistor = new Vistor();
        vistor.moveTo();
        Thread.sleep(Setting.timeout);
        String result = vistor.searchFor(input_username);
        if(!result.equals("") && checkBan){
            vistor.ban();
            Thread.sleep(Setting.timeout);
            assertEquals("已禁用",driver.findElement(By.cssSelector(".el-table_2_column_16 span")).getText());
            vistor.ban();
            Thread.sleep(Setting.timeout);
            assertEquals("正常",driver.findElement(By.cssSelector(".el-table_2_column_16 span")).getText());
        }
        assertEquals(expected_uername, result);
    }
}
