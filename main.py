import requests
import tweepy
import random
import time
import os
import bs4
from bs4 import BeautifulSoup
from pybooru import Moebooru

siteurl='https://www.sakugabooru.com/post/show/'
client = Moebooru(site_url='https://www.sakugabooru.com')#Might change
files = client.post_list(tags="order:random")
    
api_keys = open("token.txt")
lines = api_keys.readlines()
consumer_key = lines[1].rstrip()
consumer_secret= lines[4].rstrip()
access_token = lines[7].rstrip() 
access_token_secret=lines[10].rstrip()

def main():
    #while (True):
    try:
        files = client.post_list(tags="order:random")#Random Post 
        choice = random.choice(files) #Select 1 Random Post from Query
        boorurl=choice['file_url'] #File URL
        tags = choice['tags'] #Post Tags
        verdict=filetypechecker(boorurl)
        posturl = siteurl+"{0}".format(choice['id'])#URL Print
        #print(verdict)
        #head = requests.head(boorurl)
        #For filesize checking 
        '''
        if(filesizechecker(head)): 
            pass 
        '''
        animatorname=artistgrabber(posturl)
        
        data = requests.get(boorurl)
        with open("C:/Users/Admin/Documents/PersonalFiles/Repositories/sakugabooru-video-files/{}".format(choice['id'])+".mp4",'wb') as file: #Customize
            file.write(data.content)
        time.sleep(5)
        
        params="Animator Name: {}\nTags: {}\nPost URL: {}\n".format(animatorname,tags,posturl)
        #print(params)
        #testpost(params)
        mediapost(params)
    except Exception as e:
        print(e)
        
#Filesize Checker
'''
def filesizechecker(head):
    header = head.headers
    content_length = header.get('content_length')
    if content_length and content_length > 3072:
        return False
'''
def artistgrabber(posturl):
    r =requests.get(posturl)
    soup = bs4.BeautifulSoup(r.text,'lxml')
    for div in soup.find_all(class_="sidebar"):
        artist=div.find(class_="tag-type-artist").text
    artistname=(artist.strip("? "))
    return artistname

def filetypechecker(boorurl):
    if boorurl.find('/'):
            if ".mp4" in (boorurl.rsplit('/',1)[1]):
                return True
            else:
                pass

def mediapost(params):
    try:
        auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
        auth.set_access_token(access_token,access_token_secret)
        api = tweepy.API(auth)
        #Looking into how to upload properly using tweepy
        #os.chdir('C:/Users/Admin/Documents/PersonalFiles/Repositories/sakugabooru-video-files')
    except Exception as e:
        print (e)
   
    try:
        media_list=[]
        for dirpath, dirnames, files in os.walk('C:/Users/Admin/Documents/PersonalFiles/Repositories/sakugabooru-video-files'):
            for f in files:
                media_list.append(os.path.join(dirpath,f))
        media = media_list[0]
        upload_media=api.media_upload(media)
        api.update_status(status=params, media_ids=[upload_media.media_id_string])
    except Exception as e:
        print(e)
'''       
def testpost(params):
    try:
        auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
        auth.set_access_token(access_token,access_token_secret)
        api = tweepy.API(auth)
        #Looking into how to upload properly using tweepy
        #os.chdir('C:/Users/Admin/Documents/PersonalFiles/Repositories/sakugabooru-video-files')
    except Exception as e:
        print (e)

    try:
        api.update_status(status=params)
    except Exception as e:
        print (e)
'''
if __name__ == '__main__':
    main()

#https://github.com/braian87b/tweepy - for video
#https://stackoverflow.com/questions/51106363/tweet-mp4-files-with-tweepy solving video problem it

#Change methodology for upload of video
#Limit File Size
#Change Search Method - annoying na af