import scrapper
import time

i = 0
while i < 1000:
    i += 1
    try:
        scrapper.start(headless=False)
    except:
        print("错误")
    finally:
        print("============================等待20秒启动下一轮============================")
        time.sleep(20)
        continue
# todo reporter.py 报告侵权

# todo change ip 切换ip【需要购买代理】
