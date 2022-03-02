import time
import json
import os
def data():
 if os.name == 'nt':
    pass
 if os.name == 'linux':
    import simplejson as json
 else:
    try:
        import json
    except:
        import simplejson as json
 file = open("settings.json", "r")
 data = json.load(file)
 file.close()
 data['token'] = input("Please Enter Your Account Token: ")
 data['channel'] = input("Please Enter Your Channel ID: ")
 data['gm'] = input("Toggle Automatically Use Gems Mode (YES/NO): ")
 data['sm'] = input("Toggle Sleep Mode (YES/NO): ")
 data['em'] = input("Toggle Automatically Send Random Text To Level Up (YES/NO): ")
 data['pm'] = input("Toggle Automatically Send Pray (YES/NO): ")
 data['alt'] = input("Toggle Automatically Do Quests (YES/NO): ")
 if data['alt'] == "YES":
  data['alt'] = input("Enter Your Alternative Account ID To Do Some Specified Quests: ")
 else:
  data['alt'] = "None"
 data['prefix'] = input("Toggle Selfbot Commands, You Can Control Your Selfbot Using Commands (YES/NO): ")
 if data['prefix'] == "YES":
  data['prefix'] = input("Enter Your Selfbot Prefix: ")
  data['allowedid'] = input("Do You Want Allow An User To Use Your Selfbot Commands? If Yes Enter The Account ID, Otherwise Enter \"None\": ")
  print("Great! You Can View Selfbot Commands At Option [3] Info At The Main Menu!")
  time.sleep(1)
 else:
  data['prefix'] = "None"
  data['allowedid'] = "None"
 data['webhook'] = input("Toggle Discord Webhook, Enter Webhook Link If You Want It To Ping You If OwO Asked Captcha. Otherwise Enter \"None\": ")
 if data['webhook'] != "None":
  data['webhookping'] = input("Do You Want To Ping A Specified User When OwO Asked Captcha? If Yes Enter User ID. Otherwise Enter \"None\": ")
 file = open("settings.json", "w")
 json.dump(data, file)
 file.close()
 print('Successfully saved!')
