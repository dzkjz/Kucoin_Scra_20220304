import random
import time
from typing import List

from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.utils import ChromeType
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import *

import adReported
import randomize_user_agent
import saver


class crawler:

    def __init__(self, path, lang=None):
        """可以设置国家 设置格式 en-US"""
        self.__driver__ = None
        self.__driver_options__ = webdriver.ChromeOptions()
        self.__lang_list__ = ['ar-AE',
                              'ar-EG',
                              'ca-ES',
                              'cy-GB',
                              'da-DK',
                              'de-AT',
                              'de-CH',
                              'de-DE',
                              'de-LU',
                              'en-AU',
                              'en-CA',
                              'en-CA',
                              'en-CB',
                              'en-GB',
                              'en-SG',
                              'en-IE',
                              'en-NZ',
                              'en-PH',
                              'en-US',
                              'en-ZA',
                              'en-ZW',
                              'es-AR',
                              'es-VE',
                              'es-CR',
                              'es-MX',
                              'es-PR',
                              'es-ES',
                              'fr-BE',
                              'fr-CA',
                              'fr-CH',
                              'fr-FR',
                              'fr-LU',
                              'it-CH',
                              'it-IT',
                              'ko-KR',
                              'nl-BE',
                              'nl-NL',
                              'pt-BR',
                              'pt-PT',
                              'ru-RU',
                              'se-FI',
                              'se-SE',
                              'se-NO',
                              'ta-IN',
                              'th-TH',
                              'tr-TR',
                              'uk-UA',
                              'vi-VN',
                              'zh-CN',
                              'zh-HK',
                              'zh-MO',
                              'zh-SG',
                              'zh-TW',
                              'zu-ZA'
                              ]
        self.__lang__ = lang
        self.__device__ = 'desktop'
        self.__keyword__ = ''
        self.__ua_string__ = ''
        self.__ad_lists__: List[adReported] = []
        self.__log_path__ = path

    def page_has_loaded(driverWeb: WebDriver, advertising: adReported):
        wait = WebDriverWait(driverWeb, 20, poll_frequency=1,
                             ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException])
        wait.until(EC.element_to_be_clickable((By.XPATH, '//div')))
        # print("Checking if {} page is loaded.".format(currentUrl))
        advertising.set_landing_url(driverWeb.current_url)  # 设置广告landing链接
        page_state = ''
        try:
            page_state = driverWeb.execute_script('return document.readyState;')
        finally:
            return page_state == 'complete'

    def device(self):
        device = 'desktop'

        """BlackBerry Z30,
        LG Optimus L70,
        Microsoft Lumia 950,
        Nexus 10,
        iPhone 4,
        Galaxy S5,
        iPhone 6 Plus,
        iPad,
        """

        if self.__ua_string__.find('Android') > -1 or self.__ua_string__.find('iPhone') > -1:
            device = 'mobile'
            mobile_emulation = {
                "deviceMetrics": {"width": 360, "height": 640, "pixelRatio": 3.0},
                "userAgent": self.__ua_string__}
            self.__driver_options__.add_experimental_option('mobileEmulation', mobile_emulation)

    def headless(self, headless):
        # 设置无头浏览器
        if headless:
            self.__driver_options__.add_argument('--headless')
            self.__driver_options__.add_argument('--disable-gpu')

    def lang(self):
        # 切换语言
        if self.__lang__ is None:
            lang_list = self.__lang_list__
            self.__lang__ = random.choice(lang_list).strip()

    def ua(self):
        self.__ua_string__ = randomize_user_agent.randomize_user_agent()
        self.__driver_options__.add_argument(f"--user-agent={self.__ua_string__}")
        print(f"使用ua： {self.__ua_string__}")

    def keyword(self):
        # 找到输入框
        element = self.__driver__.find_element(By.CSS_SELECTOR, "input[name=q]")
        # 选择关键词
        keywords = ['kucoin', 'kucoin exchange', 'kucoin login', 'kucoin app']
        keyword = random.choice(keywords)
        self.__keyword__ = keyword
        # 输入关键词
        element.send_keys(self.__keyword__)
        time.sleep(3)
        # 回车「搜索」
        element.send_keys(Keys.ENTER)

    def getAds(self):
        ads_lists: List[WebElement] = self.__driver__.find_elements(By.CSS_SELECTOR, '#tads div[data-text-ad]')
        print('get ads')
        """serp url"""
        serp_url = self.__driver__.current_url
        ad_description = ''
        for ad in ads_lists:
            # 重要：广告的landing page 或者可以获取广告商户的customer id
            ad_redirect_url = ad.find_element(By.CSS_SELECTOR, 'a[data-rw]').get_attribute('data-rw')  # 重要： 谷歌广告跳转源链接
            ad_title = ad.find_element(By.CSS_SELECTOR, 'a[data-rw]').find_element(By.CSS_SELECTOR,
                                                                                   'a[data-rw] div[role=heading] span').text  # 重要：广告标题
            xpath_rule = \
                f'''
            //div[@data-text-ad]//div[a[@data-rw="{ad_redirect_url}"]]//ancestor::div[@data-text-ad]//div[not(.//a[@data-rw="{ad_redirect_url}"]) and not(ancestor::a[@data-rw="{ad_redirect_url}"]) and not(.//span[@jscontroller]) and not(ancestor::span[@jscontroller]) and not(@jscontroller) and  not(.//div[@jscontroller]) and not(ancestor::div[@jscontroller])]//text()[string-length(.)>2]/ancestor::div[1]'''
            text_elements_of_ad = ad.find_elements(By.XPATH, xpath_rule)  # 有时候文本在div下面
            for text_element_of_ad in text_elements_of_ad:
                element_text = text_element_of_ad.text
                if len(element_text) > 2:  # 如果文本长度大于2，应该是广告说明文本了
                    ad_description = element_text
            xpath_rule = \
                f'''
            //div[@data-text-ad]//div[a[@data-rw="{ad_redirect_url}"]]//ancestor::div[@data-text-ad]//span[not(.//a[@data-rw="{ad_redirect_url}"]) and not(ancestor::a[@data-rw="{ad_redirect_url}"]) and not(.//span[@jscontroller]) and not(ancestor::span[@jscontroller]) and not(@jscontroller) and  not(.//div[@jscontroller]) and not(ancestor::div[@jscontroller])]//text()[string-length(.)>2]/ancestor::span[1]'''

            text_elements_of_ad = ad.find_elements(By.XPATH, xpath_rule)  # 有时候文本在span下面
            for text_element_of_ad in text_elements_of_ad:
                element_text = text_element_of_ad.text
                if len(element_text) > 2:  # 如果文本长度大于2，应该是广告说明文本了
                    ad_description = element_text

            # 已经获取到最后的说明文本
            current_url = self.__driver__.current_url  # 重要：serp page url

            adFind = adReported.adsReported()  # 创建实例
            adFind.set_ad_title(ad_title)  # 设置广告标题
            adFind.set_ad_description(ad_description)  # 设置广告描述文本
            adFind.set_google_ad_url(ad_redirect_url)  # 设置广告跳转链接
            adFind.set_serp_url(current_url)  # 设置广告serp页面链接
            adFind.set_ua(self.__ua_string__)
            adFind.set_country(self.__lang__)
            adFind.set_keyword(self.__keyword__)
            adFind.set_device(self.__device__)
            adFind.set_language(self.__lang__)
            self.__ad_lists__.append(adFind)  # 存储到ad_lists中

    def get_landing_url(self):

        for ad in self.__ad_lists__:
            keyword = ad.get_keyword()
            ua = ad.get_ua()
            lang = ad.get_language()
            country = ad.get_country()
            device = ad.get_device()
            date_of_url = ad.get_date()
            gUrl = ad.get_google_url()
            serp_url = ad.get_serp_url()
            title = ad.get_ad_title()
            description = ad.get_ad_description()

            print(f"""
                所在结果页面：{serp_url},
                广告标题：{title},
                广告描述：{description},
                跳转链接：{gUrl},
                抓取时间：{date_of_url},
                抓取使用ua：{ua},
                抓取使用语言：{lang},
                开始抓取landing page页面...
                """)
            self.__driver__.get(gUrl)
            time.sleep(3)
            try:
                print('转到页面')
                if self.page_has_loaded(self.__driver__, ad):  # 等待页面打开
                    print('页面已经打开: {}'.format(ad.get_landing_url()))

            except TimeoutException:
                print('页面打开超时！继续下一个广告位...')

            except WebDriverException:
                print('页面打开错误:{}'.format(WebDriverException.args))

            finally:
                # log
                if ad.get_landing_url() == '??':
                    ad.set_landing_url(self.__driver__.current_url)
                landingURL = ad.get_landing_url()
                # 保存
                log = saver.saver(path=self.__log_path__)

                log.appender(keywords=keyword, ua=ua, lang=lang, country=country, device=device, time=date_of_url,
                             gUrl=gUrl,
                             SERPUrl=serp_url, title=title, description=description, landingUrl=landingURL)
                print("保存本条数据完成！")

    def start(self, headless=True):
        """开启无头与否"""
        # 切换语言
        self.__driver_options__.add_experimental_option('prefs', {'intl.accept_languages': f'{self.__lang__}'})
        # 修改 UA 信息
        self.ua()
        # 切换设备
        self.device()
        # 设置无头浏览器
        self.headless(headless)

        # 配置chrome 浏览器
        # s = Service(ChromeDriverManager().install())
        s = ChromeService(executable_path=ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install())
        self.__driver__ = webdriver.Chrome(service=s, options=self.__driver_options__)
        # 打开谷歌搜索
        self.__driver__.get('https://www.google.com/')

        # keywords
        self.keyword()

        """
        #获取广告数量 及 跳转后landing page链接 及 对应投诉链接
        # 提交需要填写ad text ，需要填写谷歌广告的展示链接以及出现bid的谷歌serp页面的链接
        # 【因此要搜集的是这几个】点击report ad没有用 点了只是带你到 https://services.google.com/inquiry/aw_tmcomplaint 页面投诉去
        """
        WebDriverWait(self.__driver__, 30).until(EC.presence_of_all_elements_located)
        # 获取链接
        self.getAds()
        # 获取最后landing url
        self.get_landing_url()

        # 退出
        self.__driver__.quit()
