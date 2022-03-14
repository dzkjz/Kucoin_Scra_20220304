import scrapper
import time
import report


class Queue:
    def do(self):
        while True:

            try:
                scrapper.start(headless=True)
            except:
                print("抓取错误")
            try:
                report.report(checkIfSubmittedFirst=True)
            except:
                print("报告数据错误")
            finally:
                print("报告数据流程完毕")
                print("============================等待20秒启动下一轮============================")
                time.sleep(20)
                continue


# todo 缺少切换ip 处理recaptcha change ip 切换ip【需要购买代理】

# todo 读取跳转中间url

# todo 增加一个主抓巴西 我们重点国家，土耳其，德国，印度，荷兰需要间隔时间短一点的递交恶意广告，谢谢

if __name__ == "__main__":
    queue = Queue()
    queue.do()
