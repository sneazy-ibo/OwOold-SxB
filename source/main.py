import api
from sys import executable, argv, exit
import time
import requests
import os
if os.path.exists('api.py'):
 pass
else:
 exit
import atexit
from multiprocessing import Process
from multiprocessing import Pool
import random
import re
try:
 from inputimeout import inputimeout,TimeoutOccurred
except:
 from setup import install
 install()
finally:
 from inputimeout import inputimeout,TimeoutOccurred
if os.name == 'nt':
  import json
else:
  import simplejson as json
try:
  from discum import *
except:
  from setup import install
  install()
finally:
  from discum import *
try:
 from discord_webhook import DiscordWebhook
except:
 from setup import install
 install()
finally:
 from discord_webhook import DiscordWebhook
print("""\
░█████╗░░██╗░░░░░░░██╗░█████╗░  ░██████╗███████╗██╗░░░░░███████╗  ██████╗░░█████╗░████████╗
██╔══██╗░██║░░██╗░░██║██╔══██╗  ██╔════╝██╔════╝██║░░░░░██╔════╝  ██╔══██╗██╔══██╗╚══██╔══╝
██║░░██║░╚██╗████╗██╔╝██║░░██║  ╚█████╗░█████╗░░██║░░░░░█████╗░░  ██████╦╝██║░░██║░░░██║░░░
██║░░██║░░████╔═████║░██║░░██║  ░╚═══██╗██╔══╝░░██║░░░░░██╔══╝░░  ██╔══██╗██║░░██║░░░██║░░░
╚█████╔╝░░╚██╔╝░╚██╔╝░╚█████╔╝  ██████╔╝███████╗███████╗██║░░░░░  ██████╦╝╚█████╔╝░░░██║░░░
░╚════╝░░░░╚═╝░░░╚═╝░░░╚════╝░  ╚═════╝░╚══════╝╚══════╝╚═╝░░░░░  ╚═════╝░░╚════╝░░░░╚═╝░░░

**Version: 1.0.3**""")
wbm=[13,16]
time.sleep(0.5)
class client:
  commands=[
    "owo hunt",
    "owo hunt",
    "owo battle"
    ]
  totalcmd = 0
  totaltext = 0
  stopped = False
  recentversion = "1.0.3"
  class color:
    purple = '\033[95m'
    okblue = '\033[94m'
    okcyan = '\033[96m'
    okgreen = '\033[92m'
    warning = '\033[93m'
    fail = '\033[91m'
    reset = '\033[0m'
    bold = '\033[1m'
    underline = '\033[4m'
    if os.name == 'nt':
     purple = ''
     okblue = ''
     okcyan = ''
     okgreen = ''
     warning = ''
     fail = ''
     reset = ''
     bold = ''
     underline = ''
  with open('settings.json', "r") as file:
        data = json.load(file)
        token = data["token"]
        channel = data["channel"]
        gm = data["gm"]
        sm = data["sm"]
        pm = data["pm"]
        em = data["em"]
        prefix = data["prefix"]
        allowedid = data["allowedid"]
        webhook = data["webhook"]
        webhookping = data["webhookping"]
        alt = data["alt"]
  if data["token"] and data["channel"] == 'nothing':
   print(f"{color.fail} !!! [ERROR] !!! {color.reset} Please Enter Information To Continue")
   time.sleep(1)
   from newdata import data
   data()
   os.execl(executable, executable, *argv)
  response = requests.get("https://api.github.com/repos/ahihiyou20/discord-selfbot-owo-bot/releases/latest")
  if recentversion in response.json()["name"]:
    print(f"{color.warning}Checking Update... {color.reset}")
    time.sleep(1)
    print(f"{color.okgreen}No Update Available {color.reset}")
  else:
   print(f"{color.warning}Checking Update... {color.reset}")
   time.sleep(1)
   print(f"{color.warning}Update Available {color.reset}")
   print(f"{color.purple}Update Info:{color.reset}")
   time.sleep(0.5)
   print(response.json()["name"])
   print(response.json()["body"])
   choice = input(f"{color.warning}Do You Want To Update (YES/NO): {color.reset}")
   if choice.lower() == "yes":
    import update
   else:
    pass
  print('=========================')
  print('|                       |')
  print(f'| [1] {color.purple}Load data         {color.reset}|')
  print(f'| [2] {color.purple}Create new data   {color.reset}|')
  print(f'| [3] {color.purple}Info              {color.reset}|')
  print('=========================')
  time.sleep(0.5)
