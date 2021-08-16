import requests
import tweepy
import random
import time
import os
import bs4
import glob
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
        files = client.post_list(tags="order:random") #Random Post 
        choice = random.choice(files) #Select 1 Random Post from Query
        boorurl=choice['file_url'] #File URL
        tags = choice['tags'] #Post Tags
        verdict=filetypechecker(boorurl) #Checker if .mp4 file or not
        posturl = siteurl+"{0}".format(choice['id'])#URL Print
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
        
        params="Animator Name: {}\nTags: {}\nPost URL: {}\n".format(animatorname,tags,posturl)

        time.sleep(5)
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
    except Exception as e:
        print (e)
       
    try:
        file_path=[]
        directory_name='C:/Users/Admin/Documents/PersonalFiles/Repositories/sakugabooru-video-files'
        media_list=filter(lambda x: os.path.isfile(os.path.join(directory_name,x)),os.listdir(directory_name))
        media_list=sorted(media_list,key=lambda x: os.path.getmtime(os.path.join(directory_name,x)),reverse=True)
        for media in media_list:
            file_path.append(os.path.join(directory_name,media))       
        media=file_path[0]
        print(media)
        upload_media=api.media_upload(media)
        api.update_status(status=params, media_ids=[upload_media.media_id_string])
    except Exception as e:
        print("exception:",e)

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
if __name__ == '__main__':
    main()

#Change methodology for upload of video
#Limit File Size
#attempt ug 2 min cooldown