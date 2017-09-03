import matplotlib.pyplot as plt
import matplotlib.dates as dates
import csv
from collections import deque
import datetime as dt
import twitterAPI

now = dates.date2num(dt.datetime.now())

with open('nuke_checker.csv', 'a', newline='') as csvfile:
    nuke_write = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    nuke_write.writerow([now] + [twitterAPI.percent_chance])


with open('nuke_checker.csv') as csvfile:
    plots = deque(csv.reader(csvfile, delimiter=','), 30)
    X, Y = zip(*plots)

# Formatting of graph
plt.figure(figsize=(12, 9))
ax = plt.subplot(111)
ax.spines["bottom"].set_color('black')
ax.spines["left"].set_color('black')
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.grid(color=(0.9, 0.9, 0.9), linewidth=1)
ax.get_xaxis().tick_bottom()
ax.get_yaxis().tick_left()
ax.set_facecolor((0.95, 0.95, 0.95))
plt.xlabel('Date (DD/MM/YYYY)', fontsize=14)
plt.ylabel('Percent-Chance of NK Nuking (%)', fontsize=14)
plt.title('30 Day Trend of the Percent-Chance of North Korea Nuking the World', fontsize=18)
plt.ylim(0, 100)
plt.yticks(fontsize=11)
plt.xticks(fontsize=11)
plt.plot(X, Y, linewidth=1, marker='o', color='k')
ax.xaxis_date()
plt.savefig("percent-chance-nuke.png", bbox_inches='tight')
