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

#Change this later to make it more secure
consumer_key = "B9Ak5QdKrUQQDTSHuwFg7Yh1V"
consumer_secret="iV6QvTchyPINQgMPMTXcTT8XkM95BbhH7CEuxNGivFJVRCF6OZ"
access_token = "1351695896170295297-XymMP0mZREWyuFJxSN3UBvSBN1wE0W"
access_token_secret="GRy7MdXpTHhFdN2z5t9w767DkSGybPVjLqWjIv8anqtiz"

for x in array:
    artistlist.append((x['name']))


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
        data = requests.get(boorurl)
        with open("C:/Users/Admin/Documents/PersonalFiles/Repositories/sakugabooru-video-files/{}".format(filechoice['id'])+".mp4",'wb') as file: #Customize
            file.write(data.content)
        posturl = siteurl+"{0}".format(filechoice['id'])#URL Print
    except:
        pass

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
    os.chdir('C:/Users/Admin/Documents/PersonalFiles/Repositories/sakugabooru-video-files')
    for booru_file in os.listdir('.'):
        api.update_with_media(booru_file)

if __name__ == '__main__':
    main()
    mediapost()