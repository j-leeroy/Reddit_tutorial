import praw
import pandas as pd
import datetime as dt

reddit = praw.Reddit('CREDENTIALS')

subreddit = reddit.subreddit('Texas')
#subreddit = reddit.subreddit('HEB')
search_subreddit = subreddit.search("HEB")
#keywords = ['work policy', 'time and attendance', 'occurance', 'policy', 'drug']
# for submission in subreddit.stream.submissions():
#     if len(submission.title.split()) > 10:
#         break
#     else:
#         lowerCase_title = submission.title.lower()
#         for questions in keywords:
#             if questions in lowerCase_title:
#                 print(lowerCase_title)
#                 print(
#                     'Your asked a policy question, I encourage you to visit https://partnernet.heb.com/HR/Policies/Forms/AllItems.aspx: I am a bot')
#                 break



topics_dict = { "Title":[], \
                "Author":[], \
                "url":[], \
                "created": [], \
                }

for submission in search_subreddit:
    topics_dict["Title"].append(submission.title)
    topics_dict["Author"].append(submission.author)
    topics_dict["url"].append(submission.url)
    topics_dict["created"].append(submission.created)
    # print(30*'*')
    # print('\n''TITLE: ', submission.title)
    # submission.comments.replace_more(limit=0)
    # #limiting to 15 comment replies
    # for comment in submission.comments:
    #     print(30*'-')
    #     print(comment.body)


topics_dataFrame = pd.DataFrame(topics_dict)

#creates a nice date format
def get_date(created):
    return dt.datetime.fromtimestamp(created)

_timestamp = topics_dataFrame["created"].apply(get_date)
topics_dataFrame = topics_dataFrame.assign(timestamp = _timestamp)
#Removes the useless "created" date that is in unix
topics_dataFrame = topics_dataFrame.drop(labels="created", axis=1)
print(topics_dataFrame)

topics_dataFrame.to_csv('RedditHEB.csv', index=False)


