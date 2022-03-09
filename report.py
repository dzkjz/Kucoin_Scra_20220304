import reader
import reporter
import saver


def report(checkIfSubmittedFirst):
    # 取链接
    print("检测是否有需要提交的数据")
    link_paras = reader.retrieve_gad_url('data_saved/log.xlsx', checkIfSubmittedFirst=checkIfSubmittedFirst)
    if link_paras is not None:

        for link_para in link_paras:
            sav = saver.saver()
            if sav.check_url_ifisSubmitted(link_para):
                print(f"{link_para}已经提交过")
            else:
                print(f'投诉 {link_para} 开始！')
                try:
                    reporter.report(link_para)
                    print(f'投诉 {link_para} 完毕！')
                    sav.save_report_log(link_para)
                except:
                    print(f'投诉 {link_para} 遇到问题 暂时不管！')


def report_2(path,checkIfSubmittedFirst=False):
    # 取链接

    link_paras = reader.retrieve_gad_url(path, checkIfSubmittedFirst)

    if link_paras is not None:
        for link_para in link_paras:
            sav = saver.saver(path=path)
            if sav.check_url_ifisSubmitted(link_para):
                print(f"{link_para}已经提交过")
            else:
                print(f'投诉 {link_para} 开始！')
                try:
                    reporter.report(link_para)
                    print(f'投诉 {link_para} 完毕！')
                    sav.save_report_log(link_para)
                except:
                    print(f'投诉 {link_para} 遇到问题 暂时不管！')


report(True)
