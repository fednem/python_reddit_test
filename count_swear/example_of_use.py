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
