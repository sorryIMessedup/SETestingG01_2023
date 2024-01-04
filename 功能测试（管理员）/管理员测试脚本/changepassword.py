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
class MyTestCase(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(20)

        cls.driver.get("https://sei-test.021hqit.com/group-1/#/login")
    def test_00_Login(self):

        driver = self.driver

        driver.find_element(By.CSS_SELECTOR,  # 输入框要提前清理里面的数据
                            "#app > div > div.login > form > div:nth-child(1) > div > div > input").clear()
        driver.find_element(By.CSS_SELECTOR,  # 输入用户名
                            "#app > div > div.login > form > div:nth-child(1) > div > div > input").send_keys("ecnu_admin")
        driver.find_element(By.CSS_SELECTOR,  # 输入框要提前清理里面的数据
                            "#app > div > div.login > form > div:nth-child(2) > div > div > input").clear()
        driver.find_element(By.CSS_SELECTOR,  # 输入密码
                            "#app > div > div.login > form > div:nth-child(2) > div > div > input").send_keys("pl,okm123")
        login_btn_ele = driver.find_element(By.CSS_SELECTOR,  # 拿到登录按钮
                                            "#app > div > div.login > div > button")
        login_btn_ele.click()  # 按下登陆按钮
        print("已按下登陆按钮")
        time.sleep(2)

    def test_01_ChangePasswordTest01(self):
        # Pwd: 123456 -> 654321 成功修改
        driver = self.driver
        print("修改密码测试01")
        user_info_init = driver.find_element(By.CSS_SELECTOR, "#app > div > div.nav > span > span > div")
        ActionChains(driver).move_to_element(user_info_init).perform()  # hover触发
        sub_menu_ele = driver.find_element(By.CSS_SELECTOR,  # 定位到二级菜单
                                           ".menuActionItem > span:nth-child(1)")
        sub_menu_ele.click()
        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR,  # 输入原密码
                            "#app > div > div.el-dialog__wrapper > div > div.el-dialog__body > form > div:nth-child(1) > div > div > div > div.changeInput.el-input.el-input--suffix > input").clear()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.el-dialog__wrapper > div > div.el-dialog__body > form > div:nth-child(1) > div > div > div > div.changeInput.el-input.el-input--suffix > input").send_keys(
            "pl,okm123")
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR,  # 输入新密码
                            "#app > div > div.el-dialog__wrapper > div > div.el-dialog__body > form > div:nth-child(2) > div > div > div > div.changeInput.el-input.el-input--suffix > input").clear()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.el-dialog__wrapper > div > div.el-dialog__body > form > div:nth-child(2) > div > div > div > div.changeInput.el-input.el-input--suffix > input").send_keys(
            "pl,okm123")
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR,  # 确认修改密码
                            "#app > div > div.el-dialog__wrapper > div > div.el-dialog__body > form > div:nth-child(3) > div > div > div > div.changeInput.el-input.el-input--suffix > input").clear()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.el-dialog__wrapper > div > div.el-dialog__body > form > div:nth-child(3) > div > div > div > div.changeInput.el-input.el-input--suffix > input").send_keys(
            "pl,okm123")
        time.sleep(1)
        modify_ensure = driver.find_element(By.CSS_SELECTOR,
                                            "#app > div > div.el-dialog__wrapper > div > div.el-dialog__footer > div > button.el-button.confirm.el-button--primary > span")
        modify_ensure.click()
        time.sleep(2)
        txt = driver.find_element(By.XPATH, "/html/body/div[last()]").text
        print(txt)
        time.sleep(2)

    def test_02_ChangePasswordTest02(self):
        # 不填入原密码
        driver = self.driver
        print('修改密码测试02')
        user_info_init = driver.find_element(By.CSS_SELECTOR, "#app > div > div.nav > span > span > div")
        ActionChains(driver).move_to_element(user_info_init).perform()  # hover触发
        sub_menu_ele = driver.find_element(By.CSS_SELECTOR,  # 定位到二级菜单
                                           ".menuActionItem > span:nth-child(1)")
        sub_menu_ele.click()
        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR,  # 输入原密码
                            "#app > div > div.el-dialog__wrapper > div > div.el-dialog__body > form > div:nth-child(1) > div > div > div > div.changeInput.el-input.el-input--suffix > input").clear()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.el-dialog__wrapper > div > div.el-dialog__body > form > div:nth-child(1) > div > div > div > div.changeInput.el-input.el-input--suffix > input").send_keys(
            "")
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR,  # 移动光标至空白处
                            "#app > div > div.el-dialog__wrapper > div > div.el-dialog__header > div > div").click()
        time.sleep(1)
        x = '//*[@id="app"]/div/div[3]/div/div[2]/form/div[1]/div/div/div/div[2]'
        txt = driver.find_element(By.XPATH, x).text
        print(txt)
        time.sleep(2)

    def test_03_ChangePasswordTest03(self):
        # 不填入新密码
        driver = self.driver
        print('修改密码测试03')
        driver.find_element(By.CSS_SELECTOR,  # 输入原密码
                            "#app > div > div.el-dialog__wrapper > div > div.el-dialog__body > form > div:nth-child(1) > div > div > div > div.changeInput.el-input.el-input--suffix > input").clear()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.el-dialog__wrapper > div > div.el-dialog__body > form > div:nth-child(1) > div > div > div > div.changeInput.el-input.el-input--suffix > input").send_keys(
            "pl,okm123")
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR,  # 输入新密码
                            "#app > div > div.el-dialog__wrapper > div > div.el-dialog__body > form > div:nth-child(2) > div > div > div > div.changeInput.el-input.el-input--suffix > input").clear()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.el-dialog__wrapper > div > div.el-dialog__body > form > div:nth-child(2) > div > div > div > div.changeInput.el-input.el-input--suffix > input").send_keys(
            "")
        driver.find_element(By.CSS_SELECTOR,  # 移动光标至空白处
                            "#app > div > div.el-dialog__wrapper > div > div.el-dialog__header > div > div").click()
        time.sleep(1)
        x = '//*[@id="app"]/div/div[3]/div/div[2]/form/div[2]/div/div/div/div[2]'
        txt = driver.find_element(By.XPATH, x).text
        print(txt)
        time.sleep(2)

    def test_04_ChangePasswordTest04(self):
        # 不填入确认密码
        driver = self.driver
        print('修改密码测试04')
        driver.find_element(By.CSS_SELECTOR,  # 输入原密码
                            "#app > div > div.el-dialog__wrapper > div > div.el-dialog__body > form > div:nth-child(1) > div > div > div > div.changeInput.el-input.el-input--suffix > input").clear()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.el-dialog__wrapper > div > div.el-dialog__body > form > div:nth-child(1) > div > div > div > div.changeInput.el-input.el-input--suffix > input").send_keys(
            "pl,okm123")
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR,  # 输入新密码
                            "#app > div > div.el-dialog__wrapper > div > div.el-dialog__body > form > div:nth-child(2) > div > div > div > div.changeInput.el-input.el-input--suffix > input").clear()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.el-dialog__wrapper > div > div.el-dialog__body > form > div:nth-child(2) > div > div > div > div.changeInput.el-input.el-input--suffix > input").send_keys(
            "123456")
        driver.find_element(By.CSS_SELECTOR,  # 确认修改密码
                            "#app > div > div.el-dialog__wrapper > div > div.el-dialog__body > form > div:nth-child(3) > div > div > div > div.changeInput.el-input.el-input--suffix > input").clear()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.el-dialog__wrapper > div > div.el-dialog__body > form > div:nth-child(3) > div > div > div > div.changeInput.el-input.el-input--suffix > input").send_keys(
            "")
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR,  # 移动光标至空白处
                            "#app > div > div.el-dialog__wrapper > div > div.el-dialog__header > div > div").click()
        time.sleep(1)
        x = '//*[@id="app"]/div/div[3]/div/div[2]/form/div[3]/div/div/div/div[2]'
        txt = driver.find_element(By.XPATH, x).text
        print(txt)
        time.sleep(2)

    def test_05_ChangePasswordTest05(self):
        # Pwd: 654321 -> 1234 (!) 新密码过短
        driver = self.driver
        print('修改密码测试05')
        driver.find_element(By.CSS_SELECTOR,  # 输入原密码
                            "#app > div > div.el-dialog__wrapper > div > div.el-dialog__body > form > div:nth-child(1) > div > div > div > div.changeInput.el-input.el-input--suffix > input").clear()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.el-dialog__wrapper > div > div.el-dialog__body > form > div:nth-child(1) > div > div > div > div.changeInput.el-input.el-input--suffix > input").send_keys(
            "pl,okm123")
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR,  # 输入新密码
                            "#app > div > div.el-dialog__wrapper > div > div.el-dialog__body > form > div:nth-child(2) > div > div > div > div.changeInput.el-input.el-input--suffix > input").clear()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.el-dialog__wrapper > div > div.el-dialog__body > form > div:nth-child(2) > div > div > div > div.changeInput.el-input.el-input--suffix > input").send_keys(
            "1234")
        driver.find_element(By.CSS_SELECTOR,  # 移动光标至空白处
                            "#app > div > div.el-dialog__wrapper > div > div.el-dialog__header > div > div").click()
        time.sleep(1)
        x = '//*[@id="app"]/div/div[3]/div/div[2]/form/div[2]/div/div/div/div[2]'
        txt = driver.find_element(By.XPATH, x).text
        print(txt)
        time.sleep(2)

    def test_06_ChangePasswordTest06(self):
        # Pwd: 654321 -> 11451419198101145141919810 (!) 新密码过长
        driver = self.driver
        print('修改密码测试06')
        driver.find_element(By.CSS_SELECTOR,  # 输入新密码
                            "#app > div > div.el-dialog__wrapper > div > div.el-dialog__body > form > div:nth-child(2) > div > div > div > div.changeInput.el-input.el-input--suffix > input").clear()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.el-dialog__wrapper > div > div.el-dialog__body > form > div:nth-child(2) > div > div > div > div.changeInput.el-input.el-input--suffix > input").send_keys(
            "11451419198101145141919810")
        driver.find_element(By.CSS_SELECTOR,  # 移动光标至空白处
                            "#app > div > div.el-dialog__wrapper > div > div.el-dialog__header > div > div").click()
        time.sleep(2)
        x = '//*[@id="app"]/div/div[3]/div/div[2]/form/div[2]/div/div/div/div[2]'
        txt = driver.find_element(By.XPATH, x).text
        print(txt)
        time.sleep(2)

    def test_07_ChangePasswordTest07(self):
        # Pwd: 654321 -> 123456 (!) 原密码错误
        driver = self.driver
        print("修改密码测试07")
        driver.find_element(By.CSS_SELECTOR,  # 输入原密码
                            "#app > div > div.el-dialog__wrapper > div > div.el-dialog__body > form > div:nth-child(1) > div > div > div > div.changeInput.el-input.el-input--suffix > input").clear()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.el-dialog__wrapper > div > div.el-dialog__body > form > div:nth-child(1) > div > div > div > div.changeInput.el-input.el-input--suffix > input").send_keys(
            "114514")
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR,  # 输入新密码
                            "#app > div > div.el-dialog__wrapper > div > div.el-dialog__body > form > div:nth-child(2) > div > div > div > div.changeInput.el-input.el-input--suffix > input").clear()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.el-dialog__wrapper > div > div.el-dialog__body > form > div:nth-child(2) > div > div > div > div.changeInput.el-input.el-input--suffix > input").send_keys(
            "123456")
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR,  # 确认修改密码
                            "#app > div > div.el-dialog__wrapper > div > div.el-dialog__body > form > div:nth-child(3) > div > div > div > div.changeInput.el-input.el-input--suffix > input").clear()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.el-dialog__wrapper > div > div.el-dialog__body > form > div:nth-child(3) > div > div > div > div.changeInput.el-input.el-input--suffix > input").send_keys(
            "123456")
        time.sleep(1)
        modify_ensure = driver.find_element(By.CSS_SELECTOR,
                                            "#app > div > div.el-dialog__wrapper > div > div.el-dialog__footer > div > button.el-button.confirm.el-button--primary > span")
        modify_ensure.click()
        time.sleep(1)
        x = '/html/body/div[4]/p'
        txt = driver.find_element(By.XPATH, x).text
        print(txt)
        time.sleep(2)

    def test_08_ChangePasswordTest08(self):
        # Pwd: 654321 -> 123456 (!) 新密码确认不一致
        driver = self.driver
        print("修改密码测试08")
        driver.find_element(By.CSS_SELECTOR,  # 输入原密码
                            "#app > div > div.el-dialog__wrapper > div > div.el-dialog__body > form > div:nth-child(1) > div > div > div > div.changeInput.el-input.el-input--suffix > input").clear()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.el-dialog__wrapper > div > div.el-dialog__body > form > div:nth-child(1) > div > div > div > div.changeInput.el-input.el-input--suffix > input").send_keys(
            "pl,okm123")
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR,  # 输入新密码
                            "#app > div > div.el-dialog__wrapper > div > div.el-dialog__body > form > div:nth-child(2) > div > div > div > div.changeInput.el-input.el-input--suffix > input").clear()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.el-dialog__wrapper > div > div.el-dialog__body > form > div:nth-child(2) > div > div > div > div.changeInput.el-input.el-input--suffix > input").send_keys(
            "123456")
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR,  # 确认修改密码
                            "#app > div > div.el-dialog__wrapper > div > div.el-dialog__body > form > div:nth-child(3) > div > div > div > div.changeInput.el-input.el-input--suffix > input").clear()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.el-dialog__wrapper > div > div.el-dialog__body > form > div:nth-child(3) > div > div > div > div.changeInput.el-input.el-input--suffix > input").send_keys(
            "1234567")
        time.sleep(1)
        modify_ensure = driver.find_element(By.CSS_SELECTOR,
                                            "#app > div > div.el-dialog__wrapper > div > div.el-dialog__footer > div > button.el-button.confirm.el-button--primary > span")
        modify_ensure.click()
        time.sleep(2)
        x = '//*[@id="app"]/div/div[3]/div/div[2]/form/div[3]/div/div/div/div[2]'
        txt = driver.find_element(By.XPATH, x).text
        print(txt)
        time.sleep(2)



    def test_09_QuitTest01(self):
        driver = self.driver
        user_info_init = driver.find_element(By.CSS_SELECTOR,
                                             "#app > div > div.nav > span > span > div")
        ActionChains(driver).move_to_element(user_info_init).perform()
        sub_menu_ele = driver.find_element(By.CSS_SELECTOR,
                                           ".menuActionItem > span:nth-child(2)")
        sub_menu_ele.click()
        time.sleep(2)

    def test_10_QuitTest02(self):
        driver = self.driver
        driver.quit()
