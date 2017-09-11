#!/usr/bin/env python3
import matplotlib as mplt
mplt.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.dates as dates
import datetime as dt
import matplotlib.ticker as plticker
import csv
from collections import deque
from TwitterAPI import TwitterAPI
import configuration as c

now = dates.date2num(dt.date.today())

# Opens nuke_checker.csv, gets the average value of the day, writes it to to_plot.csv,
# Opens to_plot.csv, and zips the last 29 values to (x, y) coordinates
with open('nuke_checker.csv') as csvfile:
    plots = deque(csv.reader(csvfile, delimiter=','), 14976)
    plots = list(deque(plots))
    plots = [float(x) for z in plots for x in z]
    plots_sum = sum(plots) / 14976
    csvfile.close()
with open('to_plot.csv', 'a', newline='') as f:
    f_writer = csv.writer(f, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    f_writer.writerow([now] + [plots_sum])
    f.close()
with open('to_plot.csv') as f:
    make_plots = deque(csv.reader(f, delimiter=','), 29)
    X, Y = zip(*make_plots)

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
plt.xticks(rotation=70)
loc = plticker.MultipleLocator(base=10)
ax.yaxis.set_major_locator(loc)
ax.set_facecolor((0.95, 0.95, 0.95))
plt.xlabel('Date (YYYY-MM-DD)', fontsize=14)
plt.ylabel('Likelihood of NK Nuking (%)', fontsize=14)
plt.title('30 Day Trend of the Likelihood of North Korea Nuking the World', fontsize=18)
plt.ylim(0, 100)
plt.yticks(fontsize=11)
plt.xticks(fontsize=11)
plt.plot(X, Y, linewidth=1, marker='o', color='k')
ax.xaxis_date()

# Creates .png file
plt.savefig("pcn.png", bbox_inches='tight')

# Tweets
api = TwitterAPI(c.consumer_key, c.consumer_secret, c.access_token, c.access_token_secret)
image = open('/root/pcn.png', 'rb')
data = image.read()
r = api.request('statuses/update_with_media', {'status': 'The probability of North Korea nuking today is %s%%. Check '
                                                         'out the 30 day trend below!' % round(float(Y[-1]), 2)},
                {'media[]': data})
