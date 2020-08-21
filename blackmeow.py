import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
from random import randint

url = "https://www.t-cat.com.tw/Inquire/trace.aspx"

logistic_code = ['906460078323','906460078334','906460078345','906460078356','906463712466','906463712040','906460078393','906460078461','906460078450','906463712354','906465956510','906460078360','906463712084','906460078483','906463712400','906463712481']

for i in logistic_code:
    payload = {
      '__EVENTTARGET': 'ctl00$ContentPlaceHolder1$btnSend',
      '__EVENTARGUMENT': '',
      '__VIEWSTATE': 'CvASOigYWYeKtCIEpVxlPCaeQe8CEQMi68uiU37PlzuBFiI0RKToqF2NMSMfHlkl8YMNLWgEVSXPrmdGdJ9FPy3P35cz1LXvutk/ooy+vGjI+++D/CVi+8AmqrY1urXieDtauw==',
      '__VIEWSTATEGENERATOR': '9A093EFF',
      '__EVENTVALIDATION': 'Tt8BclIvi7m/w5OTMGyYEDEW6VDdNV3NlUp4n+xwjfLa9Y9jl4/RZMCGb/ayKLbjUhC9aSCdru34G35GGF1mg7fbxfm0dLaV3WFrcvnr8ojaLuyYS7VCtmsVme1/JBddqpsRW3zpEOtxEaQkjdJuPF8C6aNoDKYZ4+TzNfUzqBCkCmyCtzaEFD7oKn8tR5McoccM07TfuSxjI4tWbmd7XFGYEgDY8TDDc5IFK9OkWSNy+l0HIkAjqYMv0gx6/JrkKpb/EPe+TMs1I9UGa4CoaECLxf7JN0BK8yEh9LhCUf6xxvrk9xT6EiYsDhr3I0x8Tj5+xROUoy8o8mmWhQHznUwcfauL8kbTGDSc//Wd9aP0M4v9',
      'q': '站內搜尋',
      'ctl00$ContentPlaceHolder1$txtQuery1': i
    }
    files = []
    headers = {
      'Cookie': 'ASP.NET_SessionId=js3ujaukmjvl3oothtapgmka; citrix_ns_id=lyHJLY/Vg3n1U+9s62Hqah/JAYc0001'
    }

    response = requests.request("POST", url, headers=headers, data = payload, files = files)

    print(response.text.encode('utf8'))

    soup = BeautifulSoup(response.text.encode('utf-8'),'html.parser')

    print(soup)

    logistic_code_web = soup.find_all('a', class_="text4")
    status = soup.find_all("strong")

    print(status[0].string)
    print(logistic_code_web[0].string)

    result_status = []
    result_logistic_code = []

    result_status.append(status[0].string)
    result_logistic_code.append(logistic_code_web[0].string)

    time.sleep(randint(0.5,3))

out = {"code" : result_logistic_code,
       "status" :result_status
       }

df = pd.DataFrame(out)

df.to_csv('blackmeow.csv', sep = ',', encoding= "utf_8_sig")