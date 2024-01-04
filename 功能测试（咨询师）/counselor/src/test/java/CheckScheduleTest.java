import org.example.Setting;
import org.example.Pages.Login;
import org.example.Pages.Schedule;
import org.junit.Test;

import org.junit.runner.RunWith;
import org.junit.runners.Parameterized;

import java.util.Arrays;
import java.util.Collection;


@RunWith(Parameterized.class)
public class CheckScheduleTest extends BasicTest{
    @Parameterized.Parameters
    public static Collection<Object[]> data() {
        return Arrays.asList(TestCases.CheckScheduleTestCases);
    }

    @Parameterized.Parameter
    public int[] days;

    Schedule schedule;
    @Test
    public void CheckSchedule() throws InterruptedException {
        new Login().login();
        schedule = new Schedule();
        schedule.moveTo();
        Thread.sleep(Setting.timeout);
        schedule.checkDate(days);
    }
}
