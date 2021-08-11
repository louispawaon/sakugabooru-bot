import requests
import tweepy
import random
import time
from pybooru import Moebooru

artistlist=[]
siteurl='https://www.sakugabooru.com/post/show/'
client = Moebooru(site_url='https://www.sakugabooru.com')
array = client.artist_list(order="date") #Might change
files = client.post_list(tags="order:random")
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
        '''
        data = requests.get(boorurl)
        with open("{}".format(filechoice['id'])+".mp4",'wb') as file:
            file.write(data.content)
        '''
        posturl = siteurl+"{0}".format(filechoice['id'])#URL Print

    except:
        pass

def filetypechecker(boorurl):
    if boorurl.find('/'):
            if ".mp4" in (boorurl.rsplit('/',1)[1]):
                return True
            else:
                pass

if __name__ == '__main__':
    main()