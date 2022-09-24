from csv import reader
from os import system
from datetime import date
from zhdate import ZhDate

with open("data.csv",encoding="utf-8",newline='') as csvf:
    csv_text = reader(csvf,dialect="excel")
    data = []
    for row in csv_text:
        data.append(row)
today = date.today()  #当前日期
birthday_people_this_month = []  #本月过生日的
birthday_people_last_month = []  #上月过生日的
data = data[1:]


for person in data:
    if person[1]=='G':  #公历生日
        if person[2]==str(today.month):  #本月过生日的
            birthday_people_this_month.append((person[0],"公历"+person[2]+'月'+person[3]+'日'))
        elif person[2]==str(today.month-1):  #上个月过生日的
            birthday_people_last_month.append((person[0],"公历"+person[2]+'月'+person[3]+'日'))
    elif person[1]=='N':  #农历生日
        gregorian_date_datetime = ZhDate(today.year,int(person[2]),int(person[3])).to_datetime()
        gregorian_date = (gregorian_date_datetime.month,gregorian_date_datetime.day)
        # print(gregorian_date)
        if gregorian_date[0]==today.month:  #本月过生日的
            birthday_people_this_month.append((person[0],"农历"+ZhDate(today.year,int(person[2]),int(person[3])).chinese().split(' ')[0].split('年')[1]))
        elif gregorian_date[0]==today.month-1:  #上个月过生日的
            birthday_people_last_month.append((person[0],"农历"+ZhDate(today.year,int(person[2]),int(person[3])).chinese().split(' ')[0].split('年')[1]))
    else:
        raise ValueError("无效的历法！")

#输出
print("本月生日的有：")
for i in birthday_people_this_month:
    print(i[0],i[1])

print("\n上月生日的有：")
for i in birthday_people_last_month:
    print(i[0],i[1])

system("pause")