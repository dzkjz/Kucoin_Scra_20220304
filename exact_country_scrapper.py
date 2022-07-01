import random
import time
import exact_country_solver
import report

while True:
    try:
        # 巴西 我们重点国家，土耳其，德国，印度，荷兰需要间隔时间短一点的递交恶意广告，谢谢
        langs = [
            'pt-BR',
            'pt-BR',
            'pt-BR',
            'pt-BR',
            'pt-BR',
            'pt-BR',
            'pt-BR',
            'pt-BR',
            'pt-BR',
            'tr-TR',
            'tr-TR',
            'tr-TR',
            'tr-TR',
            'tr-TR',
            'tr-TR',
            'tr-TR',
            'tr-TR',
            'tr-TR',
            'de-DE',
            'de-DE',
            'de-DE',
            'de-DE',
            'de-DE',
            'de-DE',
            'de-DE',
            'de-DE',
            'de-DE',
            'nl-NL',
            'nl-NL',
            'nl-NL',
            'nl-NL',
            'nl-NL',
            'nl-NL',
            'nl-NL',
            'nl-NL',
            'nl-NL',
            'sa-IN',
            'ta-IN',
            'te-IN',
            'gu-IN',
            'hi-IN',
            'kn-IN',
            'kok-IN',
            'mr-IN',
            'pa-IN']
        lang = random.choice(langs).strip()
        path = 'data_saved/exact_country_log.xlsx'
        crawler = exact_country_solver.crawler(lang=lang, path=path)
        try:
            crawler.start(headless=True)
        except:
            print("爬完 有点小问题！")
        finally:
            print("爬取流程走完 举报开始！")
        # 举报
        try:
            report.report_2(path, checkIfSubmittedFirst=True)
        except:
            print("举报出问题")
        finally:
            print("举报流程走完")
    except:
        print("错误")
    finally:
        print("============================等待20秒启动下一轮============================")
        time.sleep(20)
