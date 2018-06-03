# -*- coding: utf-8 -*-
"""
Created on Sun Jun  3 09:25:36 2018

@author: lenovo
"""
import urllib.request as r
city_pinyin = input("请输入城市:");
address = 'http://api.openweathermap.org/data/2.5/forecast?q={},cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996'
info = r.urlopen(address.format(city_pinyin)).read().decode('utf-8','ignore')
import json
data = json.loads(info)
list = data['list']
first = list[0]
second = list[1]
third = list[2]
forth = list[3]
fifth = list[4]
sixth = list[5]
seventh = list[6]
print('时间' + str(first['dt_txt']) + '\n'
      +'温度' + str(first['main']['temp']) + '开式度' + '\n'
      +'最高温度' + str(first['main']['temp_max']) + '开式度' + '\n'
      +'最低温度' + str(first['main']['temp_min']) + '开式度' + '\n'
      +'天气' + str(first['weather'][0]['description']) + '\n'
      +'气压' + str(first['main']['pressure']) + 'P'
      )
print('-------------------')
print('时间' + str(second['dt_txt']) + '\n'
      +'温度' + str(second['main']['temp']) + '开式度' + '\n'
      +'最高温度' + str(second['main']['temp_max']) + '开式度' + '\n'
      +'最低温度' + str(second['main']['temp_min']) + '开式度' + '\n'
      +'天气' + str(second['weather'][0]['description']) + '\n'
      +'气压' + str(second['main']['pressure']) + 'P'
      )
print('-------------------')
print('时间' + str(third['dt_txt']) + '\n'
      +'温度' + str(third['main']['temp']) + '开式度' + '\n'
      +'最高温度' + str(third['main']['temp_max']) + '开式度' + '\n'
      +'最低温度' + str(third['main']['temp_min']) + '开式度' + '\n'
      +'天气' + str(third['weather'][0]['description']) + '\n'
      +'气压' + str(third['main']['pressure']) + 'P'
      )
print('-------------------')
print('时间' + str(fifth['dt_txt']) + '\n'
      +'温度' + str(fifth['main']['temp']) + '开式度' + '\n'
      +'最高温度' + str(fifth['main']['temp_max']) + '开式度' + '\n'
      +'最低温度' + str(fifth['main']['temp_min']) + '开式度' + '\n'
      +'天气' + str(fifth['weather'][0]['description']) + '\n'
      +'气压' + str(fifth['main']['pressure']) + 'P'
      )
print('-------------------')
print('时间' + str(forth['dt_txt']) + '\n'
      +'温度' + str(forth['main']['temp']) + '开式度' + '\n'
      +'最高温度' + str(forth['main']['temp_max']) + '开式度' + '\n'
      +'最低温度' + str(forth['main']['temp_min']) + '开式度' + '\n'
      +'天气' + str(forth['weather'][0]['description']) + '\n'
      +'气压' + str(forth['main']['pressure']) + 'P'
      )
print('-------------------')
print('时间' + str(sixth['dt_txt']) + '\n'
      +'温度' + str(sixth['main']['temp']) + '开式度' + '\n'
      +'最高温度' + str(sixth['main']['temp_max']) + '开式度' + '\n'
      +'最低温度' + str(sixth['main']['temp_min']) + '开式度' + '\n'
      +'天气' + str(sixth['weather'][0]['description']) + '\n'
      +'气压' + str(sixth['main']['pressure']) + 'P'
      )
print('-------------------')
print('时间' + str(seventh['dt_txt']) + '\n'
      +'温度' + str(seventh['main']['temp']) + '开式度' + '\n'
      +'最高温度' + str(seventh['main']['temp_max']) + '开式度' + '\n'
      +'最低温度' + str(seventh['main']['temp_min']) + '开式度' + '\n'
      +'天气' + str(seventh['weather'][0]['description']) + '\n'
      +'气压' + str(seventh['main']['pressure']) + 'P'
      )
print('-------------------')
