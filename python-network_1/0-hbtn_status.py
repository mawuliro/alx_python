#!/usr/bin/python3
import requests

response = requests.get("https://alu-intranet.hbtn.io/status")

print("Body response:")
print("\t- type: {}".format(type(response.content.decode())))
print("\t- content: {}".format(response.content.decode()))
