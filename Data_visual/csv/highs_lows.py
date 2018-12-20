import csv
from matplotlib import pyplot as plt
from datetime import datetime


filename='death_valley_2014.csv'
with open(filename) as f:
    reader=csv.reader(f)
    header_row=next(reader)
    print(header_row)

    for index,clumn_header in enumerate(header_row):
        print(index,clumn_header)

    lows,dates,highs=[],[],[]
    for row in reader:
        try:
            low=int(float(row[3]))
            current_date=datetime.strptime(row[0],'%Y-%m-%d')
            high=int(float(row[1]))

        except ValueError:
            print(current_date,'missing data')

        else:
            lows.append(low)
            dates.append(current_date)
            highs.append(high)

fig=plt.figure(dpi=128,figsize=(6.18,3.22))
plt.title('Daily high and low temperatures,July 2014',fontsize=24)
plt.tick_params(axis='both',which='major',labelsize=16)
plt.plot(dates,highs,c='red',linewidth=0.5)
plt.plot(dates,lows,c='blue',linewidth=0.5)
plt.fill_between(dates,highs,lows,facecolor='yellow',alpha=0.5)
plt.xlabel('dates',fontsize=16)
fig.autofmt_xdate()
plt.ylabel('Temperature(F)',fontsize=16)
plt.show()
