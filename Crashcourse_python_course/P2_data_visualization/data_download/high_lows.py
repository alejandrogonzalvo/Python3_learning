import csv
from datetime import datetime

from matplotlib import pyplot as plt


filename = 'sitka_weather_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
    dates, highs, lows = [], [], []
    for row in reader:
        date = datetime.strptime(row[0], "%Y-%m-%d")
        dates.append(date)

        high = int(row[1])
        highs.append(high)

        low = int(row[3])
        lows.append(low)

    print(highs)


fig = plt.figure(dpi = 128, figsize = (10,6))

plt.plot(dates, highs, c = 'red', alpha = 0.5)
plt.plot(dates, lows, c = 'blue', alpha = 0.5)
plt.fill_between(dates, highs, lows, facecolor = 'red', alpha = 0.3)
plt.fill_between(dates, 0, lows, facecolor = 'blue', alpha = 0.3)

csfont = {'fontname':'Comic Sans MS'}
plt.title("Daily temperatures, 2014", fontsize = 24, **csfont)
plt.xlabel('', fontsize = 16, **csfont)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize = 16)
plt.tick_params(axis = 'both', which = 'major', labelsize = 16)

plt.show()

