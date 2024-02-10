# Szymon Fica 337307
# list 9 task 1

import private
import requests
import json
import matplotlib.pyplot as plt

url21 = f"https://rest.coinapi.io/v1/ohlcv/BITSTAMP_SPOT_BTC_USD/history?apikey={private.API_key_coin()}&period_id=1DAY&time_start=2021-01-01T00:00:00&time_end=2022-01-01T00:00:00&limit=365"
url22 = f"https://rest.coinapi.io/v1/ohlcv/BITSTAMP_SPOT_BTC_USD/history?apikey={private.API_key_coin()}&period_id=1DAY&time_start=2022-01-01T00:00:00&time_end=2023-01-01T00:00:00&limit=365"
url23 = f"https://rest.coinapi.io/v1/ohlcv/BITSTAMP_SPOT_BTC_USD/history?apikey={private.API_key_coin()}&period_id=1DAY&time_start=2023-01-01T00:00:00&time_end=2023-12-20T00:00:00&limit=365"

def fetch_and_calculate_average_monthly_price(url):
    response = requests.get(url)
    response_json = response.json()

    time, price = [], []
    for progn in response_json:
        time.append(progn['time_period_start'])
        price.append(progn['price_open'])
    time = [ cz[0:10] for cz in time ]
    
    months, day_cnt = [0 for _ in range(0, 12)], [0 for _ in range(0, 12)]
    for i in range(0, len(time)):
        months[int(time[i][5:7])-1] += price[i]
        day_cnt[int(time[i][5:7])-1] += 1
    months = [months[i]/day_cnt[i] for i in range(0, 12)]
    return months

def predict(a, b):
    c = []
    prev = b[11]
    for i in range(0, 12):
        c.append(prev*(1+(b[i]-a[i])/a[i]))
        prev = c[-1]
    return c
    
#y21 = fetch_and_calculate_average_monthly_price(url21)
#y22 = fetch_and_calculate_average_monthly_price(url22)
#y23 = fetch_and_calculate_average_monthly_price(url23)

# previously calculated data:
y21 = [34628.43258064517, 45890.72107142856, 54421.37161290323, 57129.56266666667, 47118.50193548389, 35923.44300000001, 34237.733870967735, 45513.673870967745, 46056.812333333335, 57353.569032258056, 60847.51, 49673.63612903226]
y22 = [41351.7529032258, 40598.291428571436, 41893.36161290322, 41674.81333333334, 31867.85612903225, 24756.46233333333, 21419.967096774195, 22465.22, 19818.4, 19614.516129032258, 17698.766666666666, 16933.074074074073]
y23 = [20030.935483870966, 23296.10714285714, 24949.74193548387, 28858.571428571428, 27598.25925925926, 27738.423076923078, 30097.774193548386, 27919.0, 26271.7, 29507.709677419356, 36499.86666666667, 41851.882352941175]


p23 = predict(y21, y22)
months = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X', 'XI', 'XII']

fig, (ax1, ax2, ax3) = plt.subplots(3, 1)
ax1.plot(months, y21, color = 'blue')
ax1.set_title('2021')
ax2.plot(months, y22, color = 'red')
ax2.set_title('2022')
ax3.plot(months, p23, color = 'black')
ax3.plot(months, y23, color = 'purple')
ax1.legend(['BTC'])
ax2.legend(['BTC'])
ax3.legend(['predicted BTC', 'BTC'])
ax3.set_title('2023')
plt.show()

