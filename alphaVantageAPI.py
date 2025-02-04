import requests
import pandas
import json
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

#sym = input("Enter the stock symbol: ")
#min = input("Enter the time interval (1, 5, 15, 30, 60): ")
url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=BTC&interval=1min&apikey=IKJH57OQ1X0K6ZZ3'
r = requests.get(url)
data = r.json()
xAx=[]
yAx=[]
temp=''
for x in data['Time Series (1min)']:
    xAx.append(datetime.strptime(x,"%Y-%m-%d %H:%M:%S"))
    for y in data['Time Series (1min)'][x]['1. open']:
        temp += str(y)
    yAx.append(float(temp))
    temp=''
print(xAx, yAx) 
# plt.scatter([dt.timestamp() for dt in xAx],yAx)
# z=np.polyfit([dt.timestamp() for dt in xAx],yAx,1)
# p=np.poly1d(z)
# plt.plot(xAx,p([datetime.timestamp() for x in xAx]))   
# plt.show()

timestamps = [dt.timestamp() for dt in xAx]
plt.plot(timestamps, yAx, marker='o', linestyle='-', color='b', label='Data Points')
z = np.polyfit(timestamps, yAx, 1)
p = np.poly1d(z)
plt.plot(timestamps, p(timestamps), color='r', label='Trend Line')
plt.xlabel('Time')
plt.ylabel('Price')
plt.legend()
plt.show()