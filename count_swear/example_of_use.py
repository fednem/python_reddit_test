# -*- coding: utf-8 -*-
"""
Created on Wed Mar 14 16:03:22 2018

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

the_donald_subs = create_list_of_submission_from_subreddit(test_reddit, "the_donald")

the_donald_list = from_sub_to_list(the_donald_subs)


# Saving the list for benchmarking:
import pickle

with open('the_donald_list_20032018.pkl', 'wb') as f:  
    pickle.dump([the_donald_list], f)

#check if it works good
for i,t in enumerate(the_donald_list):
    print(str(i) + " " + t)    

my_swear_list = ["fuck", "bitch", "hell", "faggot", "cunt", "dick", "prick", "ass", "asshole", "fucking", "crap"]    
test_list = [the_donald_list[i] for i in (1087,1090,1918,1919)]

match = []
for text in test_list:
    local_count = count_swear_words_in_text(text, my_swear_list, error = "{e<=1}")
    match.append(local_count)

from itertools import chain

[element for element in chain(*match) if bool(element)]


total_count = 0
for text in the_donald_list:
    local_count = count_swear_words_in_text(text, my_swear_list)
    total_count = total_count + local_count
        

