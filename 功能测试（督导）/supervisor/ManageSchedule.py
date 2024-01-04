import time
import unittest

from selenium import webdriver


class MyTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome("D:\chromedriver-win64\chromedriver.exe")
        cls.driver.implicitly_wait(20)
        print('打开测试网站')
        cls.base_url = "https://sei-test.021hqit.com/group-1/#/login"
        cls.driver.get(cls.base_url)

    def test_00_Login(self):
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

    def test_01_管理咨询师排班测试01(self):
        driver = self.driver
        print('管理咨询师排班测试01')
        x = '//*[@id="app"]/div/div[1]/div/ul/li[3]/span'
        driver.find_element_by_xpath(x).click()
        time.sleep(2)

        # 移除12月15日第一个排班的咨询师
        driver.find_element_by_css_selector(
            "#app > div > div.content > div:nth-child(2) > div.workingScgedule.el-row > div.flexContent.el-col.el-col-19 > div.calendar > div.dateList > div:nth-child(17)").click()
        time.sleep(2)
        driver.find_element_by_css_selector(
            "#app > div > div.content > div:nth-child(2) > div.workingScgedule.el-row > div.rightList.el-col.el-col-5 > div.userList > div:nth-child(1) > div:nth-child(3)").click()
        time.sleep(2)
        driver.find_element_by_css_selector(
            "body > div.el-message-box__wrapper > div > div.el-message-box__btns > button.el-button.el-button--default.el-button--small.el-button--primary > span").click()
        time.sleep(5)
        driver.find_element_by_css_selector(
            "#app > div > div.content > div:nth-child(2) > div.workingScgedule.el-row > div.rightList.el-col.el-col-5 > div.userList > div:nth-child(1) > div:nth-child(3)").click()
        time.sleep(2)
        driver.find_element_by_css_selector(
            "body > div.el-message-box__wrapper > div > div.el-message-box__btns > button.el-button.el-button--default.el-button--small.el-button--primary > span").click()
        time.sleep(5)

    def test_02_管理咨询师排班测试02(self):
        driver = self.driver
        print('管理咨询师排班测试02')

        # 添加12月15日第一个排班的咨询师
        driver.find_element_by_css_selector(
            "#app > div > div.content > div:nth-child(2) > div.workingScgedule.el-row > div.rightList.el-col.el-col-5 > div:nth-child(3)").click()
        time.sleep(5)
        x = '//*[@id="app"]/div/div[2]/div[2]/div[2]/div/div[2]/form/div/div/div/div[1]/input'
        driver.find_element_by_xpath(x).click()
        time.sleep(5)
        driver.find_element_by_xpath("//ul[@class='el-scrollbar__view el-select-dropdown__list']/li[1]").click()
        time.sleep(2)
        driver.find_element_by_xpath("//ul[@class='el-scrollbar__view el-select-dropdown__list']/li[2]").click()
        time.sleep(2)
        driver.find_element_by_css_selector(
            "#app > div > div.content > div:nth-child(2) > div.el-dialog__wrapper > div > div.el-dialog__header > div > p.modalTitle").click()
        time.sleep(2)
        driver.find_element_by_css_selector(
            "#app > div > div.content > div:nth-child(2) > div.el-dialog__wrapper > div > div.el-dialog__footer > div > button.el-button.confirm.el-button--default").click()
        time.sleep(5)

    def test_Z_退出(self):
        driver = self.driver
        driver.quit()
