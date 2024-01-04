import org.example.Setting;
import org.example.Pages.Login;
import org.example.Pages.Record;
import org.junit.Test;

import org.junit.runner.RunWith;
import org.junit.runners.Parameterized;

import java.util.Arrays;
import java.util.Collection;
import static org.junit.Assert.*;


@RunWith(Parameterized.class)
public class SearchForRecordTest extends BasicTest{

    @Parameterized.Parameters
    public static Collection<Object[]> data() {
        return Arrays.asList(TestCases.SearchForRecordTestCases);
    }

    @Parameterized.Parameter
    public String name;

    @Parameterized.Parameter(1)
    public String from;

    @Parameterized.Parameter(2)
    public String ftime;

    @Parameterized.Parameter(3)
    public String to;

    @Parameterized.Parameter(4)
    public String ttime;

    Record record;
    @Test
    public void searchForRecord() throws InterruptedException {
        new Login().login();
        record = new Record();
        record.moveTo();
        Thread.sleep(Setting.timeout);
        record.searchForRecords(name, from, ftime, to, ttime);
        assertEquals(name, record.checkFirstRecordName());
    }
}
