#importing required libraries
import urllib.request, urllib.parse, urllib.error
import json
import pandas as pd

#receiving data from API
url = 'https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,us&appid=b6907d289e10d714a6e88b30761fae22'
uh = urllib.request.urlopen(url)
data = uh.read().decode()
weather = json.loads(data)['list']

#Processing and converting data in pandas DataFrane
dates = []
temp = []
pressure = []
wind_speed = []
final = {}
for day in weather:
    temp.append(day['main']['temp'])
    dates.append(day['dt_txt'])
    pressure.append(day['main']['pressure'])
    wind_speed.append(day['wind']['speed'])
final['temp'] = temp
final['wind_speed'] = wind_speed
final['pressure'] = pressure
df = pd.DataFrame(final, index=dates)

#User intection menu
status = True
while status:
    print('Select from options below')
    print('1. Get Weather')
    print('2. Get Wind Speed')
    print('3. Get Pressure')
    print('0. Exit')

    opt = int(input('Enter choice number: '))
    if opt == 0:
        status = False
        print('Exiting')
    else:
        date = input('Enter date in YYYY-MM-DD format (range: 2019-03-27 - 2019-03-31): ')
        hr = input('Enter hour of the day in 24Hr format')
        time = date+' '+hr+':00:00'
        if opt == 1:
            print(df['temp'][time])
        elif opt == 2:
            print(df['wind_speed'][time])
        elif opt == 3:
            print(df['pressure'][time])
        else:
            print('Wrong Choice Entered..Try again')