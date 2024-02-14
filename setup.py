from pathlib import Path

if not Path('./praw.ini').is_file():
    print("The praw.ini file has been created.\nPut the correct credentials in the praw.ini file.")
    f = open("praw.ini", "a")
    f.write("[DEFAULT]\n")
    f.write("client_id=\n")
    f.write("client_secret=\n")
    f.write("user_agent=")
    f.close()
    exit()