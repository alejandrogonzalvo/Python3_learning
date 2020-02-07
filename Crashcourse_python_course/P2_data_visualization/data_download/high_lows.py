import csv

from matplotlib import pyplot as plt

path_1 = '/home/alejandrogonzalvo4eso/Escritorio/python3_learning'
path_2 = '/Crashcourse_python_course/P2_data_visualization/data_download'
path_3 = '/resources/sitka_weather_07-2014.csv'
filename = path_1 + path_2 + path_3
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
    highs = []
    for row in reader:
        high = int(row[1])
        highs.append(high)

    print(highs)


fig = plt.figure(dpi = 128, figsize = (10,6))
plt.plot(highs, c = 'red')

plt.title("Daily high temperatures, July 2014", fontsize = 24)
plt.xlabel('', fontsize = 16)
plt.ylabel("Temperature (F)", fontsize = 16)
plt.tick_params(axis = 'both', which = 'major', labelsize = 16)

plt.show()

