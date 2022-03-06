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
        time.sleep(100)
        continue
