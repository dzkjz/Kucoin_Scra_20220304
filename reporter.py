from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
import adReported
import time
import random
from typing import List
import randomize_user_agent
from selenium.webdriver.support.ui import WebDriverWait

# https://safebrowsing.google.com/safebrowsing/report_phish/
# http://services.google.com/inquiry/aw_counterfeit   [DCMA]
# https://services.google.com/inquiry/aw_tmcomplaint [trademark]
# https://support.google.com/ads/troubleshooter/4578507

# 读取报告 如果广告标题或者广告描述有Kucoin关键词 则提交complaint
# 暂定 trademark complaint
# 修改为troubleshooter
options = webdriver.ChromeOptions()
options.add_experimental_option('prefs', {'intl.accept_languages': 'en'})
ua_string = randomize_user_agent.randomize_user_agent()
options.add_argument(f"--user-agent={ua_string}")
s = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s, options=options)
link_para = ''
# 打开谷歌投诉
# driver.get(f'https://support.google.com/ads/troubleshooter/4578507?ai={link_para}')
driver.get(f'https://support.google.com/ads/troubleshooter/4578507')

# 待页面打开
WebDriverWait(driver, 30).until(
    EC.element_to_be_clickable((By.XPATH, '//article//div//label[contains(text(),"Google Ads")]')))

# 点击

other_ads_policies_violated_element = driver.find_element(By.XPATH,
                                                          '//article//div//label[contains(text(),"Google Ads")]')
other_ads_policies_violated_element.click()
time.sleep(3)
# wait
misleading_scam_element_css = '//div[@class="list-item"]//label[@class="material-radio__label-text"]/span[contains(text(),"scam")]/parent::label/parent::div'

WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, misleading_scam_element_css)))
# 点击 misleading or scam
misleading_scam_element = driver.find_element(By.XPATH, misleading_scam_element_css)
misleading_scam_element.click()

# 填入信息
# 填入邮箱
email_address = ''
email_address_element_css = '//input[@aria-label="Email"]'
WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, email_address_element_css)))
email_address_element = driver.find_element(By.XPATH, email_address_element_css)
email_address_element.send_keys(email_address)

# 填入链接 填入tokenh 或者 link
# 找到填入的地方
link_textarea_element_css = '//textarea[contains(@id,"clickstring")]'
WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, link_textarea_element_css)))
link_textarea_element = driver.find_element(By.XPATH, link_textarea_element_css)
# 执行填写
link_textarea_element.send_keys(f'{link_para}')


# 随机取一个信息
def randomize_additional_details():
    provide_additional_details = """
    Misleading advertisement
    scam advertisement
    scam advertiser
    scam advertise
    fake brand
    false claims
    false offers
    phishing site
    phishing advertisement
    phishing advertiser
    phishing advertise
    clickbait advertisement
    clickbait advertise
    clickbait advertiser
    """
    details = provide_additional_details.splitlines()
    detail = random.choice(details)
    detail = detail.strip()
    return detail


detail = randomize_additional_details()
# 找到填入框框
comment_element_css = '//label[contains(@for,"comments_mandetory")]/following-sibling::input[contains(@aria-label,"Provide additional details")]'

comment_element = driver.find_element(By.XPATH, comment_element_css)
comment_element.send_keys(f'{detail}')

# 提交

# 找到提交按钮

submit_button_css = '//div[@class="hcfe-content"]//div[@class="buttons"]//button[contains(@class,"submit-button")]'
submit_button = driver.find_element(By.XPATH, submit_button_css)
# 提交
submit_button.click()
# 等待
time.sleep(3)
# 检测是否提交成功
confirmation_box_css = '//div[@class="cc confirmation-message"]//div[@class="confirmation-message__text"]'
# confirmation_box = driver.find_element(By.CSS_SELECTOR, confirmation_box_css)
WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, f'{confirmation_box_css}')))

# recaptcha 是否需要recaptcha
