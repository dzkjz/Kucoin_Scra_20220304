from urllib import parse
import os

path_url = "data_saved/url.txt"
path_domain = "data_saved/domain.txt"
if not os.path.exists(path_url):
    print("不存在文件")
else:
    data = open(path_url).read()
    urls = data.splitlines()
    hostnames = []
    for url in urls:
        url = url.strip()
        hostname = parse.urlparse(url).hostname
        if hostnames.count(hostname) < 1:
            hostnames.append(hostname)
    textfile = open(path_domain, "w")
    for h in hostnames:
        textfile.write(h + "\n")
    textfile.close()
    print("写完收工")
