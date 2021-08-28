from ditie_info import target_zhan
from getHtml import get_random_proxy, getHtml, get_source
from bs4 import BeautifulSoup
import json
# from house_detail_list import house_detail_list
import random
import shutil,os


with open(r'H:\project-py\maifang\我爱我家\house_detial_info.txt','r',encoding = 'utf-8') as file:
    ls = file.read()
house_detail_list = json.loads(ls)['house_detial_info']

def house_detail(house):
    house_detail_info = {}

    url_house_detail = 'https://bj.5i5j.com/ershoufang/%s.html' % house['house']
    source = get_source(url_house_detail)
    soup = BeautifulSoup(source.text)

    # 图片
    tupian = soup.find_all('div',attrs={'class':'pic-slide'})
    if len(tupian) > 0:
        tupian_url = [i['href'] for i in tupian[0].find_all('a')]
        house_detail_info['tupian_url'] = tupian_url

    # 房价信息
    fangjia_ = soup.find_all('div',attrs={'class':'content fr'})
    if len(fangjia_) > 0:
        zongjia = fangjia_[0].find_all('div',attrs={'class':'de-price fl'})[0].text
        danjia = fangjia_[0].find_all('div',attrs={'class':'danjia'})[0].get_text(strip=True)
        housesty_info = [i.get_text("|", strip=True) for i in fangjia_[0].find_all('div',attrs={'class':'house-infor clear'})]
        zushous_info = [i.get_text(" ", strip=True) for i in fangjia_[0].find_all('div',attrs={'class':'zushous'})[0].find_all('li')]

        house_detail_info['zongjia'] = zongjia
        house_detail_info['danjia'] = danjia
        house_detail_info['housesty_info'] = housesty_info
        house_detail_info['zushous_info'] = zushous_info


    # 房源信息
    fangyuan_info_ = soup.find_all('div',attrs={'class':'tag-now clear'})
    if len(fangyuan_info_) > 0:
        fangyuan_info = fangyuan_info_[0].find_all('ul',attrs={'class':'fl'})
        base_info_ = fangyuan_info[0].find_all('li')
        base_info = [i.get_text("|", strip=True) for i in base_info_]
        trans_info_ = fangyuan_info[1].find_all('li')
        trans_info = [i.get_text("|", strip=True) for i in trans_info_]

        house_detail_info['base_info'] = base_info
        house_detail_info['trans_info'] = trans_info


    # 房源特色
    fangyuan_teshe_ = soup.find_all('div',attrs={'class':'tag-nowts'})
    if len(fangyuan_teshe_) > 0 :
        fangyuan_teshe = fangyuan_teshe_[0].find_all('li')
        teshe = [i.get_text("|", strip=True) for i in fangyuan_teshe]

        house_detail_info['teshe'] = teshe

    # 业主自评
    fangyuan_yezhu_ = soup.find_all('div',attrs={'class':'yzzp'})
    if len(fangyuan_yezhu_) > 0 :
        yzzp = fangyuan_yezhu_[0].get_text("\n", strip=True)

        house_detail_info['yzzp'] = yzzp

    # 带看信息
    fangyuan_daikan_ = soup.find_all('div',attrs={'class':'infocontent dijl clear'})
    if len(fangyuan_daikan_) > 0 :
        daikan_ = fangyuan_daikan_[0].find_all('div',attrs={'class':'daikanquan fl'})
        daikan = [i.get_text("|", strip=True) for i in daikan_]

        house_detail_info['daikan_info'] = daikan

    # 小区指数
    fangyuan_zhishu_tab_ = soup.find_all('div',attrs={'class':'zhishu_tab'})
    if len(fangyuan_zhishu_tab_) > 0 :
        fangyuan_zhishu_tab = fangyuan_zhishu_tab_[0].find_all('div',attrs={'class':'zhishu_main'})
        zhishu = [i.get_text("|", strip=True) for i in fangyuan_zhishu_tab]

        house_detail_info['zhishu'] = zhishu

    # 小区信息
    infomain_xiaoqu = soup.find_all('div',attrs={'class':'infomain fl'})
    if len(infomain_xiaoqu) > 0 :
        xiaoqu_name = infomain_xiaoqu[0].a.text
        xiaoqu_info = [i.get_text("|", strip=True) for i in infomain_xiaoqu[0].find_all('li')]

        house_detail_info['xiaoqu_name'] = xiaoqu_name
        house_detail_info['xiaoqu_info'] = xiaoqu_info

    return house_detail_info

def get_house_detail(house):
    if 'house_detial' not in house.keys():
        try:
            house_detial = house_detail(house)
            house['house_detial'] = house_detial
            print('\n',house['house'],' ---- ',house_detail_list.index(house),'\n')
            with open(r'H:\project-py\maifang\我爱我家\house_detial_info.txt','w+',encoding = 'utf-8') as file:
                file.write(json.dumps({'house_detial_info':house_detail_list}))
            shutil.copy(r'H:\project-py\maifang\我爱我家\house_detial_info.txt',r'H:\project-py\maifang\我爱我家\house_detial_info_copy.txt')
            return house
        except:
            print('\n','error --- ',house['house'],' ---- ',house_detail_list.index(house),'\n')
            return house


import concurrent.futures
import urllib.request

# We can use a with statement to ensure threads are cleaned up promptly
with concurrent.futures.ThreadPoolExecutor(max_workers=15) as executor:
    while len(house_detail_list2) >0:
        print('house_detail_list2----------',len(house_detail_list2))
        # Start the load operations and mark each future with its URL
        house_detail_list2 = [i for i in house_detail_list if 'house_detial' not in i.keys()]
        future_to_url = {executor.submit(get_house_detail, house): house for house in house_detail_list2}
        try:
            for future in concurrent.futures.as_completed(future_to_url):
                url = future_to_url[future]
                try:
                    data = future.result()
                except Exception as exc:
                    print('%r generated an exception: %s' % ('url, exc'))
                else:
                    print('%r page is %d bytes' % ('url', len(data)))
        except:
            pass