choice = None
try:
 print("Automatically Pick Option [1] In 10 Seconds.")
 choice = inputimeout(prompt='Enter Your Choice: ', timeout=10)
except TimeoutOccurred:
 choice = "1"
if (choice == "1"):
      pass
elif (choice == "2"):
 from newdata import data
 data()
elif (choice == "3"):
      print(f"{client.color.purple} =========Support========== {client.color.reset}")
      print(f"{client.color.purple}https://discord.gg/3kTrhbBVQm{client.color.reset}")
      print(" ")
      print(f"{client.color.purple} =========Disclaimer========={client.color.reset}")
      print(f"{client.color.purple}This SelfBot Is Only For Education Purpose Only. Deny All Other Promises Or Responsibilities. Use The SelfBot At Your Own Risk.")
      print(" ")
      print(f'{client.color.purple} =========Credit=========={client.color.reset}')
      print(f'{client.color.purple} [Developer] {client.color.reset} Sudo-Nizel')
      print(f'{client.color.purple} [Developer] {client.color.reset} ahihiyou20')
      print(" ")
      print(f'{client.color.purple} =========Selfbot Commands=========={client.color.reset}')
      print("{Prefix}send {Message} [Send Your Provied Message}")
      print("{Prefix}restart [Restart The Selfbot]")
      print("{Prefix}exit [Stop The Selfbot]")
      print("{Prefix}sm {on/off} [Turn On Or Off Sleep Mode]")
      print("{Prefix}em {on/off} [Turn On Or Off Exp Mode]")
      print("{Prefix}pm {on/off} [Turn On Or Off Pray Mode]")
      print("{Prefix}gm {on/off} [Turn On Or Off Gems Mode]")
      print(" ")
      print("{Prefix} == Your Prefix")
      time.sleep(15)
      exit
else:
 print(f'{client.color.fail} !! [ERROR] !! {client.color.reset} Wrong input!')
 time.sleep(1)
 os.execl(executable, executable, *argv)
def at():
  return f'\033[0;43m{time.strftime("%d %b %Y %H:%M:%S", time.localtime())}\033[0;21m'
bot = discum.Client(token=client.token, log=False)
@bot.gateway.command
def on_ready(resp):
    if resp.event.ready_supplemental: #ready_supplemental is sent after ready
        user = bot.gateway.session.user
        print("Logged in as {}#{}".format(user['username'], user['discriminator']))
@bot.gateway.command
def security(resp):
 if client.webhook != 'None':
  if issuechecker(resp) == "captcha":
    client.stopped = True
    user = bot.gateway.session.user
    if client.webhookping != 'None':
     sentwebhook = DiscordWebhook(url=client.webhook, content='<@{}> I Found A Captcha In Channel: <#{}>'.format(client.webhookping,client.channel))
     response = sentwebhook.execute()
     bot.gateway.close()
    else:
     sentwebhook = DiscordWebhook(url=client.webhook, content='<@{}> <@{}> I Found A Captcha In Channel: <#{}>'.format(user['id'],client.allowedid,client.channel))
     response = sentwebhook.execute()
     bot.gateway.close()
 if client.webhook == 'None':
  if issuechecker(resp) == "captcha":
   client.stopped = True
   bot.gateway.close()
