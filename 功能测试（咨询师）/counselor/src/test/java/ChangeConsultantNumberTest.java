import org.example.Pages.Home;
import org.example.Pages.Login;
import org.junit.Test;

import org.junit.runner.RunWith;
import org.junit.runners.Parameterized;
import org.openqa.selenium.By;

import java.util.Arrays;
import java.util.Collection;
import static org.junit.Assert.*;


@RunWith(Parameterized.class)
public class ChangeConsultantNumberTest extends BasicTest{
    @Parameterized.Parameters
    public static Collection<Object[]> data() {
        return Arrays.asList(TestCases.ChangeConsultantNumberTestCases);
    }

    @Parameterized.Parameter
    public String input_set_number;

    @Parameterized.Parameter(1)
    public int input_add_number;

    @Parameterized.Parameter(2)
    public int input_sub_number;

    @Parameterized.Parameter(3)
    public int expected_num;

    Home home = new Home();
    @Test
    public void changeConsultantNumber() throws InterruptedException {
        new Login().login();

        home.setConsultantNumber(input_set_number+"", input_add_number, input_sub_number);
        assertEquals("咨询设置","咨询上限："+expected_num,
                driver.findElement(By.cssSelector(".consultCount")).getText());
    }
}
