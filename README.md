# Toxicity

This program uses Google Cloud Platform's sentiment analysis in order to rate a subreddit from reddit.com based on how "positive" or "negative" it is. This program was created by both Sawyer Nye and Paul Scott for the HackPSU programming competition in October 2018.

# How It Works

After typing in the name of a subreddit (without the "r/" part), the program collects the top comments of all time on the subreddit and plugs them into Google's sentiment analysis. Each comment is giving two separate values. The first value shows whether or not a specific comment was positive/nice or negative/hurtful. A value less than means that the comment was negative, a value between 0 and 0.15 represents a neutral comment, and a value larger than 0.15 is considered positive. The second value returned shows how passionate the comment was. This value is strictly greater than 0, and a value larger than 0.5 is considered "strongly passionate". These values are calculated for all comments and are averaged together to form an overall score for mood and passion. This data is presented as two box plots (one for each data value), a word cloud, and a list of all comments that were used in the calculations.

# Dependencies

In order for this program to work, several dependencies must be installed.

- XAMPP, which creates a virtual Apache server https://www.apachefriends.org/index.html
- praw, a python library that scrapes Reddit comments (pip install praw)
- google-cloud-language, a python library that contains sentiment analysis from GCP (pip install google-cloud-language)
- matlibplot, a python library that creates plots (pip install -U matplotlib)
- cgi, a python library that allows for python web integration (comes w/ python)

# How To Run

Once all dependencies have been installed, navigate to the xampp installation folder, and place all files from this repository into the folder named "htdocs". In both "sentiment.py" and "reddit_scraper.py", change the shebang (at the very top of the file starting with #!) to your python executable location. In "sentiment.py", change the string in the line "os.environ['GOOGLE_APPLICATION_CREDENTIALS']" to the location of a .json file containing proper google cloud platform credentials. Once these steps have been completed, open XAMPP and hit run on the Apache Module, then run any browser and type "localhost" into the address bar.

# Screenshots
<kbd><img src="https://i.imgur.com/I8p0Zvv.png"/></kbd><br><br>
<kbd><img src="https://i.imgur.com/z2k2vUA.png"/></kbd><br><br>
<kbd><img src="https://i.imgur.com/RjUbTVZ.png"/></kbd>
