
import requests 

print "Downloading..."
for i in range(0, 10):
    url = "https://source.unsplash.com/random"
    f = open('Wallpapers/unsplash' + str(i) +'.jpg','wb')
    f.write(requests.get(url).content)
    f.close()
print "Done"