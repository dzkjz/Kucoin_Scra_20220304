import re
import saver

# link = 'https://www.google.com/aclk?sa=l&ai=DChcSEwiFxOGf1LX2AhXByZYKHVj2D5wYABABGgJ0bA&ae=2&sig=AOD64_3YrdU8caPkuvQKOQ0DxCe1ZfBGLQ&q&adurl'
# re_left = 'https\:\/\/www\.google\.com/aclk\?sa\=l\&ai\='
# re_right = '\&ae\=.*'
# p = re.compile(f'({re_right}'f'|{re_left})')
# token = p.sub('', link)
# print(token)


# path = 'data_saved/new.txt'
# file = open(path)
# urls = file.read()
# urls = urls.splitlines()
# for url in urls:
#     print(url)

sa = saver.saver()
sa.save_report_log(
    'https://www.google.com/aclk?sa=l&ai=DChcSEwjl0ZX22rH2AhXFrpYKHXRJCPsYABAAGgJ0bA&sig=AOD64_1FrHqEA_BPnrJCbPTPFp29N0HxSg&rct=j&q&adurl')
# exist = sa.check_url_ifisSubmitted('DChcSEwjC19Ts0rH2AhVBy5YKHc9GAYIYABAAGgJ0bA')
# # exist = sa.check_url_ifisSubmitted(
# #     'https://www.google.com/aclk?sa=l&ai=DChcSEwis2Nq597H2AhWHZIsKHd8EBHYYABABGgJ0bQ&ae=2&sig=AOD64_1jARB63yjOpE1StuLebtxU0--AKQ&q&adurl')
# print(exist == True)
