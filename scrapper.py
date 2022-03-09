import random
import time
from typing import List

from selenium import webdriver
from selenium.common.exceptions import TimeoutException, WebDriverException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.webdriver import WebDriver
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


def page_has_loaded(driverWeb: WebDriver, advertising: adReported):
    wait = WebDriverWait(driverWeb, 20, poll_frequency=1,
                         ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException])
    elem = wait.until(EC.element_to_be_clickable((By.XPATH, '//div')))
    # print("Checking if {} page is loaded.".format(currentUrl))
    advertising.set_landing_url(driverWeb.current_url)  # 设置广告landing链接
    page_state = ''
    try:
        page_state = driverWeb.execute_script('return document.readyState;')
    finally:
        return page_state == 'complete'


def start(headless=True):
    # 切换语言
    lang_list = ['ar-AE',
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
    lang = random.choice(lang_list).strip()
    options = webdriver.ChromeOptions()
    # options.add_argument(f"--lang={lang}")
    options.add_experimental_option('prefs', {'intl.accept_languages': f'{lang}'})

    # 修改 UA 信息
    ua_string = randomize_user_agent.randomize_user_agent()
    options.add_argument(f"--user-agent={ua_string}")
    print(f"使用ua： {ua_string}")
    # 切换手机
    device = 'desktop'
    """
    BlackBerry Z30,
    LG Optimus L70,
    Microsoft Lumia 950,
    Nexus 10,
    iPhone 4
    Galaxy S5
    iPhone 6 Plus
    iPad
    """
    if ua_string.find('Android') > -1 or ua_string.find('iPhone') > -1:
        device = 'mobile'
        mobile_emulation = {
            "deviceMetrics": {"width": 360, "height": 640, "pixelRatio": 3.0},
            "userAgent": ua_string}
        options.add_experimental_option('mobileEmulation', mobile_emulation)

    # 设置无头浏览器
    if headless:
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')

    # 配置chrome 浏览器
    s = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=s, options=options)
    # 打开谷歌搜索
    driver.get('https://www.google.com/')
    # 找到输入框
    element = driver.find_element(By.CSS_SELECTOR, "input[name=q]")
    # 选择关键词
    keywords = ['kucoin', 'kucoin exchange', 'kucoin login', 'kucoin app']
    keyword = random.choice(keywords)
    # 输入关键词
    element.send_keys(keyword)
    time.sleep(3)
    # 回车「搜索」
    element.send_keys(Keys.ENTER)

    # try:
    #     WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[name=btnK]')))
    # except TimeoutException:
    #     try:
    #         WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[name=btnG]')))
    #     except TimeoutException:
    #         print('timeout')

    # button = driver.find_element(By.CSS_SELECTOR, "input[name=btnK]")
    # button.click()

    """
    #获取广告数量 及 跳转后landing page链接 及 对应投诉链接
    # 提交需要填写ad text ，需要填写谷歌广告的展示链接以及出现bid的谷歌serp页面的链接
    # 【因此要搜集的是这几个】点击report ad没有用 点了只是带你到 https://services.google.com/inquiry/aw_tmcomplaint 页面投诉去
    """
    # time.sleep(100000)
    WebDriverWait(driver, 30).until(EC.presence_of_all_elements_located)
    # ads = driver.find_element(By.CSS_SELECTOR, '#tads')
    # 获取链接
    ads_lists: List[WebElement] = driver.find_elements(By.CSS_SELECTOR, '#tads div[data-text-ad]')

    ad_lists = list()
    if len(ads_lists) < 1:
        print("没有看到广告！")
        return
    print('获取广告信息')
    """serp url"""
    serp_url = driver.current_url
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
        current_url = driver.current_url  # 重要：serp page url

        adFind = adReported.adsReported()  # 创建实例
        adFind.set_ad_title(ad_title)  # 设置广告标题
        adFind.set_ad_description(ad_description)  # 设置广告描述文本
        adFind.set_google_ad_url(ad_redirect_url)  # 设置广告跳转链接
        adFind.set_serp_url(current_url)  # 设置广告serp页面链接
        adFind.set_ua(ua_string)
        adFind.set_country('usa')
        adFind.set_keyword(keyword)
        adFind.set_device(device)
        adFind.set_language(lang)
        ad_lists.append(adFind)  # 存储到ad_lists中

    for ad in ad_lists:
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
        driver.get(gUrl)
        time.sleep(3)
        try:
            print('转到页面')
            if page_has_loaded(driver, ad):  # 等待页面打开
                print('页面已经打开: {}'.format(ad.get_landing_url()))

        except TimeoutException:
            print('页面打开超时！继续下一个广告位...')

        except WebDriverException:
            print('页面打开错误:{}'.format(WebDriverException.args))

        finally:

            # log
            if ad.get_landing_url() == '??':
                ad.set_landing_url(driver.current_url)
            landingURL = ad.get_landing_url()
            # 保存
            log = saver.saver()

            log.appender(keywords=keyword, ua=ua, lang=lang, country=country, device=device, time=date_of_url,
                         gUrl=gUrl,
                         SERPUrl=serp_url, title=title, description=description, landingUrl=landingURL)
            print("保存本条数据完成！")

    driver.quit()
