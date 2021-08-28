import json
import datetime
from ditie_info import ditie_zhan
import os

def write_house_info(item):
    house_file = {}
    house_file['house_file_ok'] = '- [ ] ok '
    house_file_name = '[{house_id}](https://bj.5i5j.com/ershoufang/{house_id}.html)  \n'.format(house_id = item['house'])
    house_file['house_file_name'] = house_file_name
    house_file_ditie = ' , '.join([' #地铁站' + ' #地铁站'.join(list(set(['/'+j[1] for j in ditie_zhan if j[0] in [i['zhan'] for i in item['info']]]))),' #地铁线' +  ' #地铁线'.join(list(set(['/'+j[2] for j in ditie_zhan if j[0] in [i['zhan'] for i in item['info']]])))]) + '\n'

    house_file['house_file_ditie'] = house_file_ditie
    house_file['tag'] = ''

    layout_img = [i for i in item['house_detial']['tupian_url'] if 'layout' in i]
    xiajia = [i for i in item['house_detial']['tupian_url'] if 'detail-sale-xiajia' in i]
    if len(xiajia) != 0:
        xiajia = '#已下架'
    else:
        xiajia = '#在售'
    if len(layout_img) == 0:
        layout_img = [i for i in item['house_detial']['tupian_url'] if 'huxing' in i]
    if len(layout_img) == 0:
        layout_img = [i for i in item['house_detial']['tupian_url'] if 'HOUSE_CUSTOMER' in i]
    if len(layout_img) == 0:
        if len(item['house_detial']['tupian_url']) > 0:
            layout_img = [item['house_detial']['tupian_url'][-1]]

    if len(layout_img)>0:
        house_file_layout_img = f"![layout]({layout_img[0]}) \n"
        house_file['house_file_layout_img'] = house_file_layout_img


    house_file_jiage = '# 简介 \n ' + ',  '.join([item['house_detial']['zongjia'],item['house_detial']['danjia']]) +' \n'
    house_file['house_file_jiage'] = house_file_jiage

    house_file_zushous = '\n'.join(item['house_detial']['zushous_info'])+'\n'
    house_file['house_file_zushous'] = house_file_zushous
    for i in item['house_detial']['zushous_info']:
        if '区域' in i:
            quyu = ' #区域/' +'/'.join(i.split(' ')[1:])

    if 'base_info' in item['house_detial'].keys():
        house_file_base_info = '# 基本信息 \n ' + '\n'.join(item['house_detial']['base_info'])+'\n'
        house_file['house_file_base_info'] = house_file_base_info
        for i in item['house_detial']['base_info']:
            if '所在楼层|' in i:
                loucheng_info = i.replace('所在楼层|','').split('/')
                if len(loucheng_info) > 0:
                    loucheng_suozai = '#所在楼层/'+loucheng_info[0]
                else:
                    loucheng_suozai = '#所在楼层/无'
                if len(loucheng_info) > 1:
                    loucheng_zong = '#总楼层/'+loucheng_info[1]
                else:
                    loucheng_zong = '#总楼层/无'
    else:
        loucheng_suozai = '#所在楼层/无'
        loucheng_zong = '#总楼层/无'

    if 'trans_info' in item['house_detial'].keys():
        house_file_trans_info = '# 交易信息 \n ' + '\n'.join(item['house_detial']['trans_info'])+'\n'
        house_file['house_file_trans_info'] = house_file_trans_info

    if 'teshe' in item['house_detial'].keys():
        house_file_teshe = '# 交易特色 \n ' + '\n'.join(item['house_detial']['teshe'])+'\n'
        house_file['house_file_teshe'] = house_file_teshe

    if 'daikan_info' in item['house_detial'].keys():
        house_file_daikan = '# 带看 \n ' + '\t '.join(item['house_detial']['daikan_info'])+'\n'
        house_file['house_file_daikan'] = house_file_daikan

    house_file_xiaoqu_name = '# 小区 ' + ''.join(item['house_detial']['xiaoqu_name'])+'\n'
    house_file['house_file_xiaoqu_name'] = house_file_xiaoqu_name

    if 'zhishu' in item['house_detial'].keys():
        house_file_zhishu = '## 小区指数 \n ' + '\n'.join(item['house_detial']['zhishu'])+'\n'
        house_file['house_file_zhishu'] = house_file_zhishu

    if 'xiaoqu_info' in item['house_detial'].keys():
        house_file_xiaoqu_info = '## 小区信息 \n ' + '\n'.join(item['house_detial']['xiaoqu_info'])+'\n'
        house_file['house_file_xiaoqu_info'] = house_file_xiaoqu_info


    try:
        danjia = float(item['house_detial']['danjia'].split('万')[0])
        num = int(danjia/2 // 1 + 1)
    except:
        num = '--'
        return
    if 'house_file_layout_img' in house_file.keys():
        zongjia = int(float(item['house_detial']['zongjia'].replace('万',''))/15)
        mianji = int(float(item['house_detial']['zongjia'].replace('万',''))/danjia/5)
        xiaoqu = '-'+item['house_detial']['xiaoqu_name']
        house_file['tag'] = f'#单价/{(num-1)*2}-{num*2} #总价/{zongjia*15}-{(zongjia+1)*15} #面积/{mianji*5}-{(mianji+1)*5 }  {quyu}/小区{xiaoqu} {xiajia} {loucheng_suozai} {loucheng_zong} #layout \n'
        File_Path = os.getcwd() +'\\房子-layout\\'   #获取到当前文件的目录，并检查是否有report文件夹，如果不存在则自动新建report文件
        if not os.path.exists(File_Path):
            os.makedirs(File_Path)
        with open(r'H:\project-py\maifang\我爱我家\房子-layout\%s.md' % item['house'], 'w+',encoding = 'utf-8') as file:
            for i in house_file.keys():
                file.write(house_file[i])
        with open(r'H:\project-py\maifang\我爱我家\房子-layout\房子-layout.md', 'a+',encoding = 'utf-8') as file:
            file.write('# [%s](%s.md) \n' % (item['house'],item['house']))
            file.write('%s \n' % house_file['house_file_ditie'])
            file.write('%s \n' % house_file['house_file_jiage'])
            file.write('%s \n' % house_file['tag'])
            file.write('%s \n' % house_file['house_file_layout_img'])
        with open(r'H:\project-py\maifang\我爱我家\房子-layout\房子-layout-ls.md', 'a+',encoding = 'utf-8') as file:
            file.write('[[%s]] \n' % item['house'])

    else:
        zongjia = int(float(item['house_detial']['zongjia'].replace('万',''))/15)
        mianji = int(float(item['house_detial']['zongjia'].replace('万',''))/danjia/5)
        xiaoqu = '-'+item['house_detial']['xiaoqu_name']
        house_file['tag'] = f'#单价/{(num-1)*2}-{num*2} #总价/{zongjia*15}-{(zongjia+1)*15} #面积/{mianji*5}-{(mianji+1)*5 }  {quyu}/小区{xiaoqu} {xiajia} {loucheng_suozai} {loucheng_zong} #nolayout \n'
        File_Path = os.getcwd() +'\\房子-nolayout\\'    #获取到当前文件的目录，并检查是否有report文件夹，如果不存在则自动新建report文件
        if not os.path.exists(File_Path):
            os.makedirs(File_Path)
        with open(r'H:\project-py\maifang\我爱我家\房子-nolayout\%s.md' % item['house'], 'w+',encoding = 'utf-8') as file:
            for i in house_file.keys():
                file.write(house_file[i])
        with open(r'H:\project-py\maifang\我爱我家\房子-nolayout\房子-nolayout.md', 'a+',encoding = 'utf-8') as file:
            file.write('# [%s](%s.md) \n' % (item['house'],item['house']))
            file.write('%s \n' % house_file['house_file_ditie'])
            file.write('%s \n' % house_file['house_file_jiage'])
            file.write('%s \n' % house_file['tag'])
        with open(r'H:\project-py\maifang\我爱我家\房子-nolayout\房子-nolayout-ls.md', 'a+',encoding = 'utf-8') as file:
            file.write('[[%s]] \n' % item['house'])

with open(r'H:\project-py\maifang\我爱我家\house_detial_info_copy.txt','r',encoding = 'utf-8') as file:
    ls = file.read()

house_detail_list = json.loads(ls)['house_detial_info']

# item = house_detail_list[0]
for item in house_detail_list:
    if item['house'] == '40826584':
        a = item
        item = a
    write_house_info(item)
