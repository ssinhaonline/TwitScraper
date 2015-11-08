"""
This module uses BeautifulSoup 4 and Requests package to scrape Twitter for data, and can be used to bypass the REST API request ceiling set by Twitter

@author ssinhaonline <homepage = "www.datanoobjournals.com/ssinhaonline" email = "ssinhaonline@gmail.com">
@date Nov 6, 2015
"""

import re
from bs4 import BeautifulSoup
import webbrowser

def getTweets(usrUrl):
    """Collects the tweets of passed @username and returns a list of tweets"""
    src = sourceExtractor(usrUrl)
    soup = BeautifulSoup(src)
    tweetStream = soup.find_all('ol', {'id': 'stream-items-id'})[0].find_all('li', {'data-item-type': 'tweet'})
    tweets = []
    for tweetTree in tweetStream:
        try:
            tweetPTags = tweetTree.div.find('div', {'class':'content'}).find_all('p')
            thistweet = ''
            for tag in tweetPTags:
                thistweet = tag.text + ' '
            tweets.append(thistweet)
        except:
            pass
    return tweets

def sourceExtractor(url):
    from selenium import webdriver
    from time import sleep
    driver = webdriver.Firefox()
    driver.get(url)
    src1 = driver.page_source
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
    sleep(2)
    src2 = driver.page_source
    while(len(src1)<len(src2)):
        src1 = src2
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
        sleep(2)
        src2 = driver.page_source
    driver.close()
    return src2

usrNm = raw_input('Provide your username: @')
usrUrl = 'https://twitter.com/' + usrNm.lower()
followersUrl = usrUrl + '/followers'
usrTweets = getTweets(usrUrl)
for tweet in usrTweets:
    print tweet
    print '\n'

