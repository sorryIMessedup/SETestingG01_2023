import time
import unittest

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class MyTestCase(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome("D:\\chromedriver-win64\\chromedriver.exe")
        cls.driver.implicitly_wait(20)
        print('打开测试网站')
        cls.driver.get("https://sei-test.021hqit.com/group-1/#/login")

    def test_00_Login(self):
        driver = self.driver
        print('测试登录')
        driver.find_element(By.CSS_SELECTOR,  # 输入框要提前清理里面的数据
                            "#app > div > div.login > form > div:nth-child(1) > div > div > input").clear()
        driver.find_element(By.CSS_SELECTOR,  # 输入用户名
                            "#app > div > div.login > form > div:nth-child(1) > div > div > input").send_keys("john")
        driver.find_element(By.CSS_SELECTOR,  # 输入框要提前清理里面的数据
                            "#app > div > div.login > form > div:nth-child(2) > div > div > input").clear()
        driver.find_element(By.CSS_SELECTOR,  # 输入密码
                            "#app > div > div.login > form > div:nth-child(2) > div > div > input").send_keys("123456")
        login_btn_ele = driver.find_element(By.CSS_SELECTOR,  # 拿到登录按钮
                                            "#app > div > div.login > div > button")
        login_btn_ele.click()  # 按下登陆按钮
        print("已按下登陆按钮")
        time.sleep(2)

    def test_01_查询咨询对话测试01(self):
        # 按名称搜索
        driver = self.driver
        print('查询咨询对话01')
        x = '//*[@id="app"]/div/div[1]/div/ul/li[2]/span'
        check_consult_talk = driver.find_element_by_xpath(x)
        ActionChains(driver).click(check_consult_talk).perform()
        time.sleep(5)
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.consultRecord > div > "
                            "div.el-row.is-align-bottom.el-row--flex > div:nth-child(1) > div > input").clear()
        driver.find_element(By.CSS_SELECTOR,  # 搜索咨询者'谭诚'
                            "#app > div > div.content > div.consultRecord > div > "
                            "div.el-row.is-align-bottom.el-row--flex > div:nth-child(1) > div > input").send_keys(
            "谭诚")
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.consultRecord > div > "
                            "div.el-row.is-align-bottom.el-row--flex > div:nth-child(1) > div > input").send_keys(
            Keys.ENTER)
        time.sleep(5)

    def test_02_查询咨询对话测试02(self):
        # 按名称搜索
        driver = self.driver
        print('查询咨询对话02')
        x = '//*[@id="app"]/div/div[1]/div/ul/li[1]/span'
        driver.find_element_by_xpath(x).click()
        time.sleep(2)
        x = '//*[@id="app"]/div/div[1]/div/ul/li[2]/span'
        driver.find_element_by_xpath(x).click()
        time.sleep(2)
        # 搜索咨询者'高祖阳'
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.consultRecord > div > "
                            "div.el-row.is-align-bottom.el-row--flex >"
                            "div:nth-child(1) > div > input").clear()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.consultRecord > div > "
                            "div.el-row.is-align-bottom.el-row--flex >"
                            "div:nth-child(1) > div > input").send_keys(
            "李易达")
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.consultRecord > div > "
                            "div.el-row.is-align-bottom.el-row--flex >"
                            "div:nth-child(1) > div > input").send_keys(
            Keys.ENTER)
        time.sleep(5)

    def test_03_查询咨询对话测试03(self):
        # 按名称搜索
        driver = self.driver
        print('查询咨询对话03')
        x = '//*[@id="app"]/div/div[1]/div/ul/li[1]/span'
        driver.find_element_by_xpath(x).click()
        time.sleep(2)
        x = '//*[@id="app"]/div/div[1]/div/ul/li[2]/span'
        driver.find_element_by_xpath(x).click()
        time.sleep(2)
        # 搜索咨询者不存在
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.consultRecord > div > div.el-row.is-align-bottom.el-row--flex > div:nth-child(1) > div > input").clear()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.consultRecord > div > div.el-row.is-align-bottom.el-row--flex > div:nth-child(1) > div > input").send_keys(
            "yoyyi")
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.consultRecord > div > div.el-row.is-align-bottom.el-row--flex > div:nth-child(1) > div > input").send_keys(
            Keys.ENTER)
        time.sleep(2)
        x = '//*[@id="app"]/div/div[2]/div[2]/div/div[2]/div[3]/div/span'
        txt = driver.find_element_by_xpath(x).text
        print(txt)
        time.sleep(5)

    def test_04_查询咨询对话测试04(self):
        # 按名称搜索
        driver = self.driver
        print('查询咨询对话04')
        # 搜索咨询者不存在
        x = '//*[@id="app"]/div/div[1]/div/ul/li[1]/span'
        driver.find_element_by_xpath(x).click()
        time.sleep(2)
        x = '//*[@id="app"]/div/div[1]/div/ul/li[2]/span'
        driver.find_element_by_xpath(x).click()
        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.consultRecord > div > div.el-row.is-align-bottom.el-row--flex > div:nth-child(1) > div > input").clear()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.consultRecord > div > div.el-row.is-align-bottom.el-row--flex > div:nth-child(1) > div > input").send_keys(
            "莫小贝")
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.consultRecord > div > div.el-row.is-align-bottom.el-row--flex > div:nth-child(1) > div > input").send_keys(
            Keys.ENTER)
        time.sleep(2)
        x = '//*[@id="app"]/div/div[2]/div[2]/div/div[2]/div[3]/div/span'
        txt = driver.find_element_by_xpath(x).text
        print(txt)
        time.sleep(5)

    def test_05_查询咨询对话测试05_1(self):
        # 切换单页记录数
        driver = self.driver
        print('查询咨询对话测试05_1')
        x = '//*[@id="app"]/div/div[1]/div/ul/li[1]/span'
        driver.find_element_by_xpath(x).click()
        time.sleep(2)
        x = '//*[@id="app"]/div/div[1]/div/ul/li[2]/span'
        driver.find_element_by_xpath(x).click()
        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.consultRecord > div > div.el-row.is-align-bottom.el-row--flex > div:nth-child(1) > div > input").clear()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.consultRecord > div > div.el-row.is-align-bottom.el-row--flex > div:nth-child(1) > div > input").send_keys(
            Keys.ENTER)
        time.sleep(5)

        x = '//*[@id="app"]/div/div[2]/div[2]/div/div[3]/div[2]/slot/div/div/div/input'
        driver.find_element_by_xpath(x).click()
        time.sleep(2)
        # 选择一页20条记录
        driver.find_element_by_xpath("//ul[@class='el-scrollbar__view el-select-dropdown__list']/li[2]").click()
        time.sleep(2)

    def test_06_查询咨询对话测试05_2(self):
        # 切换单页记录数
        driver = self.driver
        print('查询咨询对话测试05_2')
        x = '//*[@id="app"]/div/div[1]/div/ul/li[1]/span'
        driver.find_element_by_xpath(x).click()
        time.sleep(2)
        x = '//*[@id="app"]/div/div[1]/div/ul/li[2]/span'
        driver.find_element_by_xpath(x).click()
        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.consultRecord > div > div.el-row.is-align-bottom.el-row--flex > div:nth-child(1) > div > input").clear()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.consultRecord > div > div.el-row.is-align-bottom.el-row--flex > div:nth-child(1) > div > input").send_keys(
            Keys.ENTER)
        time.sleep(2)

        x = '//*[@id="app"]/div/div[2]/div[2]/div/div[3]/div[2]/slot/div/div/div/input'
        driver.find_element_by_xpath(x).click()
        time.sleep(2)
        # 选择一页30条记录
        driver.find_element_by_xpath("//ul[@class='el-scrollbar__view el-select-dropdown__list']/li[3]").click()
        time.sleep(2)

    def test_07_查询咨询对话测试05_3(self):
        # 切换单页记录数
        driver = self.driver
        print('查询咨询对话测试05_3')
        x = '//*[@id="app"]/div/div[1]/div/ul/li[1]/span'
        driver.find_element_by_xpath(x).click()
        time.sleep(2)
        x = '//*[@id="app"]/div/div[1]/div/ul/li[2]/span'
        driver.find_element_by_xpath(x).click()
        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.consultRecord > div > div.el-row.is-align-bottom.el-row--flex > div:nth-child(1) > div > input").clear()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.consultRecord > div > div.el-row.is-align-bottom.el-row--flex > div:nth-child(1) > div > input").send_keys(
            Keys.ENTER)
        time.sleep(5)

        x = '//*[@id="app"]/div/div[2]/div[2]/div/div[3]/div[2]/slot/div/div/div/input'
        driver.find_element_by_xpath(x).click()
        time.sleep(2)
        # 选择一页40条记录
        driver.find_element_by_xpath("//ul[@class='el-scrollbar__view el-select-dropdown__list']/li[4]").click()
        time.sleep(2)

    def test_08_查询咨询对话测试06_1(self):
        # 切换单页记录数
        driver = self.driver
        print('查询咨询对话测试06_1')
        x = '//*[@id="app"]/div/div[1]/div/ul/li[1]/span'
        driver.find_element_by_xpath(x).click()
        time.sleep(2)
        x = '//*[@id="app"]/div/div[1]/div/ul/li[2]/span'
        driver.find_element_by_xpath(x).click()
        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.consultRecord > div > div.el-row.is-align-bottom.el-row--flex > div:nth-child(1) > div > input").clear()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.consultRecord > div > div.el-row.is-align-bottom.el-row--flex > div:nth-child(1) > div > input").send_keys(
            Keys.ENTER)
        time.sleep(2)

        x = '//*[@id="app"]/div/div[2]/div[2]/div/div[3]/div[2]/slot/div/div/div/input'
        driver.find_element_by_xpath(x).click()
        time.sleep(2)
        # 选择一页50条记录
        driver.find_element_by_xpath("//ul[@class='el-scrollbar__view el-select-dropdown__list']/li[5]").click()
        time.sleep(5)

    def test_09_查询咨询对话测试06_2(self):
        # 切换单页记录数
        driver = self.driver
        print('查询咨询对话06_2')
        x = '//*[@id="app"]/div/div[1]/div/ul/li[1]/span'
        driver.find_element_by_xpath(x).click()
        time.sleep(2)
        x = '//*[@id="app"]/div/div[1]/div/ul/li[2]/span'
        driver.find_element_by_xpath(x).click()
        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.consultRecord > div > div.el-row.is-align-bottom.el-row--flex > div:nth-child(1) > div > input").clear()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.consultRecord > div > div.el-row.is-align-bottom.el-row--flex > div:nth-child(1) > div > input").send_keys(
            Keys.ENTER)
        time.sleep(2)

        x = '//*[@id="app"]/div/div[2]/div[2]/div/div[3]/div[2]/slot/div/div/div/input'
        driver.find_element_by_xpath(x).click()
        time.sleep(2)
        # 选择一页60条记录
        driver.find_element_by_xpath("//ul[@class='el-scrollbar__view el-select-dropdown__list']/li[6]").click()
        time.sleep(2)

    def test_10_查询咨询对话测试07(self):
        driver = self.driver
        print('查询咨询对话07')
        x = '//*[@id="app"]/div/div[1]/div/ul/li[1]/span'
        driver.find_element_by_xpath(x).click()
        time.sleep(2)
        x = '//*[@id="app"]/div/div[1]/div/ul/li[2]/span'
        driver.find_element_by_xpath(x).click()
        time.sleep(2)
        # 搜索咨询者'熊怡玮'
        # 搜索存在的记录
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.consultRecord > div > div.el-row.is-align-bottom.el-row--flex > div:nth-child(1) > div > input").clear()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.consultRecord > div > div.el-row.is-align-bottom.el-row--flex > div:nth-child(1) > div > input").send_keys(
            "熊怡玮")

        time.sleep(3)
        # 定位“12月1号”
        x = '//*[@id="app"]/div/div[2]/div[2]/div/div[1]/div[2]/div/input[1]'
        driver.find_element_by_xpath(x).click()
        time.sleep(5)
        begin = '/html/body/div[last()]/div[1]/div/div[2]/table/tbody/tr[2]/td[4]/div/span'
        driver.find_element_by_xpath(begin).click()
        time.sleep(2)
        # 定位“1月31日”
        end = '/html/body/div[last()]/div[1]/div/div[3]/table/tbody/tr[7]/td[2]/div/span'
        driver.find_element_by_xpath(end).click()
        time.sleep(2)
        certain = '/html/body/div[last()]/div[2]/button[2]/span'
        driver.find_element_by_xpath(certain).click()
        time.sleep(2)

    def test_11_查询咨询对话测试08(self):
        driver = self.driver
        print('查询咨询对话08')
        x = '//*[@id="app"]/div/div[1]/div/ul/li[1]/span'
        driver.find_element_by_xpath(x).click()
        time.sleep(2)
        x = '//*[@id="app"]/div/div[1]/div/ul/li[2]/span'
        driver.find_element_by_xpath(x).click()
        time.sleep(2)
        # 搜索咨询者'高祖阳'
        # 查看存在的记录
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.consultRecord > div > div.el-row.is-align-bottom.el-row--flex > div:nth-child(1) > div > input").clear()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.consultRecord > div > div.el-row.is-align-bottom.el-row--flex > div:nth-child(1) > div > input").send_keys(
            "高祖阳")

        time.sleep(3)
        # 搜索范围从今年12月底到明年1月底
        # 定位“12月1号”
        x = '//*[@id="app"]/div/div[2]/div[2]/div/div[1]/div[2]/div/input[1]'
        driver.find_element_by_xpath(x).click()
        time.sleep(5)
        begin = '/html/body/div[last()]/div[1]/div/div[2]/table/tbody/tr[2]/td[4]/div/span'
        driver.find_element_by_xpath(begin).click()
        time.sleep(2)
        # 定位“1月31日”
        end = '/html/body/div[last()]/div[1]/div/div[3]/table/tbody/tr[7]/td[2]/div/span'
        driver.find_element_by_xpath(end).click()
        time.sleep(2)
        certain = '/html/body/div[last()]/div[2]/button[2]/span'
        driver.find_element_by_xpath(certain).click()
        time.sleep(2)

    def test_12_查询咨询对话测试09(self):
        driver = self.driver
        print('查询咨询对话09')
        # 具体选择咨询者'熊怡玮'
        # 查询不存在的记录
        # 定位“12月31号”
        x = '//*[@id="app"]/div/div[1]/div/ul/li[1]/span'
        driver.find_element_by_xpath(x).click()
        time.sleep(2)
        x = '//*[@id="app"]/div/div[1]/div/ul/li[2]/span'
        driver.find_element_by_xpath(x).click()
        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.consultRecord > div > div.el-row.is-align-bottom.el-row--flex > div:nth-child(1) > div > input").clear()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.consultRecord > div > div.el-row.is-align-bottom.el-row--flex > div:nth-child(1) > div > input").send_keys(
            "熊怡玮")

        time.sleep(3)
        x = '//*[@id="app"]/div/div[2]/div[2]/div/div[1]/div[2]/div/input[1]'
        driver.find_element_by_xpath(x).click()
        time.sleep(5)
        begin = '/html/body/div[last()]/div[1]/div/div[2]/table/tbody/tr[6]/td[6]/div/span'
        driver.find_element_by_xpath(begin).click()
        time.sleep(2)
        # 定位“1月31日”
        end = '/html/body/div[last()]/div[1]/div/div[3]/table/tbody/tr[7]/td[2]/div/span'
        driver.find_element_by_xpath(end).click()
        time.sleep(2)
        certain = '/html/body/div[last()]/div[2]/button[2]/span'
        driver.find_element_by_xpath(certain).click()
        time.sleep(5)
        x = '//*[@id="app"]/div/div[2]/div[2]/div/div[2]/div[3]/div/span'
        txt = driver.find_element_by_xpath(x).text
        print(txt)
        time.sleep(2)

    def test_13_查询咨询对话测试10(self):
        driver = self.driver
        print('查询咨询对话10')
        # 具体选择咨询者'高祖阳'
        # 查询不存在的记录
        # 定位“12月31号”
        x = '//*[@id="app"]/div/div[1]/div/ul/li[1]/span'
        driver.find_element_by_xpath(x).click()
        time.sleep(2)
        x = '//*[@id="app"]/div/div[1]/div/ul/li[2]/span'
        driver.find_element_by_xpath(x).click()
        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.consultRecord > div > div.el-row.is-align-bottom.el-row--flex > "
                            "div:nth-child(1) > div > input").clear()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.consultRecord > div > div.el-row.is-align-bottom.el-row--flex > div:nth-child(1) > div > input").send_keys(
            "高祖阳")

        time.sleep(3)
        x = '//*[@id="app"]/div/div[2]/div[2]/div/div[1]/div[2]/div/input[1]'
        driver.find_element_by_xpath(x).click()
        time.sleep(5)
        begin = '/html/body/div[last()]/div[1]/div/div[2]/table/tbody/tr[6]/td[6]/div/span'
        driver.find_element_by_xpath(begin).click()
        time.sleep(2)
        # 定位“1月31日”
        end = '/html/body/div[last()]/div[1]/div/div[3]/table/tbody/tr[7]/td[2]/div/span'
        driver.find_element_by_xpath(end).click()
        time.sleep(2)
        certain = '/html/body/div[last()]/div[2]/button[2]/span'
        driver.find_element_by_xpath(certain).click()
        time.sleep(5)
        x = '//*[@id="app"]/div/div[2]/div[2]/div/div[2]/div[3]/div/span'
        txt = driver.find_element_by_xpath(x).text
        print(txt)
        time.sleep(2)

    def test_14_查询咨询对话测试11(self):
        driver = self.driver
        print('查询咨询对话11')
        # 不具体选择咨询者
        # 查询部分记录
        # 定位“12月16号”
        x = '//*[@id="app"]/div/div[1]/div/ul/li[1]/span'
        driver.find_element_by_xpath(x).click()
        time.sleep(2)
        x = '//*[@id="app"]/div/div[1]/div/ul/li[2]/span'
        driver.find_element_by_xpath(x).click()
        time.sleep(2)

        x = '//*[@id="app"]/div/div[2]/div[2]/div/div[1]/div[2]/div/input[1]'
        driver.find_element_by_xpath(x).click()
        time.sleep(5)
        begin = '/html/body/div[last()]/div[1]/div/div[2]/table/tbody/tr[4]/td[5]/div/span'
        driver.find_element_by_xpath(begin).click()
        time.sleep(2)
        # 定位“1月31日”
        end = '/html/body/div[last()]/div[1]/div/div[3]/table/tbody/tr[7]/td[2]/div/span'
        driver.find_element_by_xpath(end).click()
        time.sleep(2)
        certain = '/html/body/div[last()]/div[2]/button[2]/span'
        driver.find_element_by_xpath(certain).click()
        time.sleep(5)

    def test_15_查询咨询对话测试12(self):
        driver = self.driver
        print('查询咨询对话12')
        # 测试灰色日期的功能

        x = '//*[@id="app"]/div/div[1]/div/ul/li[1]/span'
        driver.find_element_by_xpath(x).click()
        time.sleep(2)
        x = '//*[@id="app"]/div/div[1]/div/ul/li[2]/span'
        driver.find_element_by_xpath(x).click()
        time.sleep(2)

        x = '//*[@id="app"]/div/div[2]/div[2]/div/div[1]/div[2]/div/input[1]'
        driver.find_element_by_xpath(x).click()
        time.sleep(5)
        # 定位12月1日旁边的12月30日
        begin = '/html/body/div[last()]/div[1]/div/div[2]/table/tbody/tr[2]/td[3]/div/span'
        driver.find_element_by_xpath(begin).click()
        time.sleep(2)
        # 定位“1月31日”
        end = '/html/body/div[last()]/div[1]/div/div[3]/table/tbody/tr[7]/td[2]/div/span'
        driver.find_element_by_xpath(end).click()
        time.sleep(2)
        certain = '/html/body/div[last()]/div[2]/button[2]/span'
        driver.find_element_by_xpath(certain).click()
        time.sleep(5)

    def test_16_查询咨询对话测试13(self):
        driver = self.driver
        print('查询咨询对话13')

        x = '//*[@id="app"]/div/div[1]/div/ul/li[2]/span'
        driver.find_element_by_xpath(x).click()
        time.sleep(2)
        # 测试灰色日期的功能
        # 测试1月最后一行的5日是否跳转
        x = '//*[@id="app"]/div/div[2]/div[2]/div/div[1]/div[2]/div/input[1]'
        driver.find_element_by_xpath(x).click()
        time.sleep(3)
        begin = '/html/body/div[last()]/div[1]/div/div[2]/table/tbody/tr[2]/td[4]/div/span'
        driver.find_element_by_xpath(begin).click()
        time.sleep(5)
        end = '/html/body/div[last()]/div[1]/div/div[3]/table/tbody/tr[7]/td[2]/div/span'
        driver.find_element_by_xpath(end).click()
        time.sleep(5)
        certain = '/html/body/div[last()]/div[2]/button[2]/span'
        driver.find_element_by_xpath(certain).click()
        time.sleep(5)

    def test_17_查询咨询对话测试14(self):
        driver = self.driver
        print('查询咨询对话14')
        # 查询右选月份按钮
        x = '//*[@id="app"]/div/div[1]/div/ul/li[1]/span'
        driver.find_element_by_xpath(x).click()
        time.sleep(2)
        x = '//*[@id="app"]/div/div[1]/div/ul/li[2]/span'
        driver.find_element_by_xpath(x).click()
        time.sleep(2)
        x = '//*[@id="app"]/div/div[2]/div[2]/div/div[1]/div[2]/div/input[1]'
        driver.find_element_by_xpath(x).click()
        time.sleep(5)
        x = '/html/body/div[last()]/div[1]/div/div[2]/div/button[2]'
        driver.find_element_by_xpath(x).click()
        time.sleep(3)
        # 选择11月18日
        begin = '/html/body/div[last()]/div[1]/div/div[2]/table/tbody/tr[4]/td[5]/div/span'
        driver.find_element_by_xpath(begin).click()
        time.sleep(2)
        # 定位“12月15日”
        end = '/html/body/div[last()]/div[1]/div/div[3]/table/tbody/tr[4]/td[4]/div/span'
        driver.find_element_by_xpath(end).click()
        time.sleep(2)
        certain = '/html/body/div[last()]/div[2]/button[2]/span'
        driver.find_element_by_xpath(certain).click()
        time.sleep(5)

    def test_18_查询咨询对话测试15(self):
        driver = self.driver
        print('查询咨询对话15')
        # 查询左选月份按钮
        x = '//*[@id="app"]/div/div[1]/div/ul/li[1]/span'
        driver.find_element_by_xpath(x).click()
        time.sleep(2)
        x = '//*[@id="app"]/div/div[1]/div/ul/li[2]/span'
        driver.find_element_by_xpath(x).click()
        time.sleep(2)

        x = '//*[@id="app"]/div/div[2]/div[2]/div/div[1]/div[2]/div/input[1]'
        driver.find_element_by_xpath(x).click()
        time.sleep(5)
        x = '/html/body/div[last()]/div[1]/div/div[3]/div/button[2]'

        driver.find_element_by_xpath(x).click()
        time.sleep(3)
        # 选择1月13日
        begin = '/html/body/div[last()]/div[1]/div/div[2]/table/tbody/tr[4]/td[5]/div/span'
        driver.find_element_by_xpath(begin).click()
        time.sleep(2)
        # 定位“2月6日”
        end = '/html/body/div[last()]/div[1]/div/div[3]/table/tbody/tr[4]/td[4]/div/span'
        driver.find_element_by_xpath(end).click()
        time.sleep(2)
        certain = '/html/body/div[last()]/div[2]/button[2]/span'
        driver.find_element_by_xpath(certain).click()
        time.sleep(5)

    def test_19_查询咨询对话测试16(self):
        driver = self.driver
        print('查询咨询对话14')
        # 查询跨好几个月选择记录
        x = '//*[@id="app"]/div/div[1]/div/ul/li[1]/span'
        driver.find_element_by_xpath(x).click()
        time.sleep(2)
        x = '//*[@id="app"]/div/div[1]/div/ul/li[2]/span'
        driver.find_element_by_xpath(x).click()
        time.sleep(2)

        x = '//*[@id="app"]/div/div[2]/div[2]/div/div[1]/div[2]/div/input[1]'
        driver.find_element_by_xpath(x).click()
        time.sleep(5)

        x = '/html/body/div[last()]/div[1]/div/div[2]/div/button[2]'
        driver.find_element_by_xpath(x).click()
        time.sleep(3)

        x = '/html/body/div[last()]/div[1]/div/div[2]/div/button[2]'
        driver.find_element_by_xpath(x).click()
        time.sleep(3)

        # 选择10月14日
        x = '/html/body/div[last()]/div[1]/div/div[3]/div/button[2]'
        begin = '/html/body/div[last()]/div[1]/div/div[2]/table/tbody/tr[4]/td[5]/div/span'
        driver.find_element_by_xpath(begin).click()
        time.sleep(2)
        driver.find_element_by_xpath(x).click()
        time.sleep(3)

        # 选择12月15日
        end = '/html/body/div[last()]/div[1]/div/div[3]/table/tbody/tr[4]/td[4]/div/span'
        driver.find_element_by_xpath(end).click()
        time.sleep(2)
        certain = '/html/body/div[last()]/div[2]/button[2]/span'
        driver.find_element_by_xpath(certain).click()
        time.sleep(5)

    def test_20_查询咨询对话测试17(self):
        driver = self.driver
        print('查询咨询对话17')
        # 查询10月27日到明年4月13日
        x = '//*[@id="app"]/div/div[1]/div/ul/li[1]/span'
        driver.find_element_by_xpath(x).click()
        time.sleep(2)
        x = '//*[@id="app"]/div/div[1]/div/ul/li[2]/span'
        driver.find_element_by_xpath(x).click()
        time.sleep(2)

        x = '//*[@id="app"]/div/div[2]/div[2]/div/div[1]/div[2]/div/input[1]'
        driver.find_element_by_xpath(x).click()
        time.sleep(5)

        x = '/html/body/div[last()]/div[1]/div/div[2]/div/button[2]'
        driver.find_element_by_xpath(x).click()
        time.sleep(3)

        x = '/html/body/div[last()]/div[1]/div/div[2]/div/button[2]'
        driver.find_element_by_xpath(x).click()
        time.sleep(3)

        x = '/html/body/div[last()]/div[1]/div/div[3]/div/button[2]'
        begin = '/html/body/div[last()]/div[1]/div/div[2]/table/tbody/tr[6]/td[4]/div/span'
        driver.find_element_by_xpath(begin).click()
        time.sleep(2)
        driver.find_element_by_xpath(x).click()
        time.sleep(3)

        driver.find_element_by_xpath(x).click()
        time.sleep(3)

        driver.find_element_by_xpath(x).click()
        time.sleep(3)

        driver.find_element_by_xpath(x).click()
        time.sleep(3)
        driver.find_element_by_xpath(x).click()
        time.sleep(3)

        end = '/html/body/div[last()]/div[1]/div/div[3]/table/tbody/tr[4]/td[4]/div/span'
        driver.find_element_by_xpath(end).click()
        time.sleep(2)
        certain = '/html/body/div[last()]/div[2]/button[2]/span'
        driver.find_element_by_xpath(certain).click()
        time.sleep(5)

    def test_ZZ_Quit(self):
        driver = self.driver
        driver.quit()
