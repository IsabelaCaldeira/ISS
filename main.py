import json
import turtle
import urllib.request
import time
import webbrowser   
import geocoder

url = "http://api.open-notify.org/astro.json"
response = urllib.request.urlopen(url)
result = json.loads(response.read())

file = open("iss.txt","w")
file.write("Atualmente, possui" + str(result["number"]) + "astrounatas na estação espacial internacional: \n\n")

people = result["people"]

for p in people:
    file.write(p['name'] + " - a bordo" + "\n")
    
 