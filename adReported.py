from datetime import datetime


class adsReported:
    """
    广告实例
    包含属性：
    名字
    获取的时间
    谷歌广告跳转前置链接
    广告landing page链接
    搜索引擎结果页面的链接
    广告的标题文本
    广告的说明文本
    """

    def __init__(self, name=''):
        """搜索使用的关键词"""
        self.__keyword__ = '??'

        """搜索使用的硬件设备信息"""
        self.__device__ = '??'

        """搜索时使用的语言"""
        self.__language__ = '??'

        """广告的名字，这个可以自定义"""
        self.__name__ = name

        """广告被发现的时间，这个会自动生成"""
        self.__date__ = datetime.now()

        """广告的谷歌投放产生的url 格式一般是google.com/…………………………"""
        self.__google_ad_url__ = '??'

        """广告跳转后的最终页面链接"""
        self.__landing_url__ = '??'

        """广告标题文本，主要用于判断是否包含品牌词"""
        self.__ad_title__ = '??'

        """广告的描述文本，主要用于判断是否包含品牌词"""
        self.__ad_description__ = '??'

        """广告被发现时所在的serp页面的链接"""
        self.__ad_serp_url__ = '??'
        """广告被发现国家"""
        self.__country = '??'
        """广告被发现时使用的ua"""
        self.__ua__ = '??'

    def renew_date(self):
        """更新发现时间"""
        self.__date__ = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")

    def get_date(self):
        return self.__date__

    def set_google_ad_url(self, url):
        """设置投放产生的谷歌url"""
        self.__google_ad_url__ = url

    def get_google_url(self):
        """获取投放生成的谷歌url"""
        return self.__google_ad_url__

    def set_landing_url(self, url):
        """设置跳转后的最终页面链接"""
        self.__landing_url__ = url

    def get_landing_url(self):
        """获取跳转后的最终页面链接"""
        return self.__landing_url__

    def set_ad_title(self, title):
        """设置广告标题文本"""
        self.__ad_title__ = title

    def get_ad_title(self):
        """获取广告标题文本"""
        return self.__ad_title__

    def set_ad_description(self, description):
        """设置广告说明文本"""
        self.__ad_description__ = description

    def get_ad_description(self):
        """获取广告说明文本"""
        return self.__ad_description__

    def set_serp_url(self, serp_url):
        """设置广告所在serp页面的链接"""
        self.__ad_serp_url__ = serp_url

    def get_serp_url(self):
        """获取广告所在serp页面的链接"""
        return self.__ad_serp_url__

    def set_country(self, country):
        """设置广告被发现的国家"""
        self.__country = country

    def get_country(self):
        """获取广告被发现的国家"""
        return self.__country

    def set_ua(self, ua):
        """设置广告被发现时使用的ua"""
        self.__ua__ = ua

    def get_ua(self):
        """获取广告被发现时使用的ua"""
        return self.__ua__

    def set_keyword(self, keyword):
        """设置搜索时使用的关键词"""
        self.__keyword__ = keyword

    def get_keyword(self):
        """获取搜索时使用的关键词"""
        return self.__keyword__

    def set_device(self, hardware):
        """设置搜索时设置的硬件设备信息"""
        self.__device__ = hardware

    def get_device(self):
        """获取搜索时设置的硬件设备信息"""
        return self.__device__

    def set_language(self, language):
        """设置搜索时使用的语言"""
        self.__language__ = language

    def get_language(self):
        """获取搜索时使用的语言"""
        return self.__language__