@bot.gateway.command
def issuechecker(resp):
 if resp.event.message:
   m = resp.parsed.auto()
   if m['channel_id'] == client.channel and client.stopped != True:
    if m['author']['id'] == '408785106942164992' or m['author']['username'] == 'OwO' or m['author']['discriminator'] == '8456' or m['author']['public_flags'] == '65536':
     if 'captcha' in m['content'].lower():
       print(f'{at()}{client.color.warning} !! [CAPTCHA] !! {client.color.reset} CAPTCHA   ACTION REQUİRED')
       return "captcha"
     if '(2/5)' in m['content'].lower():
       print(f'{at()}{client.color.warning} !! [CAPTCHA] !! {client.color.reset} CAPTCHA   ACTION REQUİRED (2/5)')
       return "captcha"
     if '(3/5)' in m['content'].lower():
       print(f'{at()}{client.color.warning} !! [CAPTCHA] !! {client.color.reset} CAPTCHA   ACTION REQUİRED (3/5)')
       return "captcha"
     if '(4/5)' in m['content'].lower():
       print(f'{at()}{client.color.warning} !! [CAPTCHA] !! {client.color.reset} CAPTCHA   ACTION REQUİRED (4/5)')
       return "captcha"
     if '(5/5)' in m['content'].lower():
       print(f'{at()}{client.color.warning} !! [CAPTCHA] !! {client.color.reset} CAPTCHA   ACTION REQUİRED (5/5)')
       return "captcha"
     if 'banned' in m['content'].lower():
       print(f'{at()}{client.color.fail} !!! [BANNED] !!! {client.color.reset} your account have been banned from owo bot please open a issue on the Support Discord server')
       return "captcha"
     if 'complete your captcha to verify that you are human!'  in m['content']:
       print(f'{at()}{client.color.warning} !! [CAPTCHA] !! {client.color.reset} CAPTCHA   ACTION REQUİRED')
       return "captcha"
     if 'DM' in m['content'].lower():
       print(f'{at()}{client.color.warning} !! [CAPTCHA] !! {client.color.reset} CAPTCHA   ACTION REQUİRED')
       return "captcha"
def runner():
  if client.stopped != True:
        global wbm
        command=random.choice(client.commands)
        command2=random.choice(client.commands)
        bot.typingAction(str(client.channel))
        bot.sendMessage(str(client.channel), command)
        print(f"{at()}{client.color.okgreen} [SENT] {client.color.reset} {command}")
        client.totalcmd += 1
        if not command2==command and client.stopped != True:
          bot.typingAction(str(client.channel))
          time.sleep(13)
          bot.sendMessage(str(client.channel), command2)
          print(f"{at()}{client.color.okgreen} [SENT] {client.color.reset} {command2}")
          client.totalcmd += 1
        time.sleep(random.randint(wbm[0],wbm[1]))
def owoexp():
 if client.stopped != True:
  if client.em == "YES":
        global wbm
        try:
         response = requests.get("https://quote-garden.herokuapp.com/api/v3/quotes/random")
         if response.status_code == 200:
           json_data = response.json()
           data = json_data['data']
           bot.sendMessage(str(client.channel), data[0]['quoteText'])
           client.totaltext = client.totaltext + 1
           time.sleep(random.randint(1,6))
         else:
           pass
        except:
           pass
 if client.em == "NO":
        pass
def owopray():
 if client.stopped != True:
  if client.pm == "YES":
    bot.sendMessage(str(client.channel), "owo pray")
    print(f"{at()}{client.color.okgreen} [SENT] {client.color.reset} owo pray")
    client.totalcmd += 1
    time.sleep(13)
 if client.pm == "NO":
   pass
def gems():
 if client.stopped != True:
  if client.gm == "YES":
    bot.typingAction(str(client.channel))
    time.sleep(5)
    bot.sendMessage(str(client.channel), "owo inv")
    print(f"{at()}{client.color.okgreen} [SENT] {client.color.reset} owo inv")
    client.totalcmd += 1
    time.sleep(7)
    msgs=bot.getMessages(str(client.channel), num=5)
    msgs=json.loads(msgs.text)
    inv = 0
    length = len(msgs)
    i = 0
    while i < length:
     if msgs[i]['author']['id']=='408785106942164992' and 'Inventory' in msgs[i]['content']:
        inv=re.findall(r'`(.*?)`', msgs[i]['content'])
        i = length
     else:
        i += 1
    if not inv:
       time.sleep(5)
    else:
      if '50' in inv:
        bot.sendMessage(str(client.channel), "owo lb all")
        print(f"{at()}{client.color.okgreen} [SENT] {client.color.reset} owo lb all")
        time.sleep(13)
        gems()
        return
      if '100' in inv:
        bot.sendMessage(str(client.channel), "owo crate all")
        print(f"{at()}{client.color.okgreen} [SENT] {client.color.reset} owo crate all")
        time.sleep(2)
      for item in inv:
        try:
          if int(item) > 100:
            inv.pop(inv.index(item)) #weapons
        except: #backgounds etc
          inv.pop(inv.index(item))
      tier = [[],[],[]]
      print(f"{at()}{client.color.okblue} [INFO] {client.color.reset} Found {len(inv)} gems Inventory")
      for gem in inv:
        gem = re.sub(r"[^a-zA-Z0-9]", "", gem)
        gem = int(float(gem))
        if 50 < gem < 58:
          tier[0].append(gem)
        elif 64 < gem < 72:
          tier[1].append(gem)
        elif 71 < gem <	 79:
          tier[2].append(gem)
      for level in range(0,3):
        if not len(tier[level]) == 0 and client.stopped != True:
          bot.sendMessage(str(client.channel), "owo use "+str(max(tier[level])))
          print(f"{at()}{client.color.okgreen} [SENT] {client.color.reset} owo use {str(max(tier[level]))}")
          time.sleep(7)
 if client.gm == "NO":
      pass
