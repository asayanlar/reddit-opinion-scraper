import praw
from datetime import datetime

sep = f"\n{'-'*100}"
cleaned_comment = []

url = input("Enter url:")

reddit = praw.Reddit("DEFAULT")

submission = reddit.submission(url=url)

for top_level_comment in submission.comments:
    if (not (top_level_comment.is_submitter) and not(top_level_comment.score < 2)):
        cleaned_comment.append(top_level_comment.body.replace("\n", "")) 
        print("Reddit User -> " + "Upvotes: " + str(top_level_comment.score) + ", Date: " + str(datetime.utcfromtimestamp(top_level_comment.created_utc).strftime('%m-%Y')))
        print(str(cleaned_comment)[1:-1])
        print(sep)
        cleaned_comment = []