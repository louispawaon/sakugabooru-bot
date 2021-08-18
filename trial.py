import requests
import tweepy
import random
import time
import os
import bs4
from urllib.request import urlopen
import json
from selenium import webdriver
from bs4 import BeautifulSoup
from pybooru import Moebooru

'''
client = Moebooru(site_url='https://www.sakugabooru.com')
pagenum=random.randint(1,10)
array=client.artist_list(order="name",page=pagenum)
choice = random.choice(array)#random choice for artist
artistname=str(choice['name'])#name sa artist
print(artistname)
files = client.post_list(tags="{}".format(artistname),limit=5,page=1)#limit and page change
filechoice = random.choice(files)
print("File: {0}".format(filechoice['file_url']))
'''
#chromedriver = "/Users/Admin/Documents/PersonalFiles/Repositories/chromedriver_win32/chromedriver.exe"
#os.environ["webdriver.chrome.driver"]=chromedriver
#driver = webdriver.Chrome(executable_path='C:/Users/Admin/Documents/PersonalFiles/Repositories/chromedriver_win32/chromedriver.exe')
siteurl='https://www.sakugabooru.com/post/show/'
client = Moebooru(site_url='https://www.sakugabooru.com')#Might change
files = client.post_list(tags="order:random")
choice = random.choice(files) #Artist Name#print(files)
#print(choice)
boorurl=choice['file_url']
tags = choice['tags']
posturl = siteurl+"{0}".format(choice['id'])
print(posturl)
r =requests.get(posturl)
soup = bs4.BeautifulSoup(r.text,'lxml')

for div in soup.find_all(class_="sidebar"):
    artist=div.find(class_="tag-type-artist").text
artist2=(artist.strip("? "))
print(artist2)
print("Tags:", tags)
#Filesize Checker
'''
def filesizechecker(head):
    header = head.headers
    content_length = header.get('content_length')
    if content_length and content_length > 3072:
        return False
'''
#schedule.every(45).seconds.do(main)
'''    
def testpost(params):
    try:
        auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
        auth.set_access_token(access_token,access_token_secret)
        api = tweepy.API(auth)
    except Exception as e:
        print (e)

    try:
        api.update_status(status=params)
    except Exception as e:
        print (e)
'''
#html=requests.get(posturl).text
#driver = webdriver.Chrome(posturl)
#time.sleep(3)
#html=driver.page_source
#soup=BeautifulSoup(html,"html.parser")
#div = soup.find('div',id="content")
#print(soup.prettify())
#print(div.string)
#notes
    #make sure that the media will never duplicate 
    #random choice sa booru pagtapos search sa artistname?
    #random page not viable kay naay uban artist na dile magpakita ug result
    #dapat lahi ang video url if same tag over again (unrestrict limit?)
    #check how many posts ang related sa artist para mao ang basis sa limit ug pagenum
    #i web scrape guro jud nako ang sakugabooru para makuha ang artist list(?)-then ibutang tanan sa isa ka big list or dictionary
    #i can import a time module para every specific day mag clear out ang dictionary/list sa artist - time.sleep
    #make sure na dile (nalang) maglapas sa 1:30 ang makuha na booru
    #img files soon, mp4 lang sa ron
    #sa question about sa post url, try to use request module then dapat mag correlate ang xpath(?) sa 'file_url' na naa
    #check folder of downloads if same file/mp4, next random shit
    #since murag dile reliable ang artist tag i base nalang jud nako ni sa colored text sa kilid 

#Change methodology for upload of video
#Limit File Size
#attempt ug 2 min cooldown