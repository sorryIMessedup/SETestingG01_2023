import static org.example.Setting.*;

public class TestCases {
    public static final Object[][] LoginTestCases = new Object[][]{
            {"test", "aaa111",HomePageUrl},
            {"", "",LoginPageUrl},
            {"test", "12345678",LoginPageUrl},
            {"test", "",LoginPageUrl},
            {"", "aaa111",LoginPageUrl},
            {"123456", "aaa111",LoginPageUrl},
            {"12[}`~$$", "aaa111",LoginPageUrl},
            {"11dadfds", "aaa111",LoginPageUrl},
            {"TEST", "aaa111",HomePageUrl},
            {"test", "AAA111",LoginPageUrl},
    };
    public static final Object[][] ChangePasswordTestCases = new Object[][]{
            {"aaa111", "12345678","12345678",HomePageUrl},
            {"123", "12345678","12345678",LoginPageUrl},
            {"aaa111", "12345678","12345679",LoginPageUrl},
            {"aaa111", "123","123",LoginPageUrl},
            {"", "12345678","12345678",LoginPageUrl},
            {"aaa111", "","12345678",LoginPageUrl},
            {"aaa111", "12345678","",LoginPageUrl},
            {"aaa111", "||~··||","",LoginPageUrl},
            {"aaa111", "","||~··||",LoginPageUrl},
            {"aaa111", "||~··||","||~··||",LoginPageUrl},
            {"aaa111", "","",LoginPageUrl}
    };
    public static final Object[][] ChangeConsultantNumberTestCases = new Object[][]{
            {"5",0,0,5},
            {"2",3,2,3},
            {"0",0,0,1},
            {"0",0,1,1},
            {"5",1,1,5},
            {"-1",1,0,2},
            {Integer.MIN_VALUE+"",0,0,1},
            {Integer.MIN_VALUE+"",0,1,1},
            {Integer.MAX_VALUE+"",0,0,5},
            {Integer.MAX_VALUE+"",0,1,5},
            {"fdfefedfd",0,0,1},
            {"fdfefedfd",1,0,1}
    };
    public static final Object[][] CheckScheduleTestCases = new Object[][]{
            {new int[]{1,2,3,4,5,6,7}},
            {new int[]{8,9,10,11,12,13,14}},
            {new int[]{15,16,17,18,19,20,21}},
            {new int[]{22,23,24,25,26,27,28}},
            {new int[]{29,30,31,32,33,34,35}}
    };

    public static final Object[][] SearchForVistorTestCases = new Object[][]{
            {"李","李易达",true},
            {"李易","李易达",false},
            {"李易达","李易达",true},
            {"dfdf","",false},
    };
    public static final Object[][] SearchForRecordTestCases = new Object[][]{
            {"李易达","2000-01-01","00:00:00","2050-01-01","00:00:00"},
    };
}
