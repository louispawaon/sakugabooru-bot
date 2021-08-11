import requests
import tweepy
import random
import time
from pybooru import Moebooru

artistlist=[]
posturl='https://www.sakugabooru.com/post/show/'
client = Moebooru(site_url='https://www.sakugabooru.com')
array = client.artist_list(order="date")
files = client.post_list(tags="order:random")
for x in array:
    artistlist.append((x['name']))

#while (True):
try:
    choice = random.choice(artistlist)
    print(choice)
    files = client.post_list(tags="{}".format(choice))
    filechoice = random.choice(files) 
    boorurl=filechoice['file_url'] #File Item Print
    if boorurl.find('/'):
        if ".mp4" not in (boorurl.rsplit('/',1)[1]):
            print("hello")
        else:
            print("hi")
    #print(filechoice)
    '''
    r = requests.get(boorurl)
    with open("{}".format(filechoice['id'])+".mp4",'wb') as file:
        file.write(r.content)
    '''
    print(posturl+"{0}".format(filechoice['id'])) #URL Print
except:
    pass