# Desktop-Background-Puller
Modified version of GitHub/Dyunkim's Reddit-Desktop-Puller.

This project pulls both Reddit.com/r/EarthPorn pictures and Unsplash.com Pictures to set to the desktop background.

Pulls the top 5 pictures of the "hot" category in the reddit subreddit "EarthPorn" 

Then pulls 10 random pictures from Unsplash.com


Keep both files in the same folder and run "run.bat" file to populate the same folder with pictures.

Installation instructions:

<li> Clone/Download+unzip the repo
<li> Run the "run.bat" program once to initialize the Wallpapers folder.
<li> Change your wallpaper to use the Wallpapers folder that was just created. Make sure all are selected.

(Windows only) To automate it where it runs every time you log on (or another trigger if you want):
<li> Open up Task Scheduler (type into Windows to find it)
<li> Create a new basic task
<li> Select "At logon" for the trigger (Or whichever trigger you prefer)
<li> For the action, select start a program, and then browse to the Desktop-Background-Puller folder and select run.bat
<li> Finish
