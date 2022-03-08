import json

import pandas as pd
import pandas.errors
import os.path


class saver:
    def __init__(self, path='data_saved/log.xlsx'):
        """初始化"""
        self.__col__ = {
            '序号': [],
            '关键词': [],
            'UA': [],
            '语言': [],
            '国家IP': [],
            '设备': [],
            '发现时间': [],
            '投放生成URL': [],
            '所在SERP页面': [],
            '广告标题': [],
            '广告描述': [],
            '广告Landing Page': [],
        }
        '''文件路径'''
        self.__file_path__ = path
        """如果文件是空 则创建一个"""

        try:
            if os.path.exists(self.__file_path__):
                # df = pd.read_excel(self.__file_path__, sheet_name='Sheet1')
                print()
                # print(df.empty)
            else:
                self.new_saver()
        except pandas.errors.EmptyDataError:  # 如果表是空的文件
            self.new_saver()

    def new_saver(self):
        """重新生成一个数据表"""
        df_init = pd.DataFrame(self.__col__)
        # print(df_init)
        # 存档到默认位置
        df_init.to_excel(self.__file_path__, sheet_name='Sheet1', index=False)

    def read_index(self):
        """获取当前数据表的最后序号"""
        df = pd.read_excel(self.__file_path__, sheet_name='Sheet1', usecols=['序号'])
        if df.empty:
            # print("空表")
            return 0
        else:
            tail = df.tail(1)  # 获取最后一行
            index = tail.iloc[0]['序号']  # 获取最后一行的序号列的值
            # print(index)
            return index

    def appender(self, keywords, ua, lang, country, device, time, gUrl, SERPUrl, title, description, landingUrl):
        """添加器，把数据追加到最后一行"""
        df_origin = pd.read_excel(self.__file_path__, sheet_name='Sheet1')  # 读取原始数据DataFrame
        if df_origin.empty:
            data = {
                '序号': ['1'],
                '关键词': [keywords],
                'UA': [ua],
                '语言': [lang],
                '国家IP': [country],
                '设备': [device],
                '发现时间': [time],
                '投放生成URL': [gUrl],
                '所在SERP页面': [SERPUrl],
                '广告标题': [title],
                '广告描述': [description],
                '广告Landing Page': [landingUrl],
            }  # 生成新一行数据
        else:
            index = self.read_index()  # 读取原始数据最后一行获取index
            index += 1  # 序号自增1
            data = {
                '序号': [f"{index}"],
                '关键词': [keywords],
                'UA': [ua],
                '语言': [lang],
                '国家IP': [country],
                '设备': [device],
                '发现时间': [time],
                '投放生成URL': [gUrl],
                '所在SERP页面': [SERPUrl],
                '广告标题': [title],
                '广告描述': [description],
                '广告Landing Page': [landingUrl],
            }  # 生成新一行数据
        new_df = pd.DataFrame(data)  # 转DataFrame格式
        if df_origin.empty:
            new_df.to_excel(self.__file_path__, sheet_name='Sheet1', index=False)
        else:
            df_new = pd.concat([df_origin, new_df], axis=0)  # 追加到原始数据后面 [表合并]
            df_new.to_excel(self.__file_path__, sheet_name='Sheet1', index=False)  # 保存更新数据表

    def save_report_log(self, token, is_submitted=True):
        # 读取文档
        df = pd.read_excel(self.__file_path__, sheet_name='Sheet1')

        # 是否需要增加一列
        if 'submitted_log' not in df.columns:
            # 增加一列
            df['submitted_log'] = ''

        # 判断所在行
        if is_submitted:
            index = df.loc[df['投放生成URL'].str.contains(f'{token}', case=False, regex=False)]['序号'].index[0]
            # print(index)
            # print(df.loc[index, '投放生成URL'])
            df.loc[index, 'submitted_log'] = 'submitted'

        # 存储
        df.to_excel(self.__file_path__, sheet_name='Sheet1', index=False)

    def check_url_ifisSubmitted(self, token):
        # 读取文档
        df = pd.read_excel(self.__file_path__, sheet_name='Sheet1')
        exist = False
        # 是否需要增加一列
        if 'submitted_log' not in df.columns:
            # 增加一列
            df['submitted_log'] = ''
            # 存储
            df.to_excel(self.__file_path__, sheet_name='Sheet1', index=False)
        # 判断所在行
        submitted_log = df.loc[
            df['投放生成URL'].str.contains(f'{token}', case=False, regex=False)]
        submitted_log = submitted_log.to_json()
        submitted_log = json.loads(submitted_log)
        submitted_log_list = list(submitted_log['submitted_log'].keys())
        # submitted_log_list_last_key = submitted_log_list[-1]
        # print(submitted_log_list_last_key)

        if len(submitted_log_list) > 0:
            i = 0
            while i < len(submitted_log_list):
                key = submitted_log_list[i]
                value = submitted_log['submitted_log'][f'{key}']

                if str(value).find('submitted') > -1:
                    exist = True
                    return exist
                i += 1
            # 已经提交过了
            return exist
        else:
            # print("不存在")
            return exist
# sav = saver()
# # sav.new_saver()
# sav.read_index()
# sav.appender('kucoin', 'as', 'us', 'usa', 'desktop', '2022', 'url1', 'urlserp1', 'kucoin is king', 'kucoin is money',
#              'lanurl1')
