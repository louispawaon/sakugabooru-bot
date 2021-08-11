import requests
import tweepy
import random
import time
from pybooru import Moebooru

artistlist=[]
posturl='https://www.sakugabooru.com/post/show/'
client = Moebooru(site_url='https://www.sakugabooru.com')
array=client.artist_list(order="date")
files = client.post_list(tags="order:random")
for x in array:
    artistlist.append((x['name']))

try:
    choice = random.choice(artistlist)
    print(choice)
    files = client.post_list(tags="{}".format(choice))
    filechoice = random.choice(files)
    print("File: {0}".format(filechoice['file_url']))
    print(posturl+"{0}".format(filechoice['id']))
except:
    pass