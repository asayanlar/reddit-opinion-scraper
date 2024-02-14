import praw
from datetime import datetime
from pathlib import Path

def setup_praw():
    if not Path('./praw.ini').is_file():
        exec(open("setup.py").read())

def grab_url():
    return input("Enter Reddit Post's URL: ")

def create_reddit_api():
    reddit = praw.Reddit("DEFAULT")
    return reddit

def grab_submission(reddit):
    submission = reddit.submission(url=grab_url())
    return submission

def clean_comment(comment):
    cleaned_comment = str('"' + comment + '"')
    cleaned_comment = cleaned_comment
    cleaned_comment = cleaned_comment.replace('\\u200b', '').replace("\n", "")
    return cleaned_comment

def grab_all_replies(replies):
    
    for reply in replies:
        if (not (reply.is_submitter) and not(reply.score < 3)):
            print("\nReddit User -> " + "Upvotes: " + str(reply.score) + ", Date: " + str(datetime.utcfromtimestamp(reply.created_utc).strftime('%m-%Y')))
            print(clean_comment(reply.body))

def grab_top_level_comments(top_level_comment):

    if (not (top_level_comment.is_submitter) and not(top_level_comment.score < 3)):
        print("Reddit User -> " + "Upvotes: " + str(top_level_comment.score) + ", Date: " + str(datetime.utcfromtimestamp(top_level_comment.created_utc).strftime('%m-%Y')))
        print(clean_comment(top_level_comment.body))

    else:
        print("Skipped comment...")

def grab_all_comments(submission):
    for top_level_comment in submission.comments:
        grab_top_level_comments(top_level_comment)
        top_level_comment.refresh()
        replies = top_level_comment.replies.list()
        grab_all_replies(replies)
        print("---")
