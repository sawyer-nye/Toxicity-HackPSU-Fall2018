# Toxicity-HackPSU-Fall2018
## Inspiration
Reddit is one of the most popular websites in the world. However, since it is so popular, a wide variety of people post on the website allowing for a range of both nice and mean comments. Users looking for a new subreddit may be worried about how negative (or mean) a subreddit is. Moderators of subreddits or even administrators may use this tool to gauge the the types of responses a subreddit as a whole can be described by.

## What it does
Toxicity uses Google Cloud's Language API to calculate the "sentiment" of several comments. The average of all comments is then calculated in order to find the overall "mood" of the subreddit inputted. Matplotlib and cgi are used to display box plots of the sentiment sampled comments, as well as creation of a word cloud for visualization.

## How we built it
The backend of the program uses python. The frontend is made with HTML and CSS. The frontend and the backend communicate using the cgi library in python.

## Challenges we ran into
Getting python and html to communicate was probably the most difficult part. It took 2 hours to fix this problem.

## Accomplishments that we're proud of
We made a clean looking website that functions almost exactly as we expected it to. We are especially proud of the data visualization and frontend aesthetics.

## What we learned
We learned a lot about Reddit's API and the Google Cloud API for data analysis. With the frustrations that came along the way, perhaps Javascript would have been better for frontend-backend integration than Python, but we knew how to implement the solution in Python much more strongly.
