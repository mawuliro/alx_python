#!/usr/bin/python3
import requests
import sys

url = "http://0.0.0.0:5000/search_user"
letter = sys.argv[1] if len(sys.argv) > 1 else ""

response = requests.post(url, data={'q': letter})

try:
    json_response = response.json()
    if json_response:
        print(f"[{json_response['id']}] {json_response['name']}")
    else:
        print("No result")
except ValueError:
    print("Not a valid JSON")