def quests():
 if client.stopped != True:
  if client.alt != "None":
    bot.typingAction(str(client.channel))
    time.sleep(5)
    bot.sendMessage(str(client.channel), "owo quest")
    print(f"{at()}{client.color.okgreen} [SENT] {client.color.reset} owo quest")
    client.totalcmd += 1
    time.sleep(7)
    msgs=bot.getMessages(str(client.channel), num=5)
    msgs=json.loads(msgs.text)
    quest = ""
    length = len(msgs)
    i = 0
    while i < length:
     if msgs[i]['author']['id']=='408785106942164992' and msgs[i]['content'] == "" and 'Quest Log' in msgs[i]['embeds'][0]['author']['name']:
        quest = msgs[i]['embeds'][0]['description']
        i = length
     else:
        i += 1
    if not quest:
       time.sleep(5)
    else:
          if "Have a friend pray to you" in quest:
              print(f"{at()}{client.color.okblue} [INFO]{client.color.reset} Doing Pray Quest(s)...")
              bot.sendMessage("465978474163601436", "owo quest")
              time.sleep(30)
          elif "Gamble" in quest:
              print(f"{at()}{client.color.okblue} [INFO]{client.color.reset} Doing Gamble Quest(s)...")
              bot.senMessage(str(client.channel), "owo cf 1")
          elif "Use an action command on someone" in quest:
              print(f"{at()}{client.color.okblue} [INFO]{client.color.reset} Doing Action Commands Quest(s)...")
              bot.sendMessage(str(client.channel), "owo kill <@{}>".format(client.alt))
          elif "Have a friend curse you" in quest:
              print(f"{at()}{client.color.okblue} [INFO]{client.color.reset} Doing Curse Quest(s)...")
              bot.sendMessage("465978474163601436", "owo quest")
              time.sleep(30)
          elif "Receive a cookie" in quest:
              print(f"{at()}{client.color.okblue} [INFO]{client.color.reset} Doing Cookie Quest(s)...")
              bot.sendMessage("465978474163601436", "owo quest")
              time.sleep(30)
          elif "Have a friend use an action command on you" in quest:
              print(f"{at()}{client.color.okblue} [INFO]{client.color.reset} Doing Action Commands Quest(s)...")
              bot.sendMessage("465978474163601436", "owo quest")
          elif "Say 'owo'" in quest:
              print(f"{at()}{client.color.okblue} [INFO]{client.color.reset} Doing Say 'OwO' Quest(s)...")
              bot.sendMessage(str(client.channel), "owo")
          else:
              print(f"{at()}{client.color.okcyan} [INFO]{client.color.reset} Found No Quests")
