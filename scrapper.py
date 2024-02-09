import praw
from datetime import datetime
from pathlib import Path

if not Path('./praw.ini').is_file():
    exec(open("setup.py").read())

cleaned_comment = []

url = input("Enter url:")

reddit = praw.Reddit("DEFAULT")

submission = reddit.submission(url=url)

for top_level_comment in submission.comments:
    top_level_comment.refresh()
    top_level_comment.replies.replace_more(limit=None)
    if (not (top_level_comment.is_submitter) and not(top_level_comment.score < 2)):
        cleaned_comment.append(top_level_comment.body.replace("\n", "")) 
        print("Reddit User -> " + "Upvotes: " + str(top_level_comment.score) + ", Date: " + str(datetime.utcfromtimestamp(top_level_comment.created_utc).strftime('%m-%Y')))
        print(str(cleaned_comment)[1:-1])
        replies = top_level_comment.replies
        for reply in top_level_comment.replies.list():
            print("\nReddit User -> " + "Upvotes: " + str(reply.score) + ", Date: " + str(datetime.utcfromtimestamp(reply.created_utc).strftime('%m-%Y')))
            print(str(reply.body))
        print("---")
        cleaned_comment = []