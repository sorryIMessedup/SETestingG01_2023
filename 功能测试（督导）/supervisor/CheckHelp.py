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

    def test_01_查询求助对话测试01(self):
        driver = self.driver
        print('查询求助对话01')
        x = '//*[@id="app"]/div/div[1]/div/ul/li[1]/span'
        driver.find_element_by_xpath(x).click()
        time.sleep(2)
        x = '//*[@id="app"]/div/div[1]/div/ul/li[4]/span'
        driver.find_element_by_xpath(x).click()
        time.sleep(2)

        # 搜索求助者'yoyi'
        x = '//*[@id="app"]/div/div[2]/div[2]/div/div[1]/div[1]/div/input'
        driver.find_element_by_xpath(x).clear()
        driver.find_element_by_xpath(x).send_keys("yoyi")
        driver.find_element_by_xpath(x).send_keys(Keys.ENTER)
        time.sleep(5)

    def test_02_查询求助对话测试02(self):
        # 搜索不存在咨询师求助
        driver = self.driver
        print('查询求助对话02')
        x = '//*[@id="app"]/div/div[1]/div/ul/li[1]/span'
        driver.find_element_by_xpath(x).click()
        time.sleep(2)
        x = '//*[@id="app"]/div/div[1]/div/ul/li[4]/span'
        driver.find_element_by_xpath(x).click()
        time.sleep(2)

        # 搜索求助者'yoyyyi'
        x = '//*[@id="app"]/div/div[2]/div[2]/div/div[1]/div[1]/div/input'
        driver.find_element_by_xpath(x).clear()
        driver.find_element_by_xpath(x).send_keys("yoyyyi")
        driver.find_element_by_xpath(x).send_keys(Keys.ENTER)
        time.sleep(5)

    def test_03_查询求助对话测试03_1(self):
        # 切换单页记录数
        driver = self.driver
        print('查询求助对话测试03_1')
        x = '//*[@id="app"]/div/div[1]/div/ul/li[1]/span'
        driver.find_element_by_xpath(x).click()
        time.sleep(2)
        x = '//*[@id="app"]/div/div[1]/div/ul/li[4]/span'
        driver.find_element_by_xpath(x).click()
        time.sleep(2)
        x = '//*[@id="app"]/div/div[2]/div[2]/div/div[3]/div[2]/slot/div/div/div[1]/input'

        driver.find_element_by_xpath(x).click()
        time.sleep(2)
        # 选择一页20条记录
        driver.find_element_by_xpath("//ul[@class='el-scrollbar__view el-select-dropdown__list']/li[2]").click()

        time.sleep(2)

    def test_04_查询求助对话测试03_2(self):
        # 切换单页记录数
        driver = self.driver
        print('查询求助对话测试03_2')
        x = '//*[@id="app"]/div/div[1]/div/ul/li[1]/span'
        driver.find_element_by_xpath(x).click()
        time.sleep(2)
        x = '//*[@id="app"]/div/div[1]/div/ul/li[4]/span'
        driver.find_element_by_xpath(x).click()
        time.sleep(2)
        x = '//*[@id="app"]/div/div[2]/div[2]/div/div[3]/div[2]/slot/div/div/div[1]/input'

        driver.find_element_by_xpath(x).click()
        time.sleep(2)
        # 选择一页30条记录
        driver.find_element_by_xpath("//ul[@class='el-scrollbar__view el-select-dropdown__list']/li[3]").click()

        time.sleep(2)

    def test_05_查询求助对话测试03_3(self):
        # 切换单页记录数
        driver = self.driver
        print('查询求助对话测试03_3')
        x = '//*[@id="app"]/div/div[1]/div/ul/li[1]/span'
        driver.find_element_by_xpath(x).click()
        time.sleep(2)
        x = '//*[@id="app"]/div/div[1]/div/ul/li[4]/span'
        driver.find_element_by_xpath(x).click()
        time.sleep(2)
        x = '//*[@id="app"]/div/div[2]/div[2]/div/div[3]/div[2]/slot/div/div/div[1]/input'

        driver.find_element_by_xpath(x).click()
        time.sleep(2)
        # 选择一页40条记录
        driver.find_element_by_xpath("//ul[@class='el-scrollbar__view el-select-dropdown__list']/li[4]").click()

        time.sleep(2)

    def test_06_查询求助对话测试04_1(self):
        # 切换单页记录数
        driver = self.driver
        print('查询求助对话测试04_1')
        x = '//*[@id="app"]/div/div[1]/div/ul/li[1]/span'
        driver.find_element_by_xpath(x).click()
        time.sleep(2)
        x = '//*[@id="app"]/div/div[1]/div/ul/li[4]/span'
        driver.find_element_by_xpath(x).click()
        time.sleep(2)
        x = '//*[@id="app"]/div/div[2]/div[2]/div/div[3]/div[2]/slot/div/div/div[1]/input'

        driver.find_element_by_xpath(x).click()
        time.sleep(2)
        # 选择一页50条记录
        driver.find_element_by_xpath("//ul[@class='el-scrollbar__view el-select-dropdown__list']/li[5]").click()

        time.sleep(2)

    def test_07_查询求助对话测试04_2(self):
        # 切换单页记录数
        driver = self.driver
        print('查询求助对话测试04_2')
        x = '//*[@id="app"]/div/div[1]/div/ul/li[1]/span'
        driver.find_element_by_xpath(x).click()
        time.sleep(2)
        x = '//*[@id="app"]/div/div[1]/div/ul/li[4]/span'
        driver.find_element_by_xpath(x).click()
        time.sleep(2)
        x = '//*[@id="app"]/div/div[2]/div[2]/div/div[3]/div[2]/slot/div/div/div[1]/input'

        driver.find_element_by_xpath(x).click()
        time.sleep(2)
        # 选择一页60条记录
        driver.find_element_by_xpath("//ul[@class='el-scrollbar__view el-select-dropdown__list']/li[6]").click()

        time.sleep(2)

    def test_08_查询求助对话测试05(self):
        # 搜索具体咨询师+具体日期范围的存在对话
        driver = self.driver
        print('查询求助对话05')
        x = '//*[@id="app"]/div/div[1]/div/ul/li[1]/span'
        driver.find_element_by_xpath(x).click()
        time.sleep(2)
        x = '//*[@id="app"]/div/div[1]/div/ul/li[4]/span'
        driver.find_element_by_xpath(x).click()
        time.sleep(2)
        # 搜索求助者'yoyyyi'
        x = '//*[@id="app"]/div/div[2]/div[2]/div/div[1]/div[1]/div/input'
        driver.find_element_by_xpath(x).clear()
        driver.find_element_by_xpath(x).send_keys("yoyyyi")

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
        time.sleep(5)

    def test_09_查询求助对话测试06(self):
        # 不搜索具体咨询师+具体日期范围的存在对话
        driver = self.driver
        print('查询求助对话06')
        x = '//*[@id="app"]/div/div[1]/div/ul/li[1]/span'
        driver.find_element_by_xpath(x).click()
        time.sleep(2)
        x = '//*[@id="app"]/div/div[1]/div/ul/li[4]/span'
        driver.find_element_by_xpath(x).click()
        time.sleep(2)

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
        time.sleep(5)

    def test_09_查询求助对话测试06(self):
        # 不搜索具体咨询师+具体日期范围的存在对话
        driver = self.driver
        print('查询求助对话06')
        x = '//*[@id="app"]/div/div[1]/div/ul/li[1]/span'
        driver.find_element_by_xpath(x).click()
        time.sleep(2)
        x = '//*[@id="app"]/div/div[1]/div/ul/li[4]/span'
        driver.find_element_by_xpath(x).click()
        time.sleep(2)

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
        time.sleep(5)

    def test_10_查询求助对话测试07(self):
        # 测试灰色按钮功能
        driver = self.driver
        print('查询求助对话10')
        x = '//*[@id="app"]/div/div[1]/div/ul/li[1]/span'
        driver.find_element_by_xpath(x).click()
        time.sleep(2)
        x = '//*[@id="app"]/div/div[1]/div/ul/li[4]/span'
        driver.find_element_by_xpath(x).click()
        time.sleep(2)

        x = '//*[@id="app"]/div/div[2]/div[2]/div/div[1]/div[2]/div/input[1]'
        driver.find_element_by_xpath(x).click()
        time.sleep(5)
        # 定位12月1日旁边的12月30日会跳转到11月30日
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

    def test_11_查询求助对话测试08(self):
        # 测试灰色按钮功能
        driver = self.driver
        print('查询求助对08')
        x = '//*[@id="app"]/div/div[1]/div/ul/li[1]/span'
        driver.find_element_by_xpath(x).click()
        time.sleep(2)
        x = '//*[@id="app"]/div/div[1]/div/ul/li[4]/span'
        driver.find_element_by_xpath(x).click()
        time.sleep(2)
        # 测试日历1月最后一行的5号是否跳转 会跳转
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

    def test_12_查询求助对话测试09(self):
        driver = self.driver
        print('查询求助对话09')
        # 查询右选月份按钮
        x = '//*[@id="app"]/div/div[1]/div/ul/li[1]/span'
        driver.find_element_by_xpath(x).click()
        time.sleep(2)
        x = '//*[@id="app"]/div/div[1]/div/ul/li[4]/span'
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

    def test_13_查询求助对话测试10(self):
        driver = self.driver
        print('查询求助对话10')
        # 查询左选月份按钮
        x = '//*[@id="app"]/div/div[1]/div/ul/li[1]/span'
        driver.find_element_by_xpath(x).click()
        time.sleep(2)
        x = '//*[@id="app"]/div/div[1]/div/ul/li[4]/span'
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

    def test_14_查询求助对话测试11(self):
        driver = self.driver
        print('查询求助对话11')
        # 查询跨好几个月选择记录
        x = '//*[@id="app"]/div/div[1]/div/ul/li[1]/span'
        driver.find_element_by_xpath(x).click()
        time.sleep(2)
        x = '//*[@id="app"]/div/div[1]/div/ul/li[4]/span'
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
        time.sleep(2)
        # 选择12月15日
        end = '/html/body/div[last()]/div[1]/div/div[3]/table/tbody/tr[4]/td[4]/div/span'
        driver.find_element_by_xpath(end).click()
        time.sleep(2)
        certain = '/html/body/div[last()]/div[2]/button[2]/span'
        driver.find_element_by_xpath(certain).click()
        time.sleep(5)

    def test_ZZ_退出(self):
        driver = self.driver
        driver.quit()
