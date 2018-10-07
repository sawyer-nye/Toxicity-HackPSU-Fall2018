#!C:\Users\8psco\AppData\Local\Programs\Python\Python37\python.exe
import praw
from praw.models import MoreComments

reddit = praw.Reddit(client_id='ihKFbYQUOsI9EA', \
                     client_secret='LypqJ_HTtUfLUje-f-FcAPREJIs', \
                     user_agent='toxicity_rating', \
                     username='hackpsu_scraper', \
                     password='paulandsawyer')

def getComments(post_url):
    submission = reddit.submission(url=post_url)
    usr_comments = []

    submission.comments.replace_more(limit=1) # this limits the number of replies deep

    for comment in submission.comments.list():
        if "[removed]" not in comment.body and "[deleted]" not in comment.body:
            usr_comments.append(comment.body)
            if len(usr_comments) == 10:
                break

    return usr_comments

def getLinks(sub_input):
    post_urls = []
    for submission in reddit.subreddit(sub_input).top('all', limit=5):
       post_urls.append(f'https://reddit.com/{submission.id}')
    
    return post_urls