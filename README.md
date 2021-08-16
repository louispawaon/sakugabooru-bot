<h1><i><b><a href="https://twitter.com/BotSakuga">SakugaBot</a></b></i></h1>
<p>
<b>SakugaBot</b> is a Twitter bot dedicated for <a href="https://www.liveabout.com/sakuga-animation-in-anime-144807">sakuga animation</a> and its glorious beauty. I've seen countless Anime Twitter Accounts posting images and videos related to anime but I haven't seen any attempts of producing a bot that would regularly post sakuga videos on Twitter, other than <a href="https://twitter.com/randomsakuga">@randomsakuga</a>, one of the biggest anime accounts in social media. So I took it as a challenge for myself to recreate a bot that would handle such capabilities.

All medias posted on SakugaBot are taken from <a href="https://www.sakugabooru.com/post">SAKUGABOORU</a>, one of the biggest <i>booru</i> sites across the Internet.
</p>
<br>
<p>
<h1><b><i>Tools and Libraries</i></b></h1>
 - Python
<br>
- Requests
<br>
- OS Library
<br>
- Time Library
<br>
 - <a href="https://pybooru.readthedocs.io/en/stable/index.html">Pybooru</a>
 <br>
 - <a href="https://www.tweepy.org/">Tweepy</a>
 <br>
  - <a href="https://www.crummy.com/software/BeautifulSoup/bs4/doc/">BeautifulSoup</a>
</p>
<br>

<h1><b><i>Clone this Repository</i></b></h1>

``` 
git clone https://github.com/tremor6916/sakugabooru-bot.git
```
You need to create your own ``` token.txt``` with your appropriate API Keys that you got from Twitter.

<br>
<h1><b><i>FAQ</i></b></h1>

1. Tweepy gives out an ```Invalid file type for image: video/mp4``` error, what should I do?
<br>
    > Tweepy has merged a pull request with regards to uploading video/mp4 files using their library, but they haven't released an official release up to this day. You may want to head to the <a href="https://github.com/tweepy/tweepy">Official GitHub Repository of Tweepy</a> and follow the Installation Instructions below for you to have the latest development version.
<br>

<br>
<h1><b><i>Future Updates</i></b></h1>
- Discord Buddy <br>
- Performance Improvements <br>
- Raspberry Pi Migration 





