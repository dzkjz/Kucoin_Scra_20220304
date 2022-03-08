import pandas as pd
import pandas.errors
import os.path
import json
import re


# 读取excel
def retrieve_gad_url(path):
    df_data = pandas.read_excel(path, sheet_name='Sheet1', usecols=['广告标题', '广告描述', '投放生成URL'])
    gad_urls = []
    if df_data.empty:
        return None
    else:
        df_json = df_data.to_json()
        df_json = json.loads(df_json)
        last_keys = list(df_json['广告标题'].keys())[-1]
        # print(df_json['广告标题'][last_keys])
        last_keys = int(last_keys)
        i = 0
        while i < last_keys:
            title = df_json['广告标题'][f'{i}']
            description = df_json['广告描述'][f'{i}']

            title_fix = str(title).strip().lower()
            description_fix = str(description).strip().lower()
            if title_fix.find('kucoin') > -1 or description_fix.find('kucoin') > -1:
                # print(title)
                # retrieve links
                gad_url = df_json['投放生成URL'][f'{i}']
                # print(gad_url)
                gad_urls.append(gad_url)

            elif ((title_fix.find('ku') > -1 and title_fix.find('coin') > -1) or (
                    description_fix.find('ku') > -1 and description_fix.find('coin') > -1)):
                gad_url = df_json['投放生成URL'][f'{i}']
                # print(title)
                # print(gad_url)
                gad_urls.append(gad_url)
            else:
                print("没发现")
            i += 1
    return gad_urls


# 读取txt文档
def txt_reader(path):
    if os.path.exists(path):
        file = open(path)
        urls = file.read()
        urls = urls.splitlines()
        return urls
    else:
        return None


# 直接传入url
def url_reader(url, only_token=False):
    if only_token:
        re_left = 'https\:\/\/www\.google\.com/aclk\?sa\=l\&ai\='
        re_right = '\&ae\=.*'
        p = re.compile(f'({re_right}'f'|{re_left})')
        token = p.sub('', url)
        return token
    else:
        url = str(url).strip()
        return url
