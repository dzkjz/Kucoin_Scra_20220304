import reader
import reporter

# 取链接

link_paras = reader.txt_reader('data_saved/url.txt')

if link_paras is not None:
    for link_para in link_paras:
        print(f'投诉 {link_para} 开始！')
        try:
            reporter.report(link_para)
            print(f'投诉 {link_para} 完毕！')
        except:
            print(f'投诉 {link_para} 遇到问题 暂时不管！')
