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



#for the moment it only take the top submission
def create_list_of_submission_from_subreddit(reddit_instance,subreddit):
    list_of_submission = [submission for submission in reddit_instance.subreddit(subreddit).hot(limit = 20)]
    return list_of_submission

#create a list that has every entry (title, body, comments) of every post
def from_sub_to_list(list_of_submission):
    final_result = []  
    for submission in list_of_submission:
        final_result.append(submission.title)
        final_result.append(submission.selftext)
        submission.comments.replace_more(limit = None)
        for comment in submission.comments.list():
            final_result.append(comment.body)
    return final_result

    
#here to debug
import regex
def count_swear_words_in_text(text, swear_words_list, error = "{e<=1}"):
    n_swear = [regex.match("(?:" + swear_word + ")" + error, word.lower()) for swear_word
         in swear_words_list for word in text.split()]
    return(n_swear)



import regex
def count_swear_words_in_text(text, swear_words_list, error = "{e<=1}"):
    n_swear = sum([bool(regex.match("(?:" + swear_word + ")" + error, word)) for swear_word
         in swear_words_list for word in text.split()])
    return(n_swear)
    
