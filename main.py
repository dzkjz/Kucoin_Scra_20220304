import scrapper
import time
import report

i = 0
while i < 1000:
    i += 1
    try:
        scrapper.start(headless=True)
        report.report()

    except:
        print("错误")
    finally:
        print("============================等待20秒启动下一轮============================")
        time.sleep(20)
        continue
# todo 缺少切换ip 处理recaptcha change ip 切换ip【需要购买代理】

# todo 读取跳转中间url

# todo 增加一个主抓巴西 我们重点国家，土耳其，德国，印度，荷兰需要间隔时间短一点的递交恶意广告，谢谢
