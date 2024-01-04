import org.example.Setting;
import org.example.Pages.Home;
import org.example.Pages.Login;
import org.junit.Test;
import org.junit.runner.RunWith;
import org.junit.runners.Parameterized;

import java.util.Arrays;
import java.util.Collection;

import static org.junit.Assert.assertEquals;

@RunWith(Parameterized.class)
public class ChangePasswordTest extends BasicTest{
    @Parameterized.Parameters
    public static Collection<Object[]> data() {
        return Arrays.asList(TestCases.ChangePasswordTestCases);
    }

    @Parameterized.Parameter
    public String input_old_password;

    @Parameterized.Parameter(1)
    public String input_new_password;

    @Parameterized.Parameter(2)
    public String input_again_new_password;

    @Parameterized.Parameter(3)
    public String expected_page_url;

    Home home = new Home();
    Login login = new Login();
    @Test
    public void changePassword() throws InterruptedException {
        login.login();
        home.verify();
        home.changePassword(input_old_password, input_new_password, input_again_new_password);
        home.logout();
        login.login(Setting.CorrectUserName, input_new_password);
        assertEquals("密码修改",expected_page_url,driver.getCurrentUrl());
        resetPassword(); // 还原密码
    }

    /**
     * 将密码还原
     * */
    private void resetPassword() throws InterruptedException {
        String new_password = input_new_password;
        if(login.isCurrentPage()) {
            return;
        }
        home.verify();
        home.changePassword(new_password, Setting.CorrectPassWord, Setting.CorrectPassWord);
    }
}
