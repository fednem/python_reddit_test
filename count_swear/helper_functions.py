# -*- coding: utf-8 -*-
"""
Created on Wed Mar 14 09:16:27 2018

@author: federico nemmi
"""

import praw
import regex
from nltk.corpus import stopwords

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

    
#give matching as ouotput
def count_swear_words_in_text(text, swear_words_list, error = "{e<=1}"):
    non_stopword = [word for word in text.split() if word not in stopwords.words("english") ]
    n_swear = [regex.match("(?:" + swear_word + ")" + error, word.lower()) for swear_word
         in swear_words_list for word in non_stopword]
    return(n_swear)


#give number of swearword as output, the one giving matching has been preferred, I leave this here for future reference
#def count_swear_words_in_text(text, swear_words_list, error = "{e<=1}"):
#    non_stopword = [word for word in text.split() if word not in stopwords.words("english") ]
#    n_swear = sum([bool(regex.match("(?:" + swear_word + ")" + error, word)) for swear_word
#         in swear_words_list for word in non_stopword])
#    return(n_swear)
    

def count_words_in_text(text):
    non_stopword = [word for word in text.split() if word not in stopwords.words("english") ]
    return len(non_stopword)

def swear_ratio(list_of_post, swear_words_list, error = ""):
    from itertools import chain
    match = []
    for text in list_of_post:
        local_count = count_swear_words_in_text(text, swear_words_list, error = "")
        match.append(local_count)
    only_matched = [element for element in chain(*match) if bool(element)]
    n_of_match = len(only_matched)
    
    tot_n = 0
    for text in list_of_post:
        n = count_words_in_text(text)
        tot_n += n
        
    swear_ratio = n_of_match/tot_n
    
    return only_matched, n_of_match, swear_ratio
    
#subreddit is a list of name, kwargs may be the error in the fuzzy search
def compare_subreddits(*args):
    output_dict = {}
    for subreddit in args:
        submissions = create_list_of_submission_from_subreddit(reddit_instance, subreddit)
        submissions_list = from_sub_to_list(submissions)
        flattened_list = [i for i in chain(*submissions_list)]
        
        
        
        
    
