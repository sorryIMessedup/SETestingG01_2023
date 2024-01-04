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

    def test_0_登录(self):
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

    def test_1_查询咨询师账号测试01(self):
        # 具体搜索
        driver = self.driver
        print('查询咨询师账号测试01')
        x = '//*[@id="app"]/div/div[1]/div/ul/li[5]/span'
        driver.find_element_by_xpath(x).click()
        time.sleep(2)
        x = '//*[@id="app"]/div/div[1]/div/ul/li[5]/span'
        driver.find_element_by_xpath(x).click()
        time.sleep(3)
        x = '//*[@id="app"]/div/div[2]/div[2]/div[1]/div[1]/div/input'
        driver.find_element_by_xpath(x).send_keys('胡某某')
        driver.find_element_by_xpath(x).send_keys(Keys.ENTER)
        time.sleep(5)

    def test_2_查询咨询师账号测试02(self):
        # 具体搜索
        driver = self.driver
        print('查询咨询师账号测试02')
        x = '//*[@id="app"]/div/div[2]/div[2]/div[1]/div[1]/div/input'
        driver.find_element_by_xpath(x).clear()
        driver.find_element_by_xpath(x).send_keys(Keys.ENTER)
        time.sleep(5)
        driver.find_element_by_xpath(x).send_keys('yoyi')
        driver.find_element_by_xpath(x).send_keys(Keys.ENTER)
        time.sleep(5)

    def test_3_查询咨询师账号测试03(self):
        # 具体搜索
        driver = self.driver
        print('查询咨询师账号测试03')
        x = '//*[@id="app"]/div/div[2]/div[2]/div[1]/div[1]/div/input'
        driver.find_element_by_xpath(x).clear()
        driver.find_element_by_xpath(x).send_keys(Keys.ENTER)
        time.sleep(5)
        driver.find_element_by_xpath(x).send_keys('大数据应用的场景')
        driver.find_element_by_xpath(x).send_keys(Keys.ENTER)
        time.sleep(5)

    def test_4_查询咨询师账号测试04(self):
        # 模糊搜索
        driver = self.driver
        print('查询咨询师账号测试03')
        x = '//*[@id="app"]/div/div[2]/div[2]/div[1]/div[1]/div/input'
        driver.find_element_by_xpath(x).clear()
        driver.find_element_by_xpath(x).send_keys(Keys.ENTER)
        time.sleep(5)
        driver.find_element_by_xpath(x).send_keys('大数据应用的场景')
        driver.find_element_by_xpath(x).send_keys(Keys.ENTER)
        time.sleep(5)

    def test_5_查询咨询师账号测试05(self):
        # 搜索不存在
        driver = self.driver
        print('查询咨询师账号测试05')
        x = '//*[@id="app"]/div/div[2]/div[2]/div[1]/div[1]/div/input'
        driver.find_element_by_xpath(x).clear()
        driver.find_element_by_xpath(x).send_keys(Keys.ENTER)
        time.sleep(5)
        driver.find_element_by_xpath(x).send_keys('函数语言设计')
        driver.find_element_by_xpath(x).send_keys(Keys.ENTER)
        time.sleep(5)
        x = '//*[@id="app"]/div/div[2]/div[2]/div[2]/div[1]/div[3]/div/span'
        txt = driver.find_element_by_xpath(x).text
        print(txt)
        time.sleep(2)

    def test_6_查询咨询师账号测试06(self):
        # 搜索不存在
        driver = self.driver
        print('查询咨询师账号测试06')
        x = '//*[@id="app"]/div/div[2]/div[2]/div[1]/div[1]/div/input'
        driver.find_element_by_xpath(x).clear()
        driver.find_element_by_xpath(x).send_keys(Keys.ENTER)
        time.sleep(5)
        driver.find_element_by_xpath(x).send_keys('植物力量燕麦奶')
        driver.find_element_by_xpath(x).send_keys(Keys.ENTER)
        time.sleep(5)
        x = '//*[@id="app"]/div/div[2]/div[2]/div[2]/div[1]/div[3]/div/span'
        txt = driver.find_element_by_xpath(x).text
        print(txt)
        time.sleep(2)

    def test_Z_退出(self):
        driver = self.driver
        driver.quit()
