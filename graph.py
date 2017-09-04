#!/usr/bin/env python3
import matplotlib as mplt
mplt.use('Agg')

import matplotlib.pyplot as plt
import matplotlib.dates as dates
import matplotlib.ticker as plticker
import csv
from collections import deque
import datetime as dt
import twitterAPI
from TwitterAPI import TwitterAPI
import configuration as c

# Creates current date
now = dates.date2num(dt.date.today())

# Writes current date + percent chance to csv file
with open('nuke_checker.csv', 'a', newline='') as csvfile:
    nuke_write = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    nuke_write.writerow([now] + [twitterAPI.percent_chance])

# Creates X, Y values for plot within last 30 days
with open('nuke_checker.csv') as csvfile:
    plots = deque(csv.reader(csvfile, delimiter=','), 29)
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
plt.xticks(rotation=70)
loc = plticker.MultipleLocator(base=10)
ax.yaxis.set_major_locator(loc)
ax.set_facecolor((0.95, 0.95, 0.95))
plt.xlabel('Date (YYY/MM/DD)', fontsize=14)
plt.ylabel('Percent-Chance of NK Nuking (%)', fontsize=14)
plt.title('30 Day Trend of the Percent-Chance of North Korea Nuking the World', fontsize=18)
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
r = api.request('statuses/update_with_media', {'status': 'The probability of North Korea nuking today is %s %%. Check '
                                                         'out the 30 day trend below!' % twitterAPI.percent_chance},
                {'media[]': data})
