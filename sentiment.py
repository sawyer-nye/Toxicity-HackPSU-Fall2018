#!C:\Users\8psco\AppData\Local\Programs\Python\Python37\python.exe
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types
import reddit_scraper as scrape
import cgi
import cgitb
import os
import matplotlib.pyplot as plt
import mpld3
import word_analysis as word

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'C:/Users/8psco/Documents/gcp_credentials.json'

cgitb.enable()

form = cgi.FieldStorage()

print("Content-type: text/html")
print()

# Instantiates a client
client = language.LanguageServiceClient()

subreddit = form.getfirst("url_box", "")
links = scrape.getLinks(subreddit)

scores = []
magnitudes = []
all_comments = []

for link in links:
	comments = scrape.getComments(link)

	# The text to analyze
	for comment in comments:
		try:
			text = comment.encode("utf-8")

			document = types.Document(
		    content=text,
		    type=enums.Document.Type.PLAIN_TEXT)

			# Detects the sentiment of the text
			sentiment = client.analyze_sentiment(document=document).document_sentiment
			all_comments.append(comment)
			scores.append(sentiment.score)
			magnitudes.append(sentiment.magnitude)
			
		except:
			pass

scores_avg = sum(scores)/len(scores)
magnitudes_avg = sum(magnitudes)/len(magnitudes)

rating = "NEUTRAL"
strength = "WEAK"
color_r = "#AAAAAA"
color_s = "#AAAAAA"

if scores_avg >= 0.15:
	rating = "POSITIVE"
	color_r = "#1fd13c"
elif scores_avg < 0:
	rating = "NEGATIVE"
	color_r = "#FF0000"

if magnitudes_avg >= 0.5:
	strength = "STRONG"
	color_s = "#1fd13c"

scores_avg = " (" + str(round(scores_avg, 2)) + ")"
magnitudes_avg = " (" + str(round(magnitudes_avg, 2)) + ")"

print("<!DOCTYPE html>")
print("<html>")
print("<script src=\"http://ajax.googleapis.com/ajax/libs/jquery/1.7.1/jquery.min.js\" type=\"text/javascript\"></script>")
print("<script src=\"scripts.js\"></script>")
print("<head>")
print("<link rel=\"stylesheet\" href=\"css/styles.css\">")
print("</head>")
print("<body>")
print("<div id=\"header\">")
print("<img src=\"img/logo.png\" alt=\"Toxicity Logo\">")
print("<form action=\"sentiment.py\" method=\"POST\">")
print("<input id=\"header_input\" type=\"text\" placeholder=\"Enter A Subreddit And Be Patient!\" name=\"url_box\">")
print("</form>")
print("</div>")
print("<div id=\"results\">")
print(f"<p> Subreddit: r/{subreddit} &nbsp;&nbsp;&nbsp;&nbsp;")
print(f"Overall Subreddit Mood: <em style=\"color: {color_r}\">{rating}{scores_avg}</em> &nbsp;&nbsp;&nbsp;&nbsp;")
print(f"Overall Subreddit Passion: <em style=\"color: {color_s}\">{strength}{magnitudes_avg}</em><br><br></p>")

fig1, ax1 = plt.subplots()
ax1.set_title('Sentiment Scores (Positive values are more \"Nice\")', fontsize=20)
ax1.boxplot(scores, vert=False)
print(mpld3.fig_to_html(fig1))

fig2, ax2 = plt.subplots()
ax2.set_title('Passion Scores (Positive values are more \"Passionate\")', fontsize=20)
ax2.boxplot(magnitudes, vert=False)
print(mpld3.fig_to_html(fig2))

word.make_cloud(all_comments)

print("<p><br><br><b>Sampled Comments:</b><br><br></p>")
for comment in all_comments:
	comment = comment.encode('ascii', 'ignore').decode('ascii')
	print(f"<p><i>\"{comment}\"</i><br><br></p>")

print("</div>")
print("</body>")
print("</html>")