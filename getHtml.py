import requests
from requests.adapters import HTTPAdapter

def get_proxy():
    s = requests.Session()
    s.mount('http://', HTTPAdapter(max_retries=3))
    s.mount('https://', HTTPAdapter(max_retries=3))
    proxies = {"http": None,"https": None,}
    return s.get("http://127.0.0.1:5000/get/",timeout=(1, 10), proxies=proxies).json()

def delete_proxy(proxy):
    s = requests.Session()
    s.mount('http://', HTTPAdapter(max_retries=3))
    s.mount('https://', HTTPAdapter(max_retries=3))
    proxies = {"http": None,"https": None,}
    s.get("http://127.0.0.1:5000/delete/?proxy={}".format(proxy),timeout=(1, 10), proxies=proxies)


# 获取代理
def get_random_proxy():
    """
    get random proxy from proxypool
    :return: proxy
    """
    s = requests.Session()
    s.mount('http://', HTTPAdapter(max_retries=3))
    s.mount('https://', HTTPAdapter(max_retries=3))
    proxypool_url = 'http://localhost:5555/random'
    proxies = {"http": None,"https": None,}
    return s.get(proxypool_url,timeout=(1, 30), proxies=proxies).text.strip()

# 访问网页
proxy_host = 'dyn.horocn.com'
proxy_port = 50000
proxy_username = 'MJLI1709171073103919'
proxy_pwd = "4D5b5v1jsF7WxSwM"

proxyMeta = "http://%(user)s:%(pass)s@%(host)s:%(port)s" % {
    "host": proxy_host,
    "port": proxy_port,
    "user": proxy_username,
    "pass": proxy_pwd,}

proxies = {
    'http': proxyMeta,
    'https': proxyMeta,}
# select_proxy选择代理，0为H:\project-py\ProxyPool，1为H:\project-py\proxy_pool

'------------------使用蜻蜓代理-隧道代理---------------------'
def getHtml(url_html): #,select_proxy = 0
    # if select_proxy == 1:
    #     proxy = get_proxy()
    # else:
    #     proxy = get_random_proxy()
    headers={
    'accept': 'text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cookie': '_tb_token_=berT80V49uJ9PFEJKGPI; cna=IhV+FpiDqRsCAXE54OSIgfFP; v=0; t=bb1c685b877ff64669f99c9dade7042c; cookie2=1e5103120f9886062722c86a5fad8c64; uc1=cookie14=UoTbm8P7LhIRQg%3D%3D; isg=BJWVw-e2ZCOuRUDfqsuI4YF0pJFFPHuu_ffxbBc6UYxbbrVg3-JZdKMoODL97mFc; l=dBMDiW9Rqv8wgDSFBOCiVZ9JHt_OSIRAguWfypeMi_5Zl681GgQOkUvZ8FJ6VjWftBTB4tm2-g29-etki6jgwbd6TCNQOxDc.',
    'referer': 'https://item-paimai.taobao.com/pmp_item/609160317276.htm?s=pmp_detail&spm=a213x.7340941.2001.61.1aec2cb6RKlKoy',
    'sec-fetch-mode': 'cors',
    "sec-fetch-site": 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest'
    }
    s = requests.Session()
    s.mount('http://', HTTPAdapter(max_retries=3))
    s.mount('https://', HTTPAdapter(max_retries=3))
    # html = s.get(url_html,timeout=(1, 10), headers = headers, proxies={"http": "http://{}".format(proxy)})
    html = s.get(url_html,timeout=(1, 10), headers = headers, proxies=proxies)
    # print('proxy:',proxy)
    # 使用代理访问
    return html
    # num = 10
    # while num:
    #     try:
            # s = requests.Session()
            # s.mount('http://', HTTPAdapter(max_retries=3))
            # s.mount('https://', HTTPAdapter(max_retries=3))
            # html = s.get(url_html,timeout=(1, 10), headers = headers, proxies={"http": "http://{}".format(proxy)})
            # print('proxy:',proxy)
            # # 使用代理访问
            # return html
        # except Exception:
        #     # 删除代理池中代理
        #     if select_proxy == 1:
        #         delete_proxy(proxy)
        #         proxy = get_proxy()
        #     else:
        #         proxy = get_random_proxy()
        #     num -= 1
def get_source(url_html):
    num = 10
    while num:
        source = getHtml(url_html)
        if source.status_code != 200:
            num -= 1
            print('source.status_code:',source.status_code,'重试：',num)
        else:
            while 'window.location.href="https://bj.5i5j.com/ershoufang/' in source.text:
                url_html = source.text.replace('<HTML><HEAD><script>window.location.href="','').replace('";</script></HEAD><BODY>','')
                source = get_source(url_html)
            num = 0
            print('source.status_code:',source.status_code,'Ok')

    return source
