from plyer import notification
import requests
import json
import datetime
if __name__ == '__main__':
 while 1:
    r=requests.get('https://coronavirus-19-api.herokuapp.com/countries').text.lower()
    data=json.loads(r)
    x=input("Please Enter The Name of the Country : ")
    res = [sub for sub in data if sub['country']==x]
    sa=res[0]['country']
    x=data[0]['cases']
    y=data[0]['deaths']
    z=data[0]['recovered']
    a=res[0]['cases']
    b=res[0]['todaycases']
    c=res[0]['deaths']
    d=res[0]['todaydeaths']
    e=res[0]['recovered']
    dat=datetime.datetime.now().strftime("%d-%m-%y")
    tim=datetime.datetime.now().strftime("%H : %M : %S")
    notification.notify(title=f"  Covid-19 Live Updates\tDate : {dat}\tTime - {tim}",message=f"\n\t   WORLD "
       f"\nConfirmed Cases ----> {x}\nDeaths ----> {y}\nRecovered ----> {z}\n\n\t    {sa.upper()}\nConfirmed Cases ----> "
       f" {a}\nTotal Deaths ----> {c}\nTotal Recovered ----> {e}\nToday Cases ----> {b}\nToday Deaths ----> {d}"
                           ,app_icon="C:/Users/Dell/Downloads/vir.ico",  timeout=10)
    xyz=input("Do You Want to See More Records : Press[Y/N]").lower()
    if xyz=='y':
        continue
    else:
        exit()

