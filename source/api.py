import requests
from sys import exit
username = input("Enter Your Username: ")
token = input("Enter Authorize Token: ")
at = input("Secret Token: ")
r = requests.get('https://Key-API.vien12345678.repl.co/user?token={}'.format(at))
if r.status_code == 404:
 exit("Invalid Secret Token")
try:
  if token == r.json()[username]:
    print("Successfuly Logged In !")
  else:
    exit("Invalid Authorize Token")
except KeyError:
  exit("Invalid Username")
