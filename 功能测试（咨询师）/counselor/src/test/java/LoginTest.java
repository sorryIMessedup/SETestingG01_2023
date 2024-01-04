import org.example.Pages.Login;
import org.junit.Test;

import org.junit.runner.RunWith;
import org.junit.runners.Parameterized;

import java.util.Arrays;
import java.util.Collection;
import static org.junit.Assert.*;


@RunWith(Parameterized.class)
public class LoginTest extends BasicTest{
    @Parameterized.Parameters
    public static Collection<Object[]> data() {
        return Arrays.asList(TestCases.LoginTestCases);
    }

    @Parameterized.Parameter
    public String input_username;

    @Parameterized.Parameter(1)
    public String input_password;

    @Parameterized.Parameter(2)
    public String expected_page_url;

    @Test
    public void login() throws InterruptedException {
        new Login().login(input_username,input_password);
        assertEquals("登录",expected_page_url, driver.getCurrentUrl());
    }
}
