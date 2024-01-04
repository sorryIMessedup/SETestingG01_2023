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


class TestSucceeww(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(20)
        print('打开测试网站')
        cls.driver.get("https://sei-test.021hqit.com/group-1/#/login")

    def test_01_Consultant01(self):
        driver = self.driver
        driver.find_element(By.CSS_SELECTOR,  # 输入框要提前清理里面的数据
                            "#app > div > div.login > form > div:nth-child(1) > div > div > input").clear()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.login > form > div:nth-child(1) > div > div > input").send_keys(
            "ecnu_admin")
        driver.find_element(By.CSS_SELECTOR,  # 输入框要提前清理里面的数据
                            "#app > div > div.login > form > div:nth-child(2) > div > div > input").clear()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.login > form > div:nth-child(2) > div > div > input").send_keys(
            "pl,okm123")
        driver.find_element(By.CSS_SELECTOR, "#app > div > div.login > div > button").click()
        driver.find_element(By.CSS_SELECTOR,"#app > div > div.nav > div > ul > li:nth-child(5) > img").click()
        driver.find_element(By.CSS_SELECTOR,"#app > div > div.content > div.manageConsultant > div.el-row.is-align-bottom.el-row--flex > div.el-col.el-col-20 > button > span").click()
        driver.find_element(By.CSS_SELECTOR,"#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(1) > div:nth-child(1) > div > div > div > input").clear()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(1) > div:nth-child(1) > div > div > div > input").send_keys("qwert")
        driver.find_element(By.CSS_SELECTOR,"#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(1) > div:nth-child(2) > div > div > div > input").clear()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(1) > div:nth-child(2) > div > div > div > input").send_keys("18912345678")
        driver.find_element(By.CSS_SELECTOR,"#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(2) > div.el-col.el-col-12 > div > div > div.changeInput.el-input.el-input--suffix > input").clear()
        driver.find_element(By.CSS_SELECTOR,"#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(2) > div.el-col.el-col-12 > div > div > div.changeInput.el-input.el-input--suffix > input").send_keys("350823200212080079")
        driver.find_element(By.CSS_SELECTOR,"#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(3) > div:nth-child(1) > div > div > div > input").clear()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(3) > div:nth-child(1) > div > div > div > input").send_keys("123456@qq.com")
        driver.find_element(By.CSS_SELECTOR,"#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(3) > div:nth-child(2) > div > div > div > div.el-select__tags > input").click()
        driver.find_element(By.CSS_SELECTOR,"body > div.el-select-dropdown.el-popper.is-multiple > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(1) > span").click()
        driver.find_element(By.CSS_SELECTOR,"#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(4) > div:nth-child(1) > div > div > div > input").clear()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(4) > div:nth-child(1) > div > div > div > input").send_keys("qwe")
        driver.find_element(By.CSS_SELECTOR,"#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(4) > div:nth-child(2) > div > div > div > input").clear()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(4) > div:nth-child(2) > div > div > div > input").send_keys("高级")
        driver.find_element(By.CSS_SELECTOR,"#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(5) > div > div > div > div > input").clear()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(5) > div > div > div > div > input").send_keys("fgdgsdkklltyss")
        driver.find_element(By.CSS_SELECTOR,"#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(6) > div > div > div > div > input").clear()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(6) > div > div > div > div > input").send_keys("12354s")
        driver.find_element(By.CSS_SELECTOR,"#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__footer > div > button.el-button.confirm.el-button--primary > span").click()
        time.sleep(2)

    def test_02_Consultant02(self):
        driver = self.driver

        driver.find_element(By.CSS_SELECTOR,"#app > div > div.content > div.manageConsultant > div.el-row.is-align-bottom.el-row--flex > div.el-col.el-col-20 > button > span").click()
        driver.find_element(By.CSS_SELECTOR,"#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(1) > div:nth-child(1) > div > div > div > input").clear()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(1) > div:nth-child(1) > div > div > div > input").send_keys("qwert@")
        driver.find_element(By.CSS_SELECTOR,"#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(1) > div:nth-child(2) > div > div > div > input").clear()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(1) > div:nth-child(2) > div > div > div > input").send_keys("18912345678")
        driver.find_element(By.CSS_SELECTOR,"#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(2) > div.el-col.el-col-12 > div > div > div.changeInput.el-input.el-input--suffix > input").clear()
        driver.find_element(By.CSS_SELECTOR,"#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(2) > div.el-col.el-col-12 > div > div > div.changeInput.el-input.el-input--suffix > input").send_keys("350823200212080079")
        driver.find_element(By.CSS_SELECTOR,"#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(3) > div:nth-child(1) > div > div > div > input").clear()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(3) > div:nth-child(1) > div > div > div > input").send_keys("123456@qq.com")
        driver.find_element(By.CSS_SELECTOR,"#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(3) > div:nth-child(2) > div > div > div > div.el-select__tags > input").click()
        driver.find_element(By.CSS_SELECTOR,"body > div.el-select-dropdown.el-popper.is-multiple > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(1) > span").click()
        driver.find_element(By.CSS_SELECTOR,"#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(4) > div:nth-child(1) > div > div > div > input").clear()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(4) > div:nth-child(1) > div > div > div > input").send_keys("qwe")
        driver.find_element(By.CSS_SELECTOR,"#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(4) > div:nth-child(2) > div > div > div > input").clear()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(4) > div:nth-child(2) > div > div > div > input").send_keys("高级")
        driver.find_element(By.CSS_SELECTOR,"#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(5) > div > div > div > div > input").clear()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(5) > div > div > div > div > input").send_keys("fgdgvasbbb")
        driver.find_element(By.CSS_SELECTOR,"#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(6) > div > div > div > div > input").clear()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(6) > div > div > div > div > input").send_keys("12354s")
        driver.find_element(By.CSS_SELECTOR,"#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__footer > div > button.el-button.confirm.el-button--primary > span").click()
        time.sleep(2)

    def test_03_Consultant03(self):
        driver = self.driver
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(1) > div:nth-child(1) > div > div > div > input").clear()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(1) > div:nth-child(1) > div > div > div > input").send_keys(
            "qwertr")
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(1) > div:nth-child(2) > div > div > div > input").clear()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(1) > div:nth-child(2) > div > div > div > input").send_keys(
            "18912345678")
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(2) > div.el-col.el-col-12 > div > div > div.changeInput.el-input.el-input--suffix > input").clear()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(2) > div.el-col.el-col-12 > div > div > div.changeInput.el-input.el-input--suffix > input").send_keys(
            "350823200212080079")
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(3) > div:nth-child(1) > div > div > div > input").clear()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(3) > div:nth-child(1) > div > div > div > input").send_keys(
            "123456@qq.com")

        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(4) > div:nth-child(1) > div > div > div > input").clear()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(4) > div:nth-child(1) > div > div > div > input").send_keys(
            "qwe")
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(4) > div:nth-child(2) > div > div > div > input").clear()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(4) > div:nth-child(2) > div > div > div > input").send_keys(
            "高级")
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(5) > div > div > div > div > input").clear()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(5) > div > div > div > div > input").send_keys(
            "fgdghj")
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(6) > div > div > div > div > input").clear()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(6) > div > div > div > div > input").send_keys(
            "12354s")
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__footer > div > button.el-button.confirm.el-button--primary > span").click()
        time.sleep(2)

    def test_04_Consultant04(self):
        driver = self.driver
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(1) > div:nth-child(1) > div > div > div > input").clear()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(1) > div:nth-child(1) > div > div > div > input").send_keys(
            "qwertr@")
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(1) > div:nth-child(2) > div > div > div > input").clear()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(1) > div:nth-child(2) > div > div > div > input").send_keys(
            "18912345678")
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(2) > div.el-col.el-col-12 > div > div > div.changeInput.el-input.el-input--suffix > input").clear()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(2) > div.el-col.el-col-12 > div > div > div.changeInput.el-input.el-input--suffix > input").send_keys(
            "350823200212080079")
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(3) > div:nth-child(1) > div > div > div > input").clear()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(3) > div:nth-child(1) > div > div > div > input").send_keys(
            "123456@qq.com")

        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(4) > div:nth-child(1) > div > div > div > input").clear()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(4) > div:nth-child(1) > div > div > div > input").send_keys(
            "qwe")
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(4) > div:nth-child(2) > div > div > div > input").clear()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(4) > div:nth-child(2) > div > div > div > input").send_keys(
            "高级")
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(5) > div > div > div > div > input").clear()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(5) > div > div > div > div > input").send_keys(
            "fgdgcvshj")
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(6) > div > div > div > div > input").clear()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(6) > div > div > div > div > input").send_keys(
            "12354s")
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__footer > div > button.el-button.confirm.el-button--primary > span").click()
        time.sleep(2)

    def test_05_Consultant05(self):
        driver = self.driver
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(1) > div:nth-child(1) > div > div > div > input").clear()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(1) > div:nth-child(1) > div > div > div > input").send_keys(
            "qwertr")
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(1) > div:nth-child(2) > div > div > div > input").clear()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(1) > div:nth-child(2) > div > div > div > input").send_keys(
            "189123456781")
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(2) > div.el-col.el-col-12 > div > div > div.changeInput.el-input.el-input--suffix > input").clear()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(2) > div.el-col.el-col-12 > div > div > div.changeInput.el-input.el-input--suffix > input").send_keys(
            "350823200212080079")
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(3) > div:nth-child(1) > div > div > div > input").clear()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(3) > div:nth-child(1) > div > div > div > input").send_keys(
            "123456@qq.com")

        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(4) > div:nth-child(1) > div > div > div > input").clear()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(4) > div:nth-child(1) > div > div > div > input").send_keys(
            "qwe")
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(4) > div:nth-child(2) > div > div > div > input").clear()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(4) > div:nth-child(2) > div > div > div > input").send_keys(
            "高级")
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(5) > div > div > div > div > input").clear()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(5) > div > div > div > div > input").send_keys(
            "fgxcdghj")
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(6) > div > div > div > div > input").clear()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(6) > div > div > div > div > input").send_keys(
            "12354s")
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__footer > div > button.el-button.confirm.el-button--primary > span").click()
        time.sleep(2)

    def test_06_Consultant06(self):
        driver = self.driver
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(1) > div:nth-child(1) > div > div > div > input").clear()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(1) > div:nth-child(1) > div > div > div > input").send_keys(
            "qwertr")
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(1) > div:nth-child(2) > div > div > div > input").clear()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(1) > div:nth-child(2) > div > div > div > input").send_keys(
            "18912345678")
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(2) > div.el-col.el-col-12 > div > div > div.changeInput.el-input.el-input--suffix > input").clear()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(2) > div.el-col.el-col-12 > div > div > div.changeInput.el-input.el-input--suffix > input").send_keys(
            "3508232002120800791")
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(3) > div:nth-child(1) > div > div > div > input").clear()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(3) > div:nth-child(1) > div > div > div > input").send_keys(
            "123456@qq.com")

        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(4) > div:nth-child(1) > div > div > div > input").clear()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(4) > div:nth-child(1) > div > div > div > input").send_keys(
            "qwe")
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(4) > div:nth-child(2) > div > div > div > input").clear()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(4) > div:nth-child(2) > div > div > div > input").send_keys(
            "高级")
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(5) > div > div > div > div > input").clear()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(5) > div > div > div > div > input").send_keys(
            "fgdghj")
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(6) > div > div > div > div > input").clear()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(6) > div > div > div > div > input").send_keys(
            "12354s")
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__footer > div > button.el-button.confirm.el-button--primary > span").click()
        time.sleep(2)

    def test_07_Consultant07(self):
        driver = self.driver
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(1) > div:nth-child(1) > div > div > div > input").clear()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(1) > div:nth-child(1) > div > div > div > input").send_keys(
            "qwertr")
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(1) > div:nth-child(2) > div > div > div > input").clear()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(1) > div:nth-child(2) > div > div > div > input").send_keys(
            "18912345678")
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(2) > div.el-col.el-col-12 > div > div > div.changeInput.el-input.el-input--suffix > input").clear()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(2) > div.el-col.el-col-12 > div > div > div.changeInput.el-input.el-input--suffix > input").send_keys(
            "350823200212080079")
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(3) > div:nth-child(1) > div > div > div > input").clear()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(3) > div:nth-child(1) > div > div > div > input").send_keys(
            "123456@qq.com")

        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(4) > div:nth-child(1) > div > div > div > input").clear()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(4) > div:nth-child(1) > div > div > div > input").send_keys(
            "qwe")
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(4) > div:nth-child(2) > div > div > div > input").clear()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(4) > div:nth-child(2) > div > div > div > input").send_keys(
            "高级")
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(5) > div > div > div > div > input").clear()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(5) > div > div > div > div > input").send_keys(
            "fgdghj@")
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(6) > div > div > div > div > input").clear()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(6) > div > div > div > div > input").send_keys(
            "12354s")
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__footer > div > button.el-button.confirm.el-button--primary > span").click()
        time.sleep(2)

    def test_08_Consultant08(self):
        driver = self.driver
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(1) > div:nth-child(1) > div > div > div > input").clear()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(1) > div:nth-child(1) > div > div > div > input").send_keys(
            "qwertr")
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(1) > div:nth-child(2) > div > div > div > input").clear()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(1) > div:nth-child(2) > div > div > div > input").send_keys(
            "18912345678")
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(2) > div.el-col.el-col-12 > div > div > div.changeInput.el-input.el-input--suffix > input").clear()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(2) > div.el-col.el-col-12 > div > div > div.changeInput.el-input.el-input--suffix > input").send_keys(
            "350823200212080079")
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(3) > div:nth-child(1) > div > div > div > input").clear()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(3) > div:nth-child(1) > div > div > div > input").send_keys(
            "123456@qq.com")

        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(4) > div:nth-child(1) > div > div > div > input").clear()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(4) > div:nth-child(1) > div > div > div > input").send_keys(
            "qwe")
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(4) > div:nth-child(2) > div > div > div > input").clear()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(4) > div:nth-child(2) > div > div > div > input").send_keys(
            "高级")
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(5) > div > div > div > div > input").clear()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(5) > div > div > div > div > input").send_keys(
            "fgdghj")
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(6) > div > div > div > div > input").clear()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(6) > div > div > div > div > input").send_keys(
            "12354s￥￥")
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__footer > div > button.el-button.confirm.el-button--primary > span").click()
        time.sleep(2)

    def test_09_Consultant09(self):
        driver = self.driver
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(1) > div:nth-child(1) > div > div > div > input").clear()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(1) > div:nth-child(1) > div > div > div > input").send_keys(
            "qwertr")
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(1) > div:nth-child(2) > div > div > div > input").clear()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(1) > div:nth-child(2) > div > div > div > input").send_keys(
            "18912345678")
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(2) > div.el-col.el-col-12 > div > div > div.changeInput.el-input.el-input--suffix > input").clear()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(2) > div.el-col.el-col-12 > div > div > div.changeInput.el-input.el-input--suffix > input").send_keys(
            "350823200212080079")
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(3) > div:nth-child(1) > div > div > div > input").clear()

        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(4) > div:nth-child(1) > div > div > div > input").clear()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(4) > div:nth-child(1) > div > div > div > input").send_keys(
            "qwe")
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(4) > div:nth-child(2) > div > div > div > input").clear()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(4) > div:nth-child(2) > div > div > div > input").send_keys(
            "高级")
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(5) > div > div > div > div > input").clear()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(5) > div > div > div > div > input").send_keys(
            "fgdghj")
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(6) > div > div > div > div > input").clear()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(6) > div > div > div > div > input").send_keys(
            "12354s")
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__footer > div > button.el-button.confirm.el-button--primary > span").click()
        time.sleep(2)

    def test_10_Consultant10(self):
        driver = self.driver
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(1) > div:nth-child(1) > div > div > div > input").clear()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(1) > div:nth-child(1) > div > div > div > input").send_keys(
            "qwertr")
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(1) > div:nth-child(2) > div > div > div > input").clear()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(1) > div:nth-child(2) > div > div > div > input").send_keys(
            "18912345678")
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(2) > div.el-col.el-col-12 > div > div > div.changeInput.el-input.el-input--suffix > input").clear()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(2) > div.el-col.el-col-12 > div > div > div.changeInput.el-input.el-input--suffix > input").send_keys(
            "350823200212080079")
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(3) > div:nth-child(1) > div > div > div > input").clear()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(3) > div:nth-child(1) > div > div > div > input").send_keys(
            "123456qq.com")

        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(4) > div:nth-child(1) > div > div > div > input").clear()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(4) > div:nth-child(1) > div > div > div > input").send_keys(
            "qwe")
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(4) > div:nth-child(2) > div > div > div > input").clear()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(4) > div:nth-child(2) > div > div > div > input").send_keys(
            "高级")
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(5) > div > div > div > div > input").clear()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(5) > div > div > div > div > input").send_keys(
            "fgdghj")
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(6) > div > div > div > div > input").clear()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(6) > div > div > div > div > input").send_keys(
            "12354s")
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__footer > div > button.el-button.confirm.el-button--primary > span").click()
        time.sleep(2)

    def test_11_Consultant11(self):
        driver = self.driver
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(1) > div:nth-child(1) > div > div > div > input").clear()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(1) > div:nth-child(1) > div > div > div > input").send_keys(
            "qwertr")
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(1) > div:nth-child(2) > div > div > div > input").clear()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(1) > div:nth-child(2) > div > div > div > input").send_keys(
            "18912345678")
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(2) > div.el-col.el-col-12 > div > div > div.changeInput.el-input.el-input--suffix > input").clear()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(2) > div.el-col.el-col-12 > div > div > div.changeInput.el-input.el-input--suffix > input").send_keys(
            "35082320021208007")
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(3) > div:nth-child(1) > div > div > div > input").clear()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(3) > div:nth-child(1) > div > div > div > input").send_keys(
            "123456@qq.com")

        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(4) > div:nth-child(1) > div > div > div > input").clear()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(4) > div:nth-child(1) > div > div > div > input").send_keys(
            "qwe")
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(4) > div:nth-child(2) > div > div > div > input").clear()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(4) > div:nth-child(2) > div > div > div > input").send_keys(
            "高级")
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(5) > div > div > div > div > input").clear()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(5) > div > div > div > div > input").send_keys(
            "fgdghj")
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(6) > div > div > div > div > input").clear()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(6) > div > div > div > div > input").send_keys(
            "12354s")
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__footer > div > button.el-button.confirm.el-button--primary > span").click()
        time.sleep(2)
    def test_12_Consultant12(self):
        driver = self.driver
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(1) > div:nth-child(1) > div > div > div > input").clear()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(1) > div:nth-child(1) > div > div > div > input").send_keys(
            "qwertr")
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(1) > div:nth-child(2) > div > div > div > input").clear()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(1) > div:nth-child(2) > div > div > div > input").send_keys(
            "18912345678")
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(2) > div.el-col.el-col-12 > div > div > div.changeInput.el-input.el-input--suffix > input").clear()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(2) > div.el-col.el-col-12 > div > div > div.changeInput.el-input.el-input--suffix > input").send_keys(
            "35082320021208007")
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(3) > div:nth-child(1) > div > div > div > input").clear()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(3) > div:nth-child(1) > div > div > div > input").send_keys(
            "123456@qq.com")

        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(4) > div:nth-child(1) > div > div > div > input").clear()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(4) > div:nth-child(1) > div > div > div > input").send_keys(
            "qwe")
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(4) > div:nth-child(2) > div > div > div > input").clear()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(4) > div:nth-child(2) > div > div > div > input").send_keys(
            "高级")
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(5) > div > div > div > div > input").clear()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(5) > div > div > div > div > input").send_keys(
            "fgdghj")
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(6) > div > div > div > div > input").clear()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(6) > div > div > div > div > input").send_keys(
            "1")
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__footer > div > button.el-button.confirm.el-button--primary > span").click()
        time.sleep(2)
    def test_13_Consultant13(self):
        driver = self.driver
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(1) > div:nth-child(1) > div > div > div > input").clear()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(1) > div:nth-child(1) > div > div > div > input").send_keys(
            "qwertr")
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(1) > div:nth-child(2) > div > div > div > input").clear()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(1) > div:nth-child(2) > div > div > div > input").send_keys(
            "18912345678")
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(2) > div.el-col.el-col-12 > div > div > div.changeInput.el-input.el-input--suffix > input").clear()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(2) > div.el-col.el-col-12 > div > div > div.changeInput.el-input.el-input--suffix > input").send_keys(
            "35082320021208007")
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(3) > div:nth-child(1) > div > div > div > input").clear()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(3) > div:nth-child(1) > div > div > div > input").send_keys(
            "aaaa@qq.com")

        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(4) > div:nth-child(1) > div > div > div > input").clear()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(4) > div:nth-child(1) > div > div > div > input").send_keys(
            "qwe")
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(4) > div:nth-child(2) > div > div > div > input").clear()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(4) > div:nth-child(2) > div > div > div > input").send_keys(
            "高级")
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(5) > div > div > div > div > input").clear()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(5) > div > div > div > div > input").send_keys(
            "fgdghj")
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(6) > div > div > div > div > input").clear()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(6) > div > div > div > div > input").send_keys(
            "12354s")
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__footer > div > button.el-button.confirm.el-button--primary > span").click()
        time.sleep(2)
    def test_14_Consultant14(self):
        driver = self.driver
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(1) > div:nth-child(1) > div > div > div > input").clear()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(1) > div:nth-child(1) > div > div > div > input").send_keys(
            "q")
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(1) > div:nth-child(2) > div > div > div > input").clear()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(1) > div:nth-child(2) > div > div > div > input").send_keys(
            "18912345678")
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(2) > div.el-col.el-col-12 > div > div > div.changeInput.el-input.el-input--suffix > input").clear()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(2) > div.el-col.el-col-12 > div > div > div.changeInput.el-input.el-input--suffix > input").send_keys(
            "35082320021208007")
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(3) > div:nth-child(1) > div > div > div > input").clear()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(3) > div:nth-child(1) > div > div > div > input").send_keys(
            "aaaa@qq.com")

        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(4) > div:nth-child(1) > div > div > div > input").clear()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(4) > div:nth-child(1) > div > div > div > input").send_keys(
            "qwe")
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(4) > div:nth-child(2) > div > div > div > input").clear()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(4) > div:nth-child(2) > div > div > div > input").send_keys(
            "高级")
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(5) > div > div > div > div > input").clear()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(5) > div > div > div > div > input").send_keys(
            "fgdghj")
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(6) > div > div > div > div > input").clear()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(6) > div > div > div > div > input").send_keys(
            "12354s")
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageConsultant > div:nth-child(3) > div > div.el-dialog__footer > div > button.el-button.confirm.el-button--primary > span").click()
        time.sleep(2)
    def test_12_QuitTest01r(self):
        driver = self.driver
        user_info_init = driver.find_element(By.CSS_SELECTOR,
                                             "#app > div > div.nav > span > span > div")
        ActionChains(driver).move_to_element(user_info_init).perform()
        sub_menu_ele = driver.find_element(By.CSS_SELECTOR,
                                           ".menuActionItem > span:nth-child(2)")
        sub_menu_ele.click()
        time.sleep(2)

    def test_13_QuitTest02e(self):
        driver = self.driver
        driver.quit()
