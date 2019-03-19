from sys import platform
import json

def queryID(idcard):
    with open('data.json', 'r',encoding='utf-8') as json_data:
        city = json.load(json_data)
    city_id = idcard[:6]
    city_name = city[city_id]
    print(city_name)

if __name__ =="__main__":
    queryID(input("输入身份证号："))
