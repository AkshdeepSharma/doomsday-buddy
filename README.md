# Doomsday_Buddy
The goal of this project was to create a bot that would run on a server (i.e. AWS, DO), that would tweet out the probability that North Korea would launch a nuke based on the sentiment analysis scores of recent tweets mentioning things like North Korea, nuclear war, and so on. A plot is created using plotly and tweeted out to help visualize a 30 day trend.

Files
-----
* **__init.py__:** Indicates the directory is a module. File is empty.
* **twitterAPI.py:** Authenticates with twitter, scrapes the tweets and tweets out the probability.
* **graph.py:** Creates the graph that is attached to the tweet. Note that this project is set up to run once per day, and therefore running it more than one time may make the graph look unbalanced. This can be changed, however.

NOTE: Create a "configuration.py" file containing the following code containing your twitter keys:

consumer_key = 'XXXXXXXXXXXXXXXXXXXXXX'

consumer_secret = 'XXXXXXXXXXXXXXXXXXXXXX'

access_token = 'XXXXXXXXXXX-XXXXXXXXXXX'

access_token_secret = 'XXXXXXXXXXXXXXXXXXXXXX'

NOTE 2: Create an empty CSV file named "nuke_checker.csv". This is where all your dates and % chance values will be stored and read from.

Discussion
----------
### Intro
The goals of this project were to do the following:

* Search twitter for tweets containing keywords
* Determine the sentiment analysis score (polarity) of tweets
* Determine the % chance of launching a nuke based on the formulas: Average Sentiment Analysis Score (ASAS) = Total Sentiment Analysis Score / Total Number of Tweets and %chance = 100 - ((ASAS + 1) / 2) * 100
* Paste this value, as well as the current date, in a CSV file
* Read from the CSV file and plot the %chance on a 30 day trend
* Tweet the graph and value out

### Dependencies
1. tweepy
2. textblob
3. matplotlib
4. TwitterAPI

To-Do
-----
* Switch to TensorFlow in order to get more accurate sentiment analysis values using a neural net.
* The tweepy REST api only collects tweets upto 1500 or 6-8 days, whichever comes first. Switching to using the streaming API and storing tweets in a database will result in more accurate % chance value due to more tweets being measured.

Feel free to leave any criticisms of this project, and follow my current bot on twitter at @DoomsdayBuddy.
