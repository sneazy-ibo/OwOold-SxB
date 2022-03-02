import requests
from sys import exit
username = input("Enter Your Username: ")
token = input("Enter Authorize Token: ")
at = input("Secret Token: ")
try:
 r = requests.get('https://Key-API.vien12345678.repl.co/user?token={}'.format(at),timeout=10)
except requests.exceptions.Timeout:
 print("Something Went Wrong! Please Try Again!")
 exit
try:
 if token == r.json()[username]:
   print("Successfuly Logged In !")
 else:
   print("Invalid Authorize Token")
   exit
except KeyError:
  print("Invalid Username")
  exit
except requests.exceptions.JSONDecodeError:
  print("Invalid Secret Token!")
