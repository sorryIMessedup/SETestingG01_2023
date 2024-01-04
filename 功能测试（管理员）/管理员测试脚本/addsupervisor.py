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


class TestSuccee(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(20)
        print('打开测试网站')
        cls.driver.get("https://sei-test.021hqit.com/group-1/#/login")

    def test_01_supervisor01(self):
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

        driver.find_element(By.CSS_SELECTOR, " #app > div > div.nav > div > ul > li:nth-child(6) > img").click()

        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div.el-row.is-align-bottom.el-row--flex > div.el-col.el-col-20 > button > span").click()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(1) > div:nth-child(1) > div > div > div > input").send_keys(
            "中文中人如")
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(1) > div:nth-child(2) > div > div > div > input").send_keys(
            "18912345678")
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(2) > div.el-col.el-col-12 > div > div > div.changeInput.el-input.el-input--suffix > input").send_keys(
            "350823200212080079")
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(3) > div:nth-child(1) > div > div > div > input").send_keys(
            "123456@qq.com")
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(3) > div:nth-child(2) > div > div > div > input").send_keys(
            "高级督导")
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(4) > div.searchSelect.el-col.el-col-12 > div > div > div > div > input").click()
        driver.find_element(By.CSS_SELECTOR,
                            "body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(1)").click()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(4) > div:nth-child(2) > div > div > div > input").send_keys(
            "123456")
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(6) > div > div > div > div > input").send_keys(
            "asdasdwwwddd")
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(7) > div > div > div > div > input").send_keys(
            "asdasd")

        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(5) > div > div > div > div.changeInput.el-input.el-input--suffix > input").send_keys(
            "华东师范大学")

        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div:nth-child(3) > div > div.el-dialog__footer > div > button.el-button.confirm.el-button--primary > span").click()
        time.sleep(5)
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.nav > div > ul > li.el-menu-item.is-active > img").click()
        time.sleep(2)

    def test_02_supervisor02(self):
        driver = self.driver

        driver.find_element(By.CSS_SELECTOR, "#app > div > div.nav > div > ul > li:nth-child(6) > img").click()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div.el-row.is-align-bottom.el-row--flex > div.el-col.el-col-20 > button > span").click()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(1) > div:nth-child(1) > div > div > div > input").send_keys(
            "中日日日日")
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(1) > div:nth-child(2) > div > div > div > input").send_keys(
            "18912345678")
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(2) > div.el-col.el-col-12 > div > div > div.changeInput.el-input.el-input--suffix > input").send_keys(
            "350823200212080079")
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(3) > div:nth-child(1) > div > div > div > input").send_keys(
            "123456@qq.com")
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(3) > div:nth-child(2) > div > div > div > input").send_keys(
            "高级督导")
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(4) > div.searchSelect.el-col.el-col-12 > div > div > div > div > input").click()
        driver.find_element(By.CSS_SELECTOR,
                            "body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(1)").click()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(4) > div:nth-child(2) > div > div > div > input").send_keys(
            "123456")
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(6) > div > div > div > div > input").send_keys(
            "asvbdswww")
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(7) > div > div > div > div > input").send_keys(
            "asdasd")

        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(5) > div > div > div > div.changeInput.el-input.el-input--suffix > input").send_keys(
            "华东师范大学")

        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div:nth-child(3) > div > div.el-dialog__footer > div > button.el-button.confirm.el-button--primary > span").click()
        time.sleep(5)
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.nav > div > ul > li.el-menu-item.is-active > img").click()
        time.sleep(2)

    def test_03_supervisor03(self):
        driver = self.driver

        driver.find_element(By.CSS_SELECTOR, "#app > div > div.nav > div > ul > li:nth-child(6) > img").click()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div.el-row.is-align-bottom.el-row--flex > div.el-col.el-col-20 > button > span").click()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(1) > div:nth-child(1) > div > div > div > input").send_keys(
            "中人七千万")
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(1) > div:nth-child(2) > div > div > div > input").send_keys(
            "18912345678")
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(2) > div.el-col.el-col-12 > div > div > div.changeInput.el-input.el-input--suffix > input").send_keys(
            "350823200212080079")
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(3) > div:nth-child(1) > div > div > div > input").send_keys(
            "123456@qq.com")
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(3) > div:nth-child(2) > div > div > div > input").send_keys(
            "高级督导")
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(4) > div.searchSelect.el-col.el-col-12 > div > div > div > div > input").click()
        driver.find_element(By.CSS_SELECTOR,
                            "body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(1)").click()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(4) > div:nth-child(2) > div > div > div > input").send_keys(
            "123456")
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(6) > div > div > div > div > input").send_keys(
            "asdasdssgfgfa")
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(7) > div > div > div > div > input").send_keys(
            "afgvassdd")

        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(5) > div > div > div > div.changeInput.el-input.el-input--suffix > input").send_keys(
            "华东师范大学")

        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div:nth-child(3) > div > div.el-dialog__footer > div > button.el-button.confirm.el-button--primary > span").click()
        time.sleep(5)
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.nav > div > ul > li.el-menu-item.is-active > img").click()

    def test_04_supervisor04(self):
        driver = self.driver

        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div.el-row.is-align-bottom.el-row--flex > div.el-col.el-col-20 > button > span").click()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(1) > div:nth-child(1) > div > div > div > input").send_keys(
            "中")
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(1) > div:nth-child(2) > div > div > div > input").send_keys(
            "18912345678")
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(2) > div.el-col.el-col-12 > div > div > div.changeInput.el-input.el-input--suffix > input").send_keys(
            "350823200212080079")
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(3) > div:nth-child(1) > div > div > div > input").send_keys(
            "123456@qq.com")
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(3) > div:nth-child(2) > div > div > div > input").send_keys(
            "高级督导")
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(4) > div.searchSelect.el-col.el-col-12 > div > div > div > div > input").click()
        driver.find_element(By.CSS_SELECTOR,
                            "body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(1)").click()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(4) > div:nth-child(2) > div > div > div > input").send_keys(
            "123456")
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(6) > div > div > div > div > input").send_keys(
            "asdasdssgfgfaaa")
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(7) > div > div > div > div > input").send_keys(
            "asdasd")

        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(5) > div > div > div > div.changeInput.el-input.el-input--suffix > input").send_keys(
            "华东师范大学")

        time.sleep(2)

    def test_05_supervisor05(self):
        driver = self.driver
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(1) > div:nth-child(1) > div > div > div > input").clear()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(1) > div:nth-child(1) > div > div > div > input").send_keys(
            "中@")
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(1) > div:nth-child(2) > div > div > div > input").clear()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(1) > div:nth-child(2) > div > div > div > input").send_keys(
            "18912345678")
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(2) > div.el-col.el-col-12 > div > div > div.changeInput.el-input.el-input--suffix > input").clear()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(2) > div.el-col.el-col-12 > div > div > div.changeInput.el-input.el-input--suffix > input").send_keys(
            "350823200212080079")
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(3) > div:nth-child(1) > div > div > div > input").clear()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(3) > div:nth-child(1) > div > div > div > input").send_keys(
            "123456@qq.com")
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(3) > div:nth-child(2) > div > div > div > input").clear()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(3) > div:nth-child(2) > div > div > div > input").send_keys(
            "高级督导")
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(4) > div.searchSelect.el-col.el-col-12 > div > div > div > div > input").click()
        driver.find_element(By.CSS_SELECTOR,
                            "body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(1)").click()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(4) > div:nth-child(2) > div > div > div > input").clear()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(4) > div:nth-child(2) > div > div > div > input").send_keys(
            "123456")
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(6) > div > div > div > div > input").clear()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(6) > div > div > div > div > input").send_keys(
            "asdasdssgfgfaaaaa")
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(7) > div > div > div > div > input").clear()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(7) > div > div > div > div > input").send_keys(
            "asdasd")
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(5) > div > div > div > div.changeInput.el-input.el-input--suffix > input").clear()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(5) > div > div > div > div.changeInput.el-input.el-input--suffix > input").send_keys(
            "华东师范大学")

        time.sleep(2)

    def test_06_supervisor06(self):
        driver = self.driver
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(1) > div:nth-child(1) > div > div > div > input").clear()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(1) > div:nth-child(1) > div > div > div > input").send_keys(
            "中#")
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(1) > div:nth-child(2) > div > div > div > input").clear()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(1) > div:nth-child(2) > div > div > div > input").send_keys(
            "18912345678")
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(2) > div.el-col.el-col-12 > div > div > div.changeInput.el-input.el-input--suffix > input").clear()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(2) > div.el-col.el-col-12 > div > div > div.changeInput.el-input.el-input--suffix > input").send_keys(
            "350823200212080079")
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(3) > div:nth-child(1) > div > div > div > input").clear()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(3) > div:nth-child(1) > div > div > div > input").send_keys(
            "123456@qq.com")
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(3) > div:nth-child(2) > div > div > div > input").clear()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(3) > div:nth-child(2) > div > div > div > input").send_keys(
            "高级督导")
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(4) > div.searchSelect.el-col.el-col-12 > div > div > div > div > input").click()
        driver.find_element(By.CSS_SELECTOR,
                            "body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(1)").click()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(4) > div:nth-child(2) > div > div > div > input").clear()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(4) > div:nth-child(2) > div > div > div > input").send_keys(
            "123456")
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(6) > div > div > div > div > input").clear()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(6) > div > div > div > div > input").send_keys(
            "asdasdssgfgfaaaaa")
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(7) > div > div > div > div > input").clear()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(7) > div > div > div > div > input").send_keys(
            "asdasd")
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(5) > div > div > div > div.changeInput.el-input.el-input--suffix > input").clear()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(5) > div > div > div > div.changeInput.el-input.el-input--suffix > input").send_keys(
            "华东师范大学")

    def test_07_supervisor07(self):
        driver = self.driver
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(1) > div:nth-child(1) > div > div > div > input").clear()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(1) > div:nth-child(1) > div > div > div > input").send_keys(
            "中人")
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(1) > div:nth-child(2) > div > div > div > input").clear()

        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(2) > div.el-col.el-col-12 > div > div > div.changeInput.el-input.el-input--suffix > input").clear()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(2) > div.el-col.el-col-12 > div > div > div.changeInput.el-input.el-input--suffix > input").send_keys(
            "350823200212080079")
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(3) > div:nth-child(1) > div > div > div > input").clear()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(3) > div:nth-child(1) > div > div > div > input").send_keys(
            "123456@qq.com")
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(3) > div:nth-child(2) > div > div > div > input").clear()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(3) > div:nth-child(2) > div > div > div > input").send_keys(
            "高级督导")
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(4) > div.searchSelect.el-col.el-col-12 > div > div > div > div > input").click()
        driver.find_element(By.CSS_SELECTOR,
                            "body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(1)").click()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(4) > div:nth-child(2) > div > div > div > input").clear()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(4) > div:nth-child(2) > div > div > div > input").send_keys(
            "123456")
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(6) > div > div > div > div > input").clear()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(6) > div > div > div > div > input").send_keys(
            "asdasdssgfgfaaaaa")
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(7) > div > div > div > div > input").clear()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(7) > div > div > div > div > input").send_keys(
            "asdasd")
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(5) > div > div > div > div.changeInput.el-input.el-input--suffix > input").clear()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(5) > div > div > div > div.changeInput.el-input.el-input--suffix > input").send_keys(
            "华东师范大学")

        time.sleep(2)

    def test_08_supervisor08(self):
        driver = self.driver
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(1) > div:nth-child(1) > div > div > div > input").clear()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(1) > div:nth-child(1) > div > div > div > input").send_keys(
            "中种子")
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(1) > div:nth-child(2) > div > div > div > input").clear()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(1) > div:nth-child(2) > div > div > div > input").send_keys(
            "18912345678")
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(2) > div.el-col.el-col-12 > div > div > div.changeInput.el-input.el-input--suffix > input").clear()

        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(3) > div:nth-child(1) > div > div > div > input").clear()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(3) > div:nth-child(1) > div > div > div > input").send_keys(
            "123456@qq.com")
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(3) > div:nth-child(2) > div > div > div > input").clear()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(3) > div:nth-child(2) > div > div > div > input").send_keys(
            "高级督导")
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(4) > div.searchSelect.el-col.el-col-12 > div > div > div > div > input").click()
        driver.find_element(By.CSS_SELECTOR,
                            "body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(1)").click()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(4) > div:nth-child(2) > div > div > div > input").clear()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(4) > div:nth-child(2) > div > div > div > input").send_keys(
            "123456")
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(6) > div > div > div > div > input").clear()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(6) > div > div > div > div > input").send_keys(
            "asdasdssgfgfaaaaa")
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(7) > div > div > div > div > input").clear()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(7) > div > div > div > div > input").send_keys(
            "asdasd")
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(5) > div > div > div > div.changeInput.el-input.el-input--suffix > input").clear()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(5) > div > div > div > div.changeInput.el-input.el-input--suffix > input").send_keys(
            "华东师范大学")

    def test_09_supervisor09(self):
        driver = self.driver
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(1) > div:nth-child(1) > div > div > div > input").clear()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(1) > div:nth-child(1) > div > div > div > input").send_keys(
            "中中撒")
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(1) > div:nth-child(2) > div > div > div > input").clear()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(1) > div:nth-child(2) > div > div > div > input").send_keys(
            "18912345678")
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(2) > div.el-col.el-col-12 > div > div > div.changeInput.el-input.el-input--suffix > input").clear()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(2) > div.el-col.el-col-12 > div > div > div.changeInput.el-input.el-input--suffix > input").send_keys(
            "3508232002120800793")
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(3) > div:nth-child(1) > div > div > div > input").clear()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(3) > div:nth-child(1) > div > div > div > input").send_keys(
            "123456@qq.com")
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(3) > div:nth-child(2) > div > div > div > input").clear()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(3) > div:nth-child(2) > div > div > div > input").send_keys(
            "高级督导")
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(4) > div.searchSelect.el-col.el-col-12 > div > div > div > div > input").click()
        driver.find_element(By.CSS_SELECTOR,
                            "body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(1)").click()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(4) > div:nth-child(2) > div > div > div > input").clear()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(4) > div:nth-child(2) > div > div > div > input").send_keys(
            "123456")
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(6) > div > div > div > div > input").clear()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(6) > div > div > div > div > input").send_keys(
            "asdasdssgfgfaaaaa")
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(7) > div > div > div > div > input").clear()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(7) > div > div > div > div > input").send_keys(
            "asdasd")
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(5) > div > div > div > div.changeInput.el-input.el-input--suffix > input").clear()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(5) > div > div > div > div.changeInput.el-input.el-input--suffix > input").send_keys(
            "华东师范大学")

        time.sleep(2)

    def test_10_supervisor10(self):
        driver = self.driver
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(1) > div:nth-child(1) > div > div > div > input").clear()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(1) > div:nth-child(1) > div > div > div > input").send_keys(
            "中周大生")
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(1) > div:nth-child(2) > div > div > div > input").clear()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(1) > div:nth-child(2) > div > div > div > input").send_keys(
            "18912345678")
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(2) > div.el-col.el-col-12 > div > div > div.changeInput.el-input.el-input--suffix > input").clear()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(2) > div.el-col.el-col-12 > div > div > div.changeInput.el-input.el-input--suffix > input").send_keys(
            "350823200212080079")
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(3) > div:nth-child(1) > div > div > div > input").clear()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(3) > div:nth-child(1) > div > div > div > input").send_keys(
            "12335124qq.com")
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(3) > div:nth-child(2) > div > div > div > input").clear()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(3) > div:nth-child(2) > div > div > div > input").send_keys(
            "高级督导")
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(4) > div.searchSelect.el-col.el-col-12 > div > div > div > div > input").click()
        driver.find_element(By.CSS_SELECTOR,
                            "body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(1)").click()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(4) > div:nth-child(2) > div > div > div > input").clear()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(4) > div:nth-child(2) > div > div > div > input").send_keys(
            "123456")
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(6) > div > div > div > div > input").clear()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(6) > div > div > div > div > input").send_keys(
            "asdasdssgfgfaaaaa")
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(7) > div > div > div > div > input").clear()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(7) > div > div > div > div > input").send_keys(
            "asdasd")
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(5) > div > div > div > div.changeInput.el-input.el-input--suffix > input").clear()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(5) > div > div > div > div.changeInput.el-input.el-input--suffix > input").send_keys(
            "华东师范大学")

        time.sleep(2)

    def test_11_supervisor11(self):
        driver = self.driver
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(1) > div:nth-child(1) > div > div > div > input").clear()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(1) > div:nth-child(1) > div > div > div > input").send_keys(
            "中我去饿")
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(1) > div:nth-child(2) > div > div > div > input").clear()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(1) > div:nth-child(2) > div > div > div > input").send_keys(
            "18912345678")
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(2) > div.el-col.el-col-12 > div > div > div.changeInput.el-input.el-input--suffix > input").clear()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(2) > div.el-col.el-col-12 > div > div > div.changeInput.el-input.el-input--suffix > input").send_keys(
            "350823200212080079")
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(3) > div:nth-child(1) > div > div > div > input").clear()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(3) > div:nth-child(1) > div > div > div > input").send_keys(
            "123456@qq.com")
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(3) > div:nth-child(2) > div > div > div > input").clear()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(3) > div:nth-child(2) > div > div > div > input").send_keys(
            "高级督导")
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(4) > div.searchSelect.el-col.el-col-12 > div > div > div > div > input").click()
        driver.find_element(By.CSS_SELECTOR,
                            "body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(1)").click()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(4) > div:nth-child(2) > div > div > div > input").clear()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(4) > div:nth-child(2) > div > div > div > input").send_keys(
            "123456")
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(6) > div > div > div > div > input").clear()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(6) > div > div > div > div > input").send_keys(
            "asdasdssgfgfaaaaa")
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(7) > div > div > div > div > input").clear()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(7) > div > div > div > div > input").send_keys(
            "asdasd@")
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(5) > div > div > div > div.changeInput.el-input.el-input--suffix > input").clear()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(5) > div > div > div > div.changeInput.el-input.el-input--suffix > input").send_keys(
            "华东师范大学")

        time.sleep(2)

    def test_12_supervisor12(self):
        driver = self.driver
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(1) > div:nth-child(1) > div > div > div > input").clear()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(1) > div:nth-child(1) > div > div > div > input").send_keys(
            "中请为")
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(1) > div:nth-child(2) > div > div > div > input").clear()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(1) > div:nth-child(2) > div > div > div > input").send_keys(
            "18912345678")
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(2) > div.el-col.el-col-12 > div > div > div.changeInput.el-input.el-input--suffix > input").clear()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(2) > div.el-col.el-col-12 > div > div > div.changeInput.el-input.el-input--suffix > input").send_keys(
            "350823200212080079")
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(3) > div:nth-child(1) > div > div > div > input").clear()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(3) > div:nth-child(1) > div > div > div > input").send_keys(
            "123456@qq.com")
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(3) > div:nth-child(2) > div > div > div > input").clear()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(3) > div:nth-child(2) > div > div > div > input").send_keys(
            "高级督导")
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(4) > div.searchSelect.el-col.el-col-12 > div > div > div > div > input").click()
        driver.find_element(By.CSS_SELECTOR,
                            "body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(1)").click()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(4) > div:nth-child(2) > div > div > div > input").clear()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(4) > div:nth-child(2) > div > div > div > input").send_keys(
            "123456")
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(6) > div > div > div > div > input").clear()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(6) > div > div > div > div > input").send_keys(
            "asdasdssgfgfa@")
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(7) > div > div > div > div > input").clear()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(7) > div > div > div > div > input").send_keys(
            "asdasd")

        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(5) > div > div > div > div.changeInput.el-input.el-input--suffix > input").send_keys(
            "华东师范大学")

        time.sleep(2)

    def test_13_supervisor13(self):
        driver = self.driver
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(1) > div:nth-child(1) > div > div > div > input").clear()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(1) > div:nth-child(1) > div > div > div > input").send_keys(
            "中请为as")
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(1) > div:nth-child(2) > div > div > div > input").clear()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(1) > div:nth-child(2) > div > div > div > input").send_keys(
            "18912345678")
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(2) > div.el-col.el-col-12 > div > div > div.changeInput.el-input.el-input--suffix > input").clear()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(2) > div.el-col.el-col-12 > div > div > div.changeInput.el-input.el-input--suffix > input").send_keys(
            "350823200212080079")
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(3) > div:nth-child(1) > div > div > div > input").clear()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(3) > div:nth-child(1) > div > div > div > input").send_keys(
            "123456@qq.com")
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(3) > div:nth-child(2) > div > div > div > input").clear()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(3) > div:nth-child(2) > div > div > div > input").send_keys(
            "高级督导")
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(4) > div.searchSelect.el-col.el-col-12 > div > div > div > div > input").click()
        driver.find_element(By.CSS_SELECTOR,
                            "body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(1)").click()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(4) > div:nth-child(2) > div > div > div > input").clear()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(4) > div:nth-child(2) > div > div > div > input").send_keys(
            "123456")
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(6) > div > div > div > div > input").clear()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(6) > div > div > div > div > input").send_keys(
            "asdasdssgfgfa")
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(7) > div > div > div > div > input").clear()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(7) > div > div > div > div > input").send_keys(
            "asdasd")
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(5) > div > div > div > div.changeInput.el-input.el-input--suffix > input").clear()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(5) > div > div > div > div.changeInput.el-input.el-input--suffix > input").send_keys(
            "华东师范大学")

        time.sleep(2)

    def test_14_supervisor14(self):
        driver = self.driver
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(1) > div:nth-child(1) > div > div > div > input").clear()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(1) > div:nth-child(1) > div > div > div > input").send_keys(
            "中请为")
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(1) > div:nth-child(2) > div > div > div > input").clear()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(1) > div:nth-child(2) > div > div > div > input").send_keys(
            "18912345678")
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(2) > div.el-col.el-col-12 > div > div > div.changeInput.el-input.el-input--suffix > input").clear()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(2) > div.el-col.el-col-12 > div > div > div.changeInput.el-input.el-input--suffix > input").send_keys(
            "350823200212080079")
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(3) > div:nth-child(1) > div > div > div > input").clear()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(3) > div:nth-child(1) > div > div > div > input").send_keys(
            "123456@qq.com")
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(3) > div:nth-child(2) > div > div > div > input").clear()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(3) > div:nth-child(2) > div > div > div > input").send_keys(
            "高级督导")
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(4) > div.searchSelect.el-col.el-col-12 > div > div > div > div > input").click()
        driver.find_element(By.CSS_SELECTOR,
                            "body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(1)").click()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(4) > div:nth-child(2) > div > div > div > input").clear()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(4) > div:nth-child(2) > div > div > div > input").send_keys(
            "123456")
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(6) > div > div > div > div > input").clear()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(6) > div > div > div > div > input").send_keys(
            "asdasdssgfgfa")
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(7) > div > div > div > div > input").clear()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(7) > div > div > div > div > input").send_keys(
            "123456789012345678901")
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(5) > div > div > div > div.changeInput.el-input.el-input--suffix > input").clear()
        driver.find_element(By.CSS_SELECTOR,
                            "#app > div > div.content > div.manageSupervisor > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(5) > div > div > div > div.changeInput.el-input.el-input--suffix > input").send_keys(
            "华东师范大学")

        time.sleep(2)

    def test_13_QuitTest01(self):
        driver = self.driver
        user_info_init = driver.find_element(By.CSS_SELECTOR,
                                             "#app > div > div.nav > span > span > div")
        ActionChains(driver).move_to_element(user_info_init).perform()
        sub_menu_ele = driver.find_element(By.CSS_SELECTOR,
                                           ".menuActionItem > span:nth-child(2)")
        sub_menu_ele.click()
        time.sleep(2)

    def test_14_QuitTest02(self):
        driver = self.driver
        driver.quit()
