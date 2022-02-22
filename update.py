import requests
from os import getcwd

url = "https://raw.githubusercontent.com/ahihiyou20/discord-selfbot-owo-bot/main/main.py"
directory = getcwd()
filename = directory + '/main.py'
r = requests.get(url)
print("Updating: ",filename)
f = open(filename,'w')
f.write(r.text)
print("Updated ",filename)
url = "https://raw.githubusercontent.com/ahihiyou20/discord-selfbot-owo-bot/main/newdata.py"
directory = getcwd()
filename = directory + '/newdata.py'
r = requests.get(url)
print("Updating: ",filename)
f = open(filename,'w')
f.write(r.text)
print("Updated ", filename)
url = "https://raw.githubusercontent.com/ahihiyou20/discord-selfbot-owo-bot/main/setup.py"
directory = getcwd()
filename = directory + '/setup.py'
r = requests.get(url)
print("Updating: ",filename)
f = open(filename,'w')
f.write(r.text)
print("Updated ",filename)
url = "https://raw.githubusercontent.com/ahihiyou20/discord-selfbot-owo-bot/main/settings.json"
directory = getcwd()
filename = directory + '/settings.json'
r = requests.get(url)
print("Updating: ",filename)
f = open(filename,'w')
f.write(r.text)
url = "https://raw.githubusercontent.com/ahihiyou20/discord-selfbot-owo-bot/main/version.txt"
directory = getcwd()
filename = directory + '/version.txt'
r = requests.get(url)
print("Updating: ",filename)
f = open(filename,'w')
f.write(r.text)
print("Updated ",filename)
url = "https://raw.githubusercontent.com/ahihiyou20/discord-selfbot-owo-bot/main/requirements.txt"
directory = getcwd()
filename = directory + '/requirements.txt'
r = requests.get(url)
print("Updating: ",filename)
f = open(filename,'w')
f.write(r.text)
print("Updated ",filename)
url = "https://raw.githubusercontent.com/ahihiyou20/discord-selfbot-owo-bot/main/README.md"
directory = getcwd()
filename = directory + '/README.md'
r = requests.get(url)
print("Updating: ",filename)
f = open(filename,'w')
f.write(r.text)
print("Updated ",filename)
print("Successfully Updated All File!")
