from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
import adReported
import time
from typing import List

# https://safebrowsing.google.com/safebrowsing/report_phish/
# http://services.google.com/inquiry/aw_counterfeit   [DCMA]
# https://services.google.com/inquiry/aw_tmcomplaint [trademark]


# 读取报告 如果广告标题或者广告描述有Kucoin关键词 则提交complaint
# 暂定 trademark complaint

