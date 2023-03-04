import json
import turtle
import urllib.request
import time
import webbrowser   
import geocoder

#free API
url = "http://api.open-notify.org/astro.json"

response = urllib.request.urlopen(url)
result = json.loads(response.read())

#print astrounats
file = open("iss.txt","w")
file.write("Atualmente, possui" + str(result["number"]) + "astrounatas na estação espacial internacional: \n\n")

people = result["people"]

for p in people:
    file.write(p['name'] + " - a bordo" + "\n")
    
# print long and lat
g = geocoder.ip('me')
file.write("\nA atual lang / long é: " + str(g.latlng))
file.close()
webbrowser.open("iss.txt")

