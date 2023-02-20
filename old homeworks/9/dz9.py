'''
Файл log_100.json:
1) чему равен общий вклад топ-3 всех IP по количеству посещений?
 Указать процентом
2) сколько в файле уникальных IP, с которых на сайт заходили 
только 1 раз

Файл log_full.csv:
5) найти максимально часто встречающийся IP
6) посчитать в процентах вклад этого IP адреса в общее кол-во запросов 
7) найти последнюю запись в логах с этим IP и выяснить 
какой user-agent был у этой записи 
получить словарь:

suspicious_agent = {
    "ip": '...',            # самый частовстречаемый ip в логах
    'fraction': 70.205,     # процент запросов с таким ip от общего кол-ва запросов
    'count': 29427,         # число запросов с таким IP
    'last': {               # вложенный словарь с 2-мя полями
        'agent': '...',     # последний user-agent для этого ip
        'timestamp': '...', # последний timestap для этого ip
    }
}
'''
import json
import csv
# ip_dict = {}
# with open ('log_100.json') as f:
#     lst = json.load(f)    
# total_req = len(lst)
# print(total_req)
# for row in lst:    
#     ip = row['ip']
#     if ip in ip_dict:
#         ip_dict[ip] += 1
#     else:
#         ip_dict[ip] = 1
# ip_dict = dict(sorted(ip_dict.items(), key=lambda item: item[1], reverse = True))
# print(ip_dict)
# first_3 = list(ip_dict.values())[:3]
# total = (sum(first_3) / total_req)*100
# print(f'{total} процент')        

# uniq = 0
# for row in ip_dict.items():
#     if row[1] == 1:
#         uniq += 1
# print(uniq)

# 2
suspicious_agent = {}
addit_val = {}
rows = []
with open('log_full.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        rows.append(row)
       
ip_num = {}
for elem in rows:
    timestamp = elem[0]
    ip = elem[1]
    user_agent = elem[2]
    if ip in ip_num:
        ip_num[ip] += 1
    else:
        ip_num[ip] = 1
    addit_val[ip] = {
        'agent': user_agent,
        'timestamp': timestamp,
    }
ip_num = dict(sorted(ip_num.items(), key=lambda item: item[1], reverse = True))
lst_key = list(ip_num.keys())
lst_val = list(ip_num.values())
# чтобы было точно, round не нужно использовать, но с ним красивее
fraction = round(((int(lst_val[0]) / (len(rows) - 1)) * 100), 2)
  

suspicious_agent['ip'] = lst_key[0]
suspicious_agent['fraction'] = fraction
suspicious_agent['count'] = lst_val[0] 
suspicious_agent['last'] = addit_val[lst_key[0]]
print(suspicious_agent)



 
        

        




