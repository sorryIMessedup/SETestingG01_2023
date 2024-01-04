# coding=utf8
import time
import unittest

from selenium import webdriver


class MyTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome("D:\chromedriver-win64\chromedriver.exe")
        self.driver.implicitly_wait(20)
        print('打开测试网站')
        self.base_url = "https://sei-test.021hqit.com/group-1/#/login"
        self.driver.get(self.base_url)

    def test_00_登录(self):
        driver = self.driver
        print('测试登录')
        # 查找输入框,输入账号，输入框要提前清理里面的数据
        driver.find_element_by_css_selector(
            "#app > div > div.login > form > div:nth-child(1) > div > div > input").clear()
        driver.find_element_by_css_selector(
            "#app > div > div.login > form > div:nth-child(1) > div > div > input").send_keys("adudao")
        # 查找密码输入框，输入密码
        driver.find_element_by_css_selector(
            "#app > div > div.login > form > div:nth-child(2) > div > div > input").clear()
        driver.find_element_by_css_selector(
            "#app > div > div.login > form > div:nth-child(2) > div > div > input").send_keys("adudao")

        # 拿到登录按钮
        login_btn_ele = driver.find_element_by_css_selector("#app > div > div.login > div > button")
        login_btn_ele.click()
        time.sleep(5)

    def test_01_查询咨询师排班测试01(self):
        driver = self.driver
        print('查询咨询师排班测试01')
        x = '//*[@id="app"]/div/div[1]/div/ul/li[3]/span'
        driver.find_element_by_xpath(x).click()
        time.sleep(2)
        # 以12月1日为例
        driver.find_element_by_css_selector(
            "#app > div > div.content > div:nth-child(2) > div.workingScgedule.el-row > div.flexContent.el-col.el-col-19 > div.calendar > div.dateList > div:nth-child(3)").click()
        time.sleep(5)

    def test_02_查询咨询师排班测试02(self):
        driver = self.driver
        print('查询咨询师排班测试01')
        # 12月2日依次往后
        driver.find_element_by_css_selector(
            "#app > div > div.content > div:nth-child(2) > div.workingScgedule.el-row > div.flexContent.el-col.el-col-19 > div.calendar > div.dateList > div:nth-child(4)").click()
        time.sleep(5)

    def test_03_查询咨询师排班测试03(self):
        driver = self.driver
        print('查询咨询师排班测试03')

        driver.find_element_by_css_selector(
            "#app > div > div.content > div:nth-child(2) > div.workingScgedule.el-row > div.flexContent.el-col.el-col-19 > div.calendar > div.dateList > div:nth-child(5)").click()
        time.sleep(5)

    def test_04_查询咨询师排班测试04(self):
        driver = self.driver
        print('查询咨询师排班测试04')

        driver.find_element_by_css_selector(
            "#app > div > div.content > div:nth-child(2) > div.workingScgedule.el-row > div.flexContent.el-col.el-col-19 > div.calendar > div.dateList > div:nth-child(6)").click()
        time.sleep(5)

    def test_05_查询咨询师排班测试05(self):
        driver = self.driver
        print('查询咨询师排班测试05')

        driver.find_element_by_css_selector(
            "#app > div > div.content > div:nth-child(2) > div.workingScgedule.el-row > div.flexContent.el-col.el-col-19 > div.calendar > div.dateList > div:nth-child(7)").click()
        time.sleep(5)

    def test_06_查询咨询师排班测试06(self):
        driver = self.driver
        print('查询咨询师排班测试06')

        driver.find_element_by_css_selector(
            "#app > div > div.content > div:nth-child(2) > div.workingScgedule.el-row > div.flexContent.el-col.el-col-19 > div.calendar > div.dateList > div:nth-child(8)").click()
        time.sleep(5)

    def test_07_查询咨询师排班测试07(self):
        driver = self.driver
        print('查询咨询师排班测试07')

        driver.find_element_by_css_selector(
            "#app > div > div.content > div:nth-child(2) > div.workingScgedule.el-row > div.flexContent.el-col.el-col-19 > div.calendar > div.dateList > div:nth-child(9)").click()
        time.sleep(5)

    def test_08_查询咨询师排班测试08(self):
        driver = self.driver
        print('查询咨询师排班测试07')

        driver.find_element_by_css_selector(
            "#app > div > div.content > div:nth-child(2) > div.workingScgedule.el-row > div.flexContent.el-col.el-col-19 > div.calendar > div.dateList > div:nth-child(10)").click()
        time.sleep(5)

    def test_ZZ_退出(self):
        driver = self.driver
        driver.quit()
