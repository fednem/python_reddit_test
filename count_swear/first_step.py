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

##DO NOT RUN#
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
    
test_submission = list_of_submission[1]
test_submission.title
#find all attributres of a submission instance    
list_of_submission_attributes = sorted(list_of_submission[0].__dict__.keys())

#playing with comments

comments_of_test_submission = test_submission.comments

#comments_of_test_submission is an iterable accesible as a list, you can 
#access the body of the comment with .body
comments_of_test_submission[0].body #first top-level comment
comments_of_test_submission[1].body #second top-level comment
comments_of_test_submission[0].replies #replies to the first top-level comment
comments_of_test_submission[0].replies[0] #this is a moreccomen instance - check
#the manual
comments_of_test_submission[1].replies[0].body
comments_of_test_submission[1].replies[1].body



########TEST WORKFLOW FOR EXTRACTING SUBMSSION AND ITS COMMENT WHILE REPLACING
########THE MORE COMMENTS 
#extract the first ten hottest submission from italy
list_of_submission = [submission for submission in test_reddit.subreddit("italy").hot(limit = 10)]    
##DO NOT RUN

##RUN FROM HERE


#choose second submission
submissision_hottest_italy = list_of_submission[1]
#get title
submissision_hottest_italy_title = submissision_hottest_italy.title
print(submissision_hottest_italy_title)
#get body
submissision_hottest_italy_body = submissision_hottest_italy.selftext
print(submissision_hottest_italy_body)
#get comment forest
submissision_hottest_italy_comments = submissision_hottest_italy.comments
#observe the fact that some of the comment are "more comment" and cannot
#be read as they are 
for comment in submissision_hottest_italy_comments:
    print(comment.body)
    for reply in comment.replies:
        print("NEW REPLY")
        print(reply.body)
        
#See that the first comment to the second submission to italy is a 
#"MoreComments" instance (i.e. on the site is when you need to click
#to load more comment)
#this is a more comment instance
submissision_hottest_italy_comments[0].replies.body
#you can replace all the more comments instance with replace_more
submissision_hottest_italy_comments.replace_more(limit = 100)
#reprint
for comment in submissision_hottest_italy_comments:
    print(comment.body)
    for reply in comment.replies:
        print("NEW REPLY")
        print(reply.body)

#get a list of all comment of a submission (disregarding depth)
comment_list = submissision_hottest_italy_comments.list()
for comment in comment_list:
    print(comment.body)
#now if you add the body of the original post you will have the whole thread

#try to save some objects in the environment so that you don thave to re run everything

import pickle

with open('10_hottest_submission_to_italy_040318.pkl', 'wb') as output:
    pickle.dump(list_of_submission, output, pickle.HIGHEST_PROTOCOL)
#just hope this works and so long

submissions = pickle.load(open('10_hottest_submission_to_italy_040318.pkl', "rb"))

#create a dictionary that has the titles as keys an list composed
#of main body + comment
final_result = {}  
for submission in submissions:
    local_list = []
    local_list.append(submission.selftext)
    submission.comments.replace_more(limit = None)
    for comment in submission.comments.list():
        local_list.append(comment.body)
    final_result[submission.title] = local_list
    
#look into regex for fuzzy matching
import regex
help(regex.search)    
#see here https://pypi.python.org/pypi/regex