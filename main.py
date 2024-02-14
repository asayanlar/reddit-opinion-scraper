from scraper import * 

def setup_praw():
    if not Path('./praw.ini').is_file():
        exec(open("setup.py").read())

if __name__ == "__main__":
    setup_praw()
    reddit = create_reddit_api()
    submission = grab_submission(reddit)
    grab_all_comments(submission)