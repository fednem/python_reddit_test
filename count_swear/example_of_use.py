# -*- coding: utf-8 -*-
"""
Created on Wed Mar 14 16:03:22 2018

@author: federico nemmi
"""

import os.path
import praw as pw
import pickle
from itertools import chain
import nltk
from helper_functions import create_list_of_submission_from_subreddit, from_sub_to_list, count_swear_words_in_text, count_words_in_text, swear_ratio

#get to the right directory
os.chdir("C:\\Users\\federico nemmi\\Documents\\Python Scripts\\reddit\\count_swear\\count_swear")

#create set of credentials to create a reddit instance
username="python_project"
pwd="16RueDuFoyerToulousain"
client_id="39j6UmIRmny6rA"
client_secret="4zu-BCjOu4jsITantk95onKNiek"
user_agent="count_swear by project_python"

#create the instance
#open a reddit instance 
test_reddit = pw.Reddit(client_id=client_id,
                     client_secret=client_secret,
                     user_agent=user_agent,
                     username = username,
                     password = pwd)

#create a list of submissions and comments
the_donald_subs = create_list_of_submission_from_subreddit(test_reddit, "the_donald")
the_donald_list = from_sub_to_list(the_donald_subs)


# Saving the list for benchmarking:


with open('the_donald_list_12042018.pkl', 'wb') as f:  
    pickle.dump([the_donald_list], f)

#reopen the list RUN FROM HERE FROM THE SECOND TIME
the_donald_list = pickle.load( open('the_donald_list_20032018.pkl', "rb" ) )



my_swear_list = ["fuck", "bitch", "hell", "faggot", "cunt", "dick", "prick", "ass", "asshole", "fucking", "crap"]    
match = []
for text in the_donald_list:
    local_count = count_swear_words_in_text(text, my_swear_list, error = "")
    match.append(local_count)

#best results seems to be achieved without fuzzy matching (at least for short word, maybe think of being able to give a list of 
#fuzzy matching string that match different word)

only_matched = [element for element in chain(*match) if bool(element)]
n_of_match = len(only_matched)

tot_n = 0
for text in the_donald_list:
    n = count_words_in_text(text)
    tot_n += n

swear_ratio = n_of_match/tot_n


matching, number_of_swear, ratio = swear_ratio(the_donald_list, swear_words_list = my_swear_list)
