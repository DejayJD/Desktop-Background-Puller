import praw
import urllib
import os
import shutil
from datetime import datetime, timedelta
import random
import subprocess
from appscript import *
from timeout import timeout
from time import sleep
from lastrun import lastrun




# Check to make sure that we havent run in 24 hrs 
lastrundate = datetime.strptime(lastrun, '%Y-%m-%d %H:%M:%S.%f')
if (datetime.now() - lastrundate) < timedelta(hours=20):
	print "Last executed run was less than 20 hrs ago! Quitting execution"
	exit()
else:
	print "Last executed run was over 20 hrs ago - will proceed to run"


# Sometimes running on pc awake can have issues since the wifi takes time to connect
# This sets a time out with a some retry attempts every 10 secs. (10*10 = 200 sec max timeout)
maxRetries = 10
while maxRetries > 0:
	try:
		urllib.urlretrieve('https://reddit.com/r/EarthPorn')
		break
	except Exception as e:
		print "Connection ERROR - can't reach reddit - attempt " + str(11-maxRetries)
		maxRetries -=1
		sleep(10)

if (maxRetries == 0):
	print "Max Retries Exceeded! Quitting execution"
	quit()



pictureCount = 15
maxPictureFetch = 20
blacklistedUrls = ['imgur']
clearExisting = False

# Setup Reddit API
r = praw.Reddit(client_id='2oWO-9oKpKLkCQ', client_secret='NYDPUyKvs4ZoJ5DH_5DDQGsT5eM', user_agent='EarthPornPull')

# Fetch subreddit results
print "Fetching subreddit results"
subredditResults = r.subreddit('EarthPorn').top('day', limit=maxPictureFetch)
print "Done fetching subreddit results"


print "Setting up directory"
# Setup directory
if clearExisting:
	shutil.rmtree("Wallpapers", ignore_errors=True)
if os.path.isdir("Wallpapers") == False:
	os.makedirs("Wallpapers")
print "Directory set up"


# SCRIPT = """/usr/bin/osascript<<END
# tell application "System Events"
#     tell every desktop
#         set picture to "%s"
#     end tell
# end tell
# END"""
 


count = 0
print "Parsing and saving images locally"

try: 
	for x in subredditResults:
		badUrl = False
		for blacklistedUrl in blacklistedUrls:
			if blacklistedUrl in x.url:
				print "Skipping blacklisted url: " + x.url
				badUrl = True
		if not badUrl:
			imgName = str(datetime.now()) + "-" + str(count) + ".jpg"
			if x.url.endswith('.jpg'):
				print "Saving " + imgName
				urllib.urlretrieve(x.url, imgName)
				count += 1
			else:
				urllib.urlretrieve(x.url+".jpg", imgName)
			os.rename(imgName, "Wallpapers/" + imgName)
		if count >= pictureCount:
			break
except Exception as e:
	print "Error while downloading pictures"
	print e
	
print "Done downloading pictures"
uniqueIndexes = []

# print "Setting desktop images"
# #Set the desktop images 
# se = app('System Events')
# # desktops = se.desktops.display_name.get()
# # for d in desktops:
# randomPictureIndex = random.randint(0, pictureCount)
# while randomPictureIndex in uniqueIndexes:
# 	randomPictureIndex = random.randint(0, pictureCount)

# uniqueIndexes.append(randomPictureIndex)
# imgName = str(randomPictureIndex) + ".jpg"
# path = os.getcwd() + "/Wallpapers/" + imgName
# print path
# print "Setting background to " + imgName
# subprocess.Popen(SCRIPT%path, shell=True)
# 	desk = se.desktops[its.display_name == d]
# 	print "Setting desktop picture to " + imgName
# 	desk.picture.set(mactypes.File("Wallpapers/" + imgName))

print "Saving run date to file 'lastrun.py'"
lastRunFile = open('./lastrun.py', 'w');
lastRunFile.write("lastrun = '" + str(datetime.now()) + "'")
lastRunFile.close()

print "Done"