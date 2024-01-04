import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


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

    def test_01_查询访客测试01(self):
        # 按名称具体搜索
        driver = self.driver
        print('查询访客对话01')
        x = '//*[@id="app"]/div/div[1]/div/ul/li[6]/span'
        driver.find_element_by_xpath(x).click()
        time.sleep(2)
        # 搜索访客'komorebi0110'

        x = '//*[@id="app"]/div/div[2]/div[2]/div/div[1]/div[1]/div/input'
        driver.find_element_by_css_selector(
            "#app > div > div.content > div.manageConsultant > div.el-row.is-align-bottom.el-row--flex > div > div > input").clear()
        driver.find_element_by_css_selector(
            "#app > div > div.content > div.manageConsultant > div.el-row.is-align-bottom.el-row--flex > div > div > input").send_keys(
            "komorebi0110")
        driver.find_element_by_css_selector(
            "#app > div > div.content > div.manageConsultant > div.el-row.is-align-bottom.el-row--flex > div > div > input").send_keys(
            Keys.ENTER)
        time.sleep(5)

    def test_02_查询访客测试02(self):
        # 复合名称访客按名称模糊搜索
        driver = self.driver
        print('查询访客测试02')
        x = '//*[@id="app"]/div/div[1]/div/ul/li[1]/span'
        driver.find_element_by_xpath(x).click()
        time.sleep(2)
        x = '//*[@id="app"]/div/div[1]/div/ul/li[6]/span'
        driver.find_element_by_xpath(x).click()
        time.sleep(2)
        # 搜索访客'komorebi'
        x = '//*[@id="app"]/div/div[2]/div[2]/div/div[1]/div[1]/div/input'
        driver.find_element_by_css_selector(
            "#app > div > div.content > div.manageConsultant > div.el-row.is-align-bottom.el-row--flex > div > div > input").clear()
        driver.find_element_by_css_selector(
            "#app > div > div.content > div.manageConsultant > div.el-row.is-align-bottom.el-row--flex > div > div > input").send_keys(
            "komorebi")
        driver.find_element_by_css_selector(
            "#app > div > div.content > div.manageConsultant > div.el-row.is-align-bottom.el-row--flex > div > div > input").send_keys(
            Keys.ENTER)
        time.sleep(5)
        time.sleep(5)

    def test_03_查询访客测试03(self):
        # 复合名称访客按名称模糊搜索
        driver = self.driver
        print('查询访客测试03')
        x = '//*[@id="app"]/div/div[1]/div/ul/li[1]/span'
        driver.find_element_by_xpath(x).click()
        time.sleep(2)
        x = '//*[@id="app"]/div/div[1]/div/ul/li[6]/span'
        driver.find_element_by_xpath(x).click()
        time.sleep(2)
        # 搜索访客'0110'
        x = '//*[@id="app"]/div/div[2]/div[2]/div/div[1]/div[1]/div/input'
        driver.find_element_by_css_selector(
            "#app > div > div.content > div.manageConsultant > div.el-row.is-align-bottom.el-row--flex > div > div > input").clear()
        driver.find_element_by_css_selector(
            "#app > div > div.content > div.manageConsultant > div.el-row.is-align-bottom.el-row--flex > div > div > input").send_keys(
            "0110")
        driver.find_element_by_css_selector(
            "#app > div > div.content > div.manageConsultant > div.el-row.is-align-bottom.el-row--flex > div > div > input").send_keys(
            Keys.ENTER)
        time.sleep(5)

    def test_04_查询访客测试04(self):
        # 中文名访客的模糊搜索
        driver = self.driver
        print('查询访客测试04')
        x = '//*[@id="app"]/div/div[1]/div/ul/li[1]/span'
        driver.find_element_by_xpath(x).click()
        time.sleep(2)
        x = '//*[@id="app"]/div/div[1]/div/ul/li[6]/span'
        driver.find_element_by_xpath(x).click()
        time.sleep(2)
        # 搜索访客'刁'
        x = '//*[@id="app"]/div/div[2]/div[2]/div/div[1]/div[1]/div/input'
        driver.find_element_by_css_selector(
            "#app > div > div.content > div.manageConsultant > div.el-row.is-align-bottom.el-row--flex > div > div > input").clear()
        driver.find_element_by_css_selector(
            "#app > div > div.content > div.manageConsultant > div.el-row.is-align-bottom.el-row--flex > div > div > input").send_keys(
            "刁")
        driver.find_element_by_css_selector(
            "#app > div > div.content > div.manageConsultant > div.el-row.is-align-bottom.el-row--flex > div > div > input").send_keys(
            Keys.ENTER)
        time.sleep(5)

    def test_05_查询访客测试05(self):
        # 搜索不存在的访客
        driver = self.driver
        print('查询访客测试05')
        x = '//*[@id="app"]/div/div[1]/div/ul/li[1]/span'
        driver.find_element_by_xpath(x).click()
        time.sleep(2)
        x = '//*[@id="app"]/div/div[1]/div/ul/li[6]/span'
        driver.find_element_by_xpath(x).click()
        time.sleep(2)
        # 搜索求助者'莫小贝'
        x = '//*[@id="app"]/div/div[2]/div[2]/div/div[1]/div[1]/div/input'
        driver.find_element_by_css_selector(
            "#app > div > div.content > div.manageConsultant > div.el-row.is-align-bottom.el-row--flex > div > div > input").clear()
        driver.find_element_by_css_selector(
            "#app > div > div.content > div.manageConsultant > div.el-row.is-align-bottom.el-row--flex > div > div > input").send_keys(
            "莫小贝")
        driver.find_element_by_css_selector(
            "#app > div > div.content > div.manageConsultant > div.el-row.is-align-bottom.el-row--flex > div > div > input").send_keys(
            Keys.ENTER)
        time.sleep(5)

    def test_ZZ_退出(self):
        driver = self.driver
        driver.quit()
