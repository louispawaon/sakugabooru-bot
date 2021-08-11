import requests
import tweepy
import random
import time
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
artistlist=[]
posturl='https://www.sakugabooru.com/post/show/'
client = Moebooru(site_url='https://www.sakugabooru.com')
array=client.artist_list(order="date")
files = client.post_list(tags="order:random")
for x in array:
    artistlist.append((x['name']))

#while True:
try:
    choice = random.choice(artistlist)
    print(choice)
    files = client.post_list(tags="{}".format(choice))
    filechoice = random.choice(files)
    print("File: {0}".format(filechoice['file_url']))
    print(posturl+"{0}".format(filechoice['id']))
except:
    pass

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