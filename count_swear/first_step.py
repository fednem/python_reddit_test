# -*- coding: utf-8 -*-
"""
Created on Sat Feb 24 09:05:15 2018

@author: federico.nemmi
"""

username="python_project"
pwd="16RueDuFoyerToulousain"
client_id="39j6UmIRmny6rA"
client_secret="4zu-BCjOu4jsITantk95onKNiek"
user_agent="count_swear by project_python"

import praw as pw

test_reddit = pw.Reddit(client_id=client_id,
                     client_secret=client_secret,
                     user_agent=user_agent)

for submission in test_reddit.subreddit("pics").hot(limit=10):
    print(submission.title)
    
#do mind that with the following method you are created a generator and not
    #accessing the submission
sub_to_explore = test_reddit.subreddit("todayilearned").hot(limit = 1)

sub_to_expore_as_list = list(sub_to_explore)


#from generator to list of submission
list_of_submission = []
for submission in test_reddit.subreddit("pics").hot(limit=10):
    list_of_submission.append(submission)
    
#similar but with authentication details
    
test_reddit = pw.Reddit(client_id=client_id,
                     client_secret=client_secret,
                     user_agent=user_agent,
                     username = username,
                     password = pwd)


list_of_submission = [submission for submission in test_reddit.subreddit("italy").hot(limit = 10)]    

for submission in list_of_submission:
    print (submission.title)
    
test_submission = list_of_submission[0]

#find all attributres of a submission instance    
list_of_submission_attributes = sorted(list_of_submission[0].__dict__.keys())

#playing with comments

comments_of_test_submission = test_submission.comments