import reader
import reporter
import os

# 取链接

while True:
    path_url_txt = 'data_saved/url.txt'
    link_paras = reader.txt_reader(path_url_txt)
    link_paras = list(dict.fromkeys(link_paras))  # 去重
    if link_paras is not None:
        if len(link_paras) > 0:
            link_para = link_paras[0]
            print(f'投诉 {link_para} 开始！')
            try:
                reporter.report(link_para)
                with open(path_url_txt, "r") as f:
                    lines = f.readlines()
                    lines.remove(f"{link_para}\n")
                    with open(path_url_txt, "w") as new_f:
                        for line in lines:
                            new_f.write(line)

                print(f'投诉 {link_para} 完毕！')
            except:
                print(f'投诉 {link_para} 遇到问题 暂时不管！')

    else:
        break
