''' 
import datetime
date_str = '09-19-2018'

date_object = datetime.strptime(date_str, '%m-%d-%Y').date()
print(type(date_object))
print(date_object) '''

''' import sys
date = input("Enter the date in dd-m-yyyy format")
date1,month,year=date.split("-")
if(int(date1)>31 or int(month) >12):
    print("Invalid date!")
    sys.exit()
date_dic = {1:"One",2:"two",3:"three",4:"Four",5:"Five",6:"Six",7:"Seven",8:"Eight",9:"Nine",10:"Ten",
11:"Eleven",12:"Twelve",13:"Thirteen",14:"Fourteen",15:"Fifteen",16:"Sixteen",17:"Seventeen",18:"Eighteen",19:
"Nineteen",20:"Twenty",21:"Twenty one",22:"Twenty two",23:"twenty three",24:"twenty four",25:"Twenty five",
26:"Twenty six",27:"Twenty seven",28:"Twenty eight",29:"Twenty nine",30:"Thirty",31:"Thirty one"}

month_dic={1:"Jan",2:"Feb",3:"Mar",4:"Apr",5:"May",6:"Jun",7:"Jul",8:"Aug",9:"Sep",10:"Oct",11:"Nov",
12:"Dec"}
print(date_dic.get(int(date1)), month_dic.get(int(month)),year) '''


import datetime
date = datetime.date(2000,8,5)
print(date)
