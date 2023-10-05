#!/usr/bin/python3
import requests
import sys

username = sys.argv[1]
access_token = sys.argv[2]

url = f"https://api.github.com/user"

response = requests.get(url, auth=(username, access_token))

if response.status_code == 200:
    user_data = response.json()
    print(user_data['id'])
else:
    print("None")
