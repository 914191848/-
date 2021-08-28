with open(r'H:\project-py\maifang\我爱我家\house_detial_info.txt','r',encoding = 'utf-8') as file:
    ls = file.read()
import json
ls = json.loads(ls)['house_detial_info']
for i in ls:
    print(i)


ls[0]
len(ls)
ls[-1]
ls2= []
for i in ls2:
    prit
for i in ls:
    if i['zhan_house_list'] != '':
        for house in i['zhan_house_list']:
            a = {'zhan':i['zhan'],'page':i['page'],'house_num': i['house_num'],'house':house}
            if a not in ls2:
                ls2.append(a)
ls[0]
len(ls2)
ls2[0]
ls
ls[0]
ls_ok = []
for i in ls:
    if i not in ls_ok:
        ls_ok.append(i)

ls_ok1 = [i for i in ls_ok if i['house_num'] != '']
ls_ok2 = [i for i in ls_ok if i['house_num'] == '']
len(lssss)
len(ls_ok2_)
len(ls_ok2)

ls_ok1_ = [{'zhan':i['zhan'],'page':i['page']} for i in ls_ok if i['house_num'] != '']
ls_ok2_ = [i for i in ls_ok2_ if {'zhan':i['zhan'],'page':i['page']} not in ls_ok1_]
ls_ok2_[0]

lssss = ls_ok1+ls_ok2_