@bot.gateway.command
def othercommands(resp):
 prefix = client.prefix
 if resp.event.message:
   m = resp.parsed.auto()
   if m['author']['id'] == bot.gateway.session.user['id'] or m['channel_id'] == client.channel and m['author']['id'] == client.allowedid:
    if prefix == "None":
     bot.gateway.removeCommand(othercommands)
     return
    if "{}send".format(prefix) in m['content'].lower():
     message = m['content'][6::]
     bot.sendMessage(str(m['channel_id']), message)
     print(f"{at()}{client.color.okgreen} [SENT] {client.color.reset} {message}")
    if "{}restart".format(prefix) in m['content'].lower():
     bot.sendMessage(str(m['channel_id']), "Restarting...")
     print(f"{client.color.okcyan} [INFO] Restarting...  {client.color.reset}")
     time.sleep(1)
     os.execl(executable, executable, *argv)
    if "{}exit".format(prefix) in m['content'].lower():
     bot.sendMessage(str(m['channel_id']), "Exiting...")
     print(f"{client.color.okcyan} [INFO] Exiting...  {client.color.reset}")
     bot.gateway.close()
    if "{}gm".format(prefix) in m['content'].lower():
     if "on" in m['content'].lower():
      client.gm = "YES"
      bot.sendMessage(str(m['channel_id']), "Turned On Gems Mode")
      print(f"{client.color.okcyan}[INFO] Turned On Gems Mode{client.color.okcyan}")
     if "off" in m['content'].lower():
      client.gm = "NO"
      bot.sendMessage(str(m['channel_id']), "Turned Off Gems Mode")
      print(f"{client.color.okcyan}[INFO] Turned Off Gems Mode{client.color.okcyan}")
    if "{}pm".format(prefix) in m['content'].lower():
      if "on" in m['content'].lower():
       client.pm = "YES"
       bot.sendMessage(str(m['channel_id']), "Turned On Pray Mode")
       print(f"{client.color.okcyan}[INFO] Turned On Pray Mode{client.color.reset}")
      if "off" in m['content'].lower():
       client.pm = "NO"
       bot.sendMessage(str(m['channel_id']), "Turned Off Pray Mode")
       print(f"{client.color.okcyan}[INFO] Turned Off Pray Mode{client.color.reset}")
    if "{}sm".format(prefix) in m['content'].lower():
      if "on" in m['content'].lower():
       client.sm = "YES"
       bot.sendMessage(str(m['channel_id']), "Turned On Sleep Mode")
       print(f"{client.color.okcyan}[INFO] Turned On Sleep Mode{client.color.reset}")
      if "off" in m['content'].lower():
       client.sm = "NO"
       bot.sendMessage(str(m['channel_id']), "Turned Off Sleep Mode")
       print(f"{client.color.okcyan}[INFO] Turned Off Sleep Mode{client.color.reset}")
    if "{}em".format(prefix) in m['content'].lower():
      if "on" in m['content'].lower():
       client.em = "YES"
       bot.sendMessage(str(m['channel_id']), "Turned On Exp Mode")
       print(f"{client.color.okcyan}[INFO] Turned On Sleep Mode{client.color.reset}")
      if "off" in m['content'].lower():
       client.em = "NO"
       bot.sendMessage(str(m['channel_id']), "Turned Off Exp Mode")
       print(f"{client.color.okcyan}[INFO] Turned Off Sleep Mode{client.color.reset}")
@bot.gateway.command
def loopie(resp):
 if resp.event.ready:
  x=True
  pray = 0
  owo=pray
  gem=pray
  quest = pray
  main=time.time()
  while x:
      runner()
      if time.time() - pray > random.randint(300, 600):
        owopray()
        pray=time.time()
      if time.time() - owo > random.randint(5, 15):
        owoexp()
        owo=time.time()
      if time.time() - gem > random.randint(300, 600):
        gems()
        gem=time.time()
      if client.sm == "YES":
       if time.time() - main > random.randint(1000, 2000):
        main=time.time()
        time.sleep(random.randint(500, 700))
      if client.sm == "NO":
       pass
      if time.time() - quest > random.randint(200, 300):
        quests()
        quest = time.time()
def defination1():
  global once
  if not once:
    once=True
    if __name__ == '__main__':
      lol2= Pool(os.cpu_count() - 1)
      lol2.map(loopie)
      lol=Process(target=loopie)
      lol.run()
bot.gateway.run(auto_reconnect=True)
@atexit.register
def atexit():
 print(f"{client.color.okgreen}Total Number Of Commands Executed: {client.totalcmd}{client.color.reset}")
 time.sleep(0.5)
 print(f"{client.color.okgreen}Total Number Of Random Text Sent: {client.totaltext}{client.color.reset}")
 time.sleep(0.5)
 print(f"{client.color.purple} [1] Restart {client.color.reset}")
 print(f"{client.color.purple} [2] Support {client.color.reset}")
 print(f"{client.color.purple} [3] Exit    {client.color.reset}")
 choice = None
 try:
  print("Automatically Pick Option [3] In 10 Seconds.")
  choice = inputimeout(prompt='Enter Your Choice: ', timeout=10)
 except TimeoutOccurred:
  choice = "4"
 if choice == "1":
  os.execl(executable, executable, *argv)
 elif choice == "2":
  print("Having Issue? Tell Us In Our Support Server")
  print(f"{client.color.purple} https://discord.gg/3kTrhbBVQm {client.color.reset}")
 elif choice == "3":
  bot.gateway.close()
 else:
  bot.gateway.close()
