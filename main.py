from scraper import * 

if __name__ == "__main__":
    setup_praw()
    reddit = create_reddit_api()
    submission = grab_submission(reddit)
    grab_all_comments(submission)