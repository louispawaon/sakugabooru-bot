import requests
import tweepy
import random
import time
import os
import bs4
from bs4 import BeautifulSoup
from pybooru import Moebooru
from dotenv import load_dotenv
from config import connect_api

load_dotenv()

siteurl='https://www.sakugabooru.com/post/show/'
header = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'}
client = Moebooru(site_url='https://www.sakugabooru.com')
files = client.post_list(tags="order:random")

def boorurandom():
        try:
            files = client.post_list(tags="order:random") #Random Post 
            choice = random.choice(files) #Select 1 Random Post from Query
            boorurl=choice['file_url'] #File URL
            tags = choice['tags'] #Post Tags

            verdict=filetypechecker(boorurl) #Checker if .mp4 file or not
            if(verdict):
                posturl = siteurl+"{0}".format(choice['id']) #POST URL from SakugaBooru

                animatorname=artistgrabber(posturl)
                animename=animegrabber(posturl)
                time.sleep(5)
                
                data = requests.get(boorurl,headers=header)
                print("data:",data.status_code)
                with open("sakugabooru-video-files/{}".format(choice['id'])+".mp4",'wb') as file: 
                    file.write(data.content)
                
                params="Animator Name: {}\nListed Anime Name: {}\nTags: {}\nPost URL: {}\n".format(animatorname,animename,tags,posturl)
                
                time.sleep(5)
                mediapost(params)

        except Exception as e:
            print("Main() Error:",e)


def artistgrabber(posturl):
    r = requests.get(posturl,headers=header)
    print("artistgrabber:",r.status_code)
    soup = bs4.BeautifulSoup(r.text,'lxml')

    for div in soup.find_all(class_="tag-type-artist"):
        atags = div.find_all('a')
    for artists in atags:
        artiststr=artists.text
    print(artiststr)

    return artiststr

def animegrabber(posturl):
    r = requests.get(posturl,headers=header)
    print("animegrabber:",r.status_code)
    soup = bs4.BeautifulSoup(r.text,'lxml')
    
    for div in soup.find_all(class_="tag-type-copyright"): 
        atags = div.find_all('a')
        for anime in atags:
            animestr=anime.text
    print(animestr)

    return animestr

def filetypechecker(boorurl):
    if boorurl.find('/'):
            if ".mp4" in (boorurl.rsplit('/',1)[1]):
                return True
            else:
                return False

def mediapost(params):
    try:
        api=connect_api()
        file_path=[]
        directory_name='sakugabooru-video-files' #Customize Directory
        media_list=filter(lambda x: os.path.isfile(os.path.join(directory_name,x)),os.listdir(directory_name))
        media_list=sorted(media_list,key=lambda x: os.path.getmtime(os.path.join(directory_name,x)),reverse=True)

        for media in media_list:
            file_path.append(os.path.join(directory_name,media))       
        media=file_path[0]

        print(media)
        upload_media=api.media_upload(media, media_category='tweet_video')
        api.update_status(status=params, media_ids=[upload_media.media_id_string])

    except Exception as e:
        print("Mediapost() Error:",e)
        
if __name__ == '__main__':
    boorurandom()