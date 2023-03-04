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

# Setup the world map in turtle module
screen = turtle.Screen()
screen.setup(1280, 720)
screen.setworldcoordinates(-180, -90, 180, 90)

# load the world map image
screen.bgpic("map.gif")
screen.register_shape("iss.gif")
iss = turtle.Turtle()
iss.shape("iss.gif")
iss.setheading(45)
iss.penup()

