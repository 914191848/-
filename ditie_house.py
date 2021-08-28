from ditie_info import target_zhan
from getHtml import get_random_proxy, getHtml, get_source
from bs4 import BeautifulSoup
import json
from house_list import house_list
import random

# 获取列表函数
def get_house_ls(ditie_zhan,num):
    # ditie_zhan=zhan['zhan']
    # num=zhan['page']
    #
    url_zhan = 'https://bj.5i5j.com/ershoufang/subway/{ditie_zhan}/b100e300q1n{num}/'.format(ditie_zhan=ditie_zhan,num=num)
    source = get_source(url_zhan)
    soup = BeautifulSoup(source.text)
    # 房源套数
    house_num = soup.find_all('div',attrs={'class':'total-box fl'})
    house_num = int(house_num[0].span.text)
    if (house_num/30) == (house_num//30):
        page_num = house_num//30
    else:
        page_num = house_num//30+1

    # 每页列表
    house_ls = soup.find('ul',attrs={'class':'pList'})
    house_ls = house_ls.find_all('li')
    if house_ls[0].attrs == {'class': ['nodata']}:
        house_list = []
    else:
        house_list = []
        for house_id in house_ls:
            house_list.append(house_id.div.a['href'].split('/')[-1].split('.')[0])
    return house_list,page_num,house_num

# house_list =[{'zhan':i, 'page':1, 'house_num':'', 'zhan_house_list':''} for i in target_zhan]
# 获取列表，



num=20
while num:
    try:
        for zhan in house_list:
            if (zhan['house_num'] == '') and (zhan['zhan_house_list'] == ''):
                print(len(house_list),'------',house_list.index(zhan))
                zhan_house_list = get_house_ls(zhan['zhan'],zhan['page'])
                num=20
                page_num = zhan_house_list[1]
                zhan['house_num'] = page_num
                zhan['zhan_house_list'] = zhan_house_list[0]
                if (page_num > 1) and (zhan['page'] == 1):
                    for page in range(2,page_num+1):
                        house_list.append({'zhan':zhan['zhan'], 'page':page, 'house_num':'', 'zhan_house_list':''})
                with open(r'H:\project-py\maifang\我爱我家\house_list.txt','w+',encoding = 'utf-8') as file:
                    file.write(json.dumps({'house_list':house_list}))
    except:
        num -= 1
        print('num:',num)
