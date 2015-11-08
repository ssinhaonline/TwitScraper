"""
This module uses BeautifulSoup 4 and Requests package to scrape Twitter for data, and can be used to bypass the REST API request ceiling set by Twitter

@author ssinhaonline <homepage = "www.datanoobjournals.com/ssinhaonline" email = "ssinhaonline@gmail.com">
@date Nov 6, 2015
"""

import re
import requests
from bs4 import BeautifulSoup
import webbrowser

def getTweets(usrUrl):
    """Collects the tweets of passed @username and returns a list of tweets"""
    r = requests.get(usrUrl)
    soup = BeautifulSoup(r.content)
    tweetStream = soup.find_all('ol', {'id': 'stream-items-id'})[0].find_all('li', {'data-item-type': 'tweet'})
    for tweetTree in tweetStream:
        try:
            tweetPTags = tweetTree.div.find('div', {'class':'content'}).find_all('p')
            tweets = []
            for tag in tweetPTags:
                tweets.append(tag.text)
        except:
            pass
    return tweets

usrNm = raw_input('Provide your username: @')
usrUrl = 'https://twitter.com/' + usrNm.lower()
followersUrl = usrUrl + '/followers'
usrTweets = getTweets(usrUrl)
for tweet in UsrTweets:
    print tweet
    print '\n'
