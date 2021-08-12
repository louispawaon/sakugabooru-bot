import requests
import tweepy
import random
import time
import os
from pybooru import Moebooru

artistlist=[]
siteurl='https://www.sakugabooru.com/post/show/'
client = Moebooru(site_url='https://www.sakugabooru.com')
array = client.artist_list(order="date") #Might change
files = client.post_list(tags="order:random")
for x in array:
    artistlist.append((x['name']))

api_keys = open("token.txt")
lines = api_keys.readlines()
consumer_key = lines[1].rstrip()
consumer_secret= lines[4].rstrip()
access_token = lines[7].rstrip() 
access_token_secret=lines[10].rstrip()


def main():
    #while (True):
    try:
        choice = random.choice(artistlist) #Artist Name
        print(choice)
        files = client.post_list(tags="{}".format(choice))
        filechoice = random.choice(files) 
        boorurl=filechoice['file_url'] #File Item
        verdict=filetypechecker(boorurl)
        #print(filechoice)
        print(verdict)
        head = requests.head(boorurl)
        #For filesize checking 
        '''
        if(filesizechecker(head)): 
            pass 
        '''
        data = requests.get(boorurl)
        with open("C:/Users/Admin/Documents/PersonalFiles/Repositories/sakugabooru-video-files/{}".format(filechoice['id'])+".mp4",'wb') as file: #Customize
            file.write(data.content)
        time.sleep(5)
        mediapost()
        posturl = siteurl+"{0}".format(filechoice['id'])#URL Print
    except:
        pass

#Filesize Checker
'''
def filesizechecker(head):
    header = head.headers
    content_length = header.get('content_length')
    if content_length and content_length > 3072:
        return False
'''

def filetypechecker(boorurl):
    if boorurl.find('/'):
            if ".mp4" in (boorurl.rsplit('/',1)[1]):
                return True
            else:
                pass

def mediapost():
    auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
    auth.set_access_token(access_token,access_token_secret)
    api = tweepy.API(auth)
    #Looking into how to upload properly using tweepy
    #os.chdir('C:/Users/Admin/Documents/PersonalFiles/Repositories/sakugabooru-video-files')
    try:
        media_list=[]
        for dirpath, dirnames, files in os.walk('C:/Users/Admin/Documents/PersonalFiles/Repositories/sakugabooru-video-files'):
            for f in files:
                media_list.append(os.path.join(dirpath,f))
        media = media_list[0]
        api.media_upload(media)
    except Exception as e:
        print(e)
    '''
    try:
        for booru_file in os.listdir('C:/Users/Admin/Documents/PersonalFiles/Repositories/sakugabooru-video-files'):
            api.media_upload(booru_file)
    except Exception as e:
        print(e)
    '''

if __name__ == '__main__':
    main()

#https://github.com/braian87b/tweepy - for video
#https://stackoverflow.com/questions/51106363/tweet-mp4-files-with-tweepy solving video problem it