import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import unittest
class MyTestCasewrt(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(20)
        print('打开测试网站')
        cls.driver.get("https://sei-test.021hqit.com/group-1/#/login")

    def test_00_Login(self):
        # 登陆平台
        driver = self.driver
        print('测试登录')
        driver.find_element(By.CSS_SELECTOR,  # 输入框要提前清理里面的数据
                            "#app > div > div.login > form > div:nth-child(1) > div > div > input").clear()

        driver.find_element(By.CSS_SELECTOR,  # 输入框要提前清理里面的数据
                            "#app > div > div.login > form > div:nth-child(2) > div > div > input").clear()
        driver.find_element(By.CSS_SELECTOR,  # 输入密码
                            "#app > div > div.login > form > div:nth-child(2) > div > div > input").send_keys(
            "pl,okm123")
        login_btn_ele = driver.find_element(By.CSS_SELECTOR,  # 拿到登录按钮
                                            "#app > div > div.login > div > button")
        login_btn_ele.click()

    def test_01_Loginn(self):
        # 登陆平台
        driver = self.driver
        print('测试登录')
        driver.find_element(By.CSS_SELECTOR,  # 输入框要提前清理里面的数据
                            "#app > div > div.login > form > div:nth-child(1) > div > div > input").clear()
        driver.find_element(By.CSS_SELECTOR,  # 输入用户名
                            "#app > div > div.login > form > div:nth-child(1) > div > div > input").send_keys("ecnu_admin")
        driver.find_element(By.CSS_SELECTOR,  # 输入框要提前清理里面的数据
                            "#app > div > div.login > form > div:nth-child(2) > div > div > input").clear()

        login_btn_ele = driver.find_element(By.CSS_SELECTOR,  # 拿到登录按钮
                                            "#app > div > div.login > div > button")
        login_btn_ele.click()

    def test_02_Logine(self):
        # 登陆平台
        driver = self.driver
        print('测试登录')
        driver.find_element(By.CSS_SELECTOR,  # 输入框要提前清理里面的数据
                            "#app > div > div.login > form > div:nth-child(1) > div > div > input").clear()
        driver.find_element(By.CSS_SELECTOR,  # 输入用户名
                            "#app > div > div.login > form > div:nth-child(1) > div > div > input").send_keys("ecnu_admin")
        driver.find_element(By.CSS_SELECTOR,  # 输入框要提前清理里面的数据
                            "#app > div > div.login > form > div:nth-child(2) > div > div > input").clear()
        driver.find_element(By.CSS_SELECTOR,  # 输入密码
                            "#app > div > div.login > form > div:nth-child(2) > div > div > input").send_keys(
            "pl,okm12")
        login_btn_ele = driver.find_element(By.CSS_SELECTOR,  # 拿到登录按钮
                                            "#app > div > div.login > div > button")
        login_btn_ele.click()

    def test_03_Loginm(self):
        # 登陆平台
        driver = self.driver
        print('测试登录')
        driver.find_element(By.CSS_SELECTOR,  # 输入框要提前清理里面的数据
                            "#app > div > div.login > form > div:nth-child(1) > div > div > input").clear()
        driver.find_element(By.CSS_SELECTOR,  # 输入用户名
                            "#app > div > div.login > form > div:nth-child(1) > div > div > input").send_keys("ecnu_admin")
        driver.find_element(By.CSS_SELECTOR,  # 输入框要提前清理里面的数据
                            "#app > div > div.login > form > div:nth-child(2) > div > div > input").clear()
        driver.find_element(By.CSS_SELECTOR,  # 输入密码
                            "#app > div > div.login > form > div:nth-child(2) > div > div > input").send_keys(
            "pl,okm123")
        login_btn_ele = driver.find_element(By.CSS_SELECTOR,  # 拿到登录按钮
                                            "#app > div > div.login > div > button")
        login_btn_ele.click()
    def test_04_QuitTest01(self):
        driver = self.driver
        user_info_init = driver.find_element(By.CSS_SELECTOR,
                                             "#app > div > div.nav > span > span > div")
        ActionChains(driver).move_to_element(user_info_init).perform()
        sub_menu_ele = driver.find_element(By.CSS_SELECTOR,
                                           ".menuActionItem > span:nth-child(2)")
        sub_menu_ele.click()
        time.sleep(2)

    def test_05_QuitTest02(self):
        driver = self.driver
        driver.quit()
