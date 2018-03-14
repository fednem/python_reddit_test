# -*- coding: utf-8 -*-
"""
Created on Wed Mar 14 09:16:27 2018

@author: federico nemmi
"""


username="python_project"
pwd="16RueDuFoyerToulousain"
client_id="39j6UmIRmny6rA"
client_secret="4zu-BCjOu4jsITantk95onKNiek"
user_agent="count_swear by project_python"

import praw as pw

#open a reddit instance 
test_reddit = pw.Reddit(client_id=client_id,
                     client_secret=client_secret,
                     user_agent=user_agent,
                     username = username,
                     password = pwd)

list_of_submission = [submission for submission in test_reddit.subreddit("italy").hot(limit = 10)]    

#for the moment it only take the top submission
def create_list_of_submission_from_subreddit(reddit_instance,subreddit):
    list_of_submission = [submission for submission in reddit_instance.subreddit(subreddit).top()]
    return list_of_submission

#create a dictionary that has the titles as keys an list composed
#of main body + comment
def from_sub_to_list(reddit_instance):
    final_result = []  
    for submission in list_of_submission:
        local_list = []
        local_list.append(submission.title)
        local_list.append(submission.selftext)
        submission.comments.replace_more(limit = None)
        for comment in submission.comments.list():
            local_list.append(comment.body)
        final_result.append(local_list)
    return final_result
#look into regex for fuzzy matching
import regex
help(regex.search)    