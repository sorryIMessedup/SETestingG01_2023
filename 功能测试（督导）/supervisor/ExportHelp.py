import os
import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class MyTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome("D:\chromedriver-win64\chromedriver.exe")
        self.driver.implicitly_wait(20)
        options = webdriver.ChromeOptions()
        prefs = {'profile.default_content_settings.popups': 0,
                 'download.default_directory': r'C:\Users\tancheng\Desktop\hotline'}
        options.add_experimental_option('prefs', prefs)
        self.driver = webdriver.Chrome(chrome_options=options)
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

    def test_01_导出求助对话测试01(self):
        ##直接导出第一条测试
        driver = self.driver
        print('导出求助对话01')
        x = '//*[@id="app"]/div/div[1]/div/ul/li[4]/span'
        driver.find_element_by_xpath(x).click()
        time.sleep(2)
        # 选择第一条求助对话

        x = '//*[@id="app"]/div/div[2]/div[2]/div/div[2]/div[3]/table/tbody/tr[1]/td[6]/div/div/button[1]/span'
        check_first_consult = driver.find_element_by_xpath(x)
        check_first_consult.click()
        time.sleep(5)

        x = '//*[@id="app"]/div/div[2]/div[2]/div/div[1]/div[1]/div[3]/div[1]'
        export_single_consult_talk = driver.find_element_by_xpath(x)
        export_single_consult_talk.click()
        time.sleep(2)
        certain = driver.find_element_by_css_selector(
            "body > div.el-message-box__wrapper > div > div.el-message-box__btns > button.el-button.el-button--default.el-button--small.el-button--primary > span")
        certain.click()
        time.sleep(5)
        now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
        os.chdir(r'D:\大三上\软件测试项目\dudao\下载')
        time.sleep(5)
        files = filter(os.path.isfile, os.listdir(r'D:\大三上\软件测试项目\dudao\下载'))
        files = [os.path.join(r'D:\大三上\软件测试项目\dudao\下载', f) for f in files]  # add path to each file
        files.sort(key=lambda x: os.path.getmtime(x))
        newest_file = files[-1]
        os.rename(newest_file, "ExportHelpTest01" + now + ".txt")

    def test_02_导出求助对话测试02(self):
        ##搜索咨询师'yoyi'导出第一条测试
        driver = self.driver
        print('导出求助对话02')
        x = '//*[@id="app"]/div/div[1]/div/ul/li[1]/span'
        driver.find_element_by_xpath(x).click()
        time.sleep(2)
        x = '//*[@id="app"]/div/div[1]/div/ul/li[4]/span'
        driver.find_element_by_xpath(x).click()
        time.sleep(2)
        driver.find_element_by_css_selector(
            "#app > div > div.content > div.consultRecord > div > div.el-row.is-align-bottom.el-row--flex > div:nth-child(1) > div > input").clear()
        driver.find_element_by_css_selector(
            "#app > div > div.content > div.consultRecord > div > div.el-row.is-align-bottom.el-row--flex > div:nth-child(1) > div > input").send_keys(
            "yoyi")
        driver.find_element_by_css_selector(
            "#app > div > div.content > div.consultRecord > div > div.el-row.is-align-bottom.el-row--flex > div:nth-child(1) > div > input").send_keys(
            Keys.ENTER)
        time.sleep(5)
        # 选择第一条咨询对话
        x = '//*[@id="app"]/div/div[2]/div[2]/div/div[2]/div[3]/table/tbody/tr[1]/td[6]/div/div/button[1]/span'
        check_first_consult = driver.find_element_by_xpath(x)
        check_first_consult.click()
        time.sleep(5)
        x = '//*[@id="app"]/div/div[2]/div[2]/div/div[1]/div[1]/div[3]/div[1]'
        export_single_consult_talk = driver.find_element_by_xpath(x)
        export_single_consult_talk.click()
        time.sleep(2)
        certain = driver.find_element_by_css_selector(
            "body > div.el-message-box__wrapper > div > div.el-message-box__btns > button.el-button.el-button--default.el-button--small.el-button--primary > span")
        certain.click()
        time.sleep(5)
        now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
        os.chdir(r'D:\大三上\软件测试项目\dudao\下载')
        time.sleep(5)
        files = filter(os.path.isfile, os.listdir(r'D:\大三上\软件测试项目\dudao\下载'))
        files = [os.path.join(r'D:\大三上\软件测试项目\dudao\下载', f) for f in files]  # add path to each file
        files.sort(key=lambda x: os.path.getmtime(x))
        newest_file = files[-1]
        os.rename(newest_file, "ExportHelpTest02" + now + ".txt")

    def test_03_导出求助对话测试03(self):
        ##搜索不存在的咨询者是否能导出对话
        # 看来导不出
        driver = self.driver
        print('导出求助对话03')
        x = '//*[@id="app"]/div/div[1]/div/ul/li[1]/span'
        driver.find_element_by_xpath(x).click()
        time.sleep(2)
        x = '//*[@id="app"]/div/div[1]/div/ul/li[4]/span'
        driver.find_element_by_xpath(x).click()
        time.sleep(2)
        driver.find_element_by_css_selector(
            "#app > div > div.content > div.consultRecord > div > div.el-row.is-align-bottom.el-row--flex > div:nth-child(1) > div > input").clear()
        driver.find_element_by_css_selector(
            "#app > div > div.content > div.consultRecord > div > div.el-row.is-align-bottom.el-row--flex > div:nth-child(1) > div > input").send_keys(
            "莫小贝")
        driver.find_element_by_css_selector(
            "#app > div > div.content > div.consultRecord > div > div.el-row.is-align-bottom.el-row--flex > div:nth-child(1) > div > input").send_keys(
            Keys.ENTER)
        time.sleep(5)

    def test_04_导出求助对话测试04(self):
        ##测试批量导出
        ##在没有任何选择的情况下导出报错
        driver = self.driver
        print('导出求助对话04')
        x = '//*[@id="app"]/div/div[1]/div/ul/li[1]/span'
        driver.find_element_by_xpath(x).click()
        time.sleep(2)
        x = '//*[@id="app"]/div/div[1]/div/ul/li[4]/span'
        driver.find_element_by_xpath(x).click()
        time.sleep(2)
        driver.find_element_by_css_selector(
            "#app > div > div.content > div.consultRecord > div > div.el-row.is-align-bottom.el-row--flex > div.el-col.el-col-16 > button").click()
        time.sleep(2)
        x = '/html/body/div[last()]'
        warn = driver.find_element_by_xpath(x)
        res = warn.text
        print(res)

    def test_05_导出咨询对话测试05(self):
        ##测试批量导出
        ##在选择前2个对话时仍然导出报错！！！！！！！！！
        driver = self.driver
        print('导出咨询对话05')
        x = '//*[@id="app"]/div/div[1]/div/ul/li[1]/span'
        driver.find_element_by_xpath(x).click()
        time.sleep(2)
        x = '//*[@id="app"]/div/div[1]/div/ul/li[4]/span'
        driver.find_element_by_xpath(x).click()
        time.sleep(2)

        x = '//*[@id="app"]/div/div[2]/div[2]/div/div[2]/div[3]/table/tbody/tr/td[1]/div/label/span'
        driver.find_element_by_xpath(x).click()
        time.sleep(2)
        x = '//*[@id="app"]/div/div[2]/div[2]/div/div[2]/div[3]/table/tbody/tr[2]/td[1]/div/label/span'
        driver.find_element_by_xpath(x).click()
        time.sleep(2)
        driver.find_element_by_css_selector(
            "#app > div > div.content > div.consultRecord > div > div.el-row.is-align-bottom.el-row--flex > div.el-col.el-col-16 > button").click()
        time.sleep(2)
        driver.find_element_by_css_selector(
            "body > div.el-message-box__wrapper > div > div.el-message-box__btns > button.el-button.el-button--default.el-button--small.el-button--primary").click()
        time.sleep(2)
        x = '/html/body/div[last()]'
        warn = driver.find_element_by_xpath(x)
        res = warn.text
        print(res)

        time.sleep(5)

    def test_06_导出求助对话测试06(self):
        ##测试批量导出
        ##在选择前1个对话时仍然导出报错！！！！！！！！！
        driver = self.driver
        print('导出求助对话06')
        x = '//*[@id="app"]/div/div[1]/div/ul/li[1]/span'
        driver.find_element_by_xpath(x).click()
        time.sleep(2)
        x = '//*[@id="app"]/div/div[1]/div/ul/li[4]/span'
        driver.find_element_by_xpath(x).click()
        time.sleep(2)

        x = '//*[@id="app"]/div/div[2]/div[2]/div/div[2]/div[3]/table/tbody/tr/td[1]/div/label/span'
        driver.find_element_by_xpath(x).click()
        time.sleep(2)
        driver.find_element_by_css_selector(
            "#app > div > div.content > div.consultRecord > div > div.el-row.is-align-bottom.el-row--flex > div.el-col.el-col-16 > button").click()
        time.sleep(2)
        driver.find_element_by_css_selector(
            "body > div.el-message-box__wrapper > div > div.el-message-box__btns > button.el-button.el-button--default.el-button--small.el-button--primary").click()
        time.sleep(2)
        x = '/html/body/div[last()]'
        warn = driver.find_element_by_xpath(x)
        res = warn.text
        print(res)

        time.sleep(5)

    def test_ZZ_退出(self):
        driver = self.driver
        driver.quit()
