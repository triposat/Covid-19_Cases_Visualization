from plyer import notification
import requests
import json
import datetime
if __name__ == '__main__':
    while 1:
        r = requests.get(
            'https://coronavirus-19-api.herokuapp.com/countries').text.lower()
        Data = json.loads(r)
        x = input("Name of the Country: ")
        Result = [sub for sub in Data if sub['country'] == x]
        country = Result[0]['country']
        cases = Data[0]['cases']
        deaths = Data[0]['deaths']
        recovered = Data[0]['recovered']
        case = Result[0]['cases']
        today_cases = Result[0]['todaycases']
        death = Result[0]['deaths']
        today_death = Result[0]['todaydeaths']
        recover = Result[0]['recovered']
        Today_date = datetime.datetime.now().strftime("%d-%m-%y")
        Today_time = datetime.datetime.now().strftime("%H : %M : %S")
        notification.notify(title=f"Covid-19 Live Updates\tDate: {Today_date}\tTime - {Today_time}", message=f"\n\t   WORLD "
                            f"\nConfirmed Cases: {cases}\nDeaths: {deaths}\nRecovered: {recovered}\n\n\t    {country.upper()}\nConfirmed Cases: "
                            f" {case}\nTotal Deaths: {death}\nTotal Recovered: {recover}\nToday Cases: {today_cases}\nToday Deaths: {today_death}", app_icon="D:\All IN ONE\Programming Notes\Icons/vir.ico", timeout=10)
        Choice = input("Do You Want to See More Records: Press[Y/N]").lower()
        if Choice == 'y':
            continue
        else:
            exit()
