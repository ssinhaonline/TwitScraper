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
    tweets = soup.find_all('div', {'class': 'tweet'})
    for tweet in tweets:
        permalink = tweet.find_all('p', {'class':'tweet-text'})
        print re.sub('<.*?>', '',str(permalink))[1:-1]
        print "================================================================================================"
    print len(tweets)

usrNm = raw_input('Provide your username: @')
usrUrl = 'https://twitter.com/' + usrNm.lower()
#webbrowser.open(usrUrl)
#print usrUrl
followersUrl = usrUrl + '/followers'
#usrTweets = getTweets(usrUrl)
getTweets(usrUrl)
'''
r2 = requests.get(followersUrl)
soup2 = BeautifulSoup(r2.content)
#print soup1.prettify()
#print soup2.prettify()
'''
