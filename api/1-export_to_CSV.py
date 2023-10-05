#!/usr/bin/python3
import csv
import requests
import sys

employee_id = int(sys.argv[1])

# Get employee details
response = requests.get(f"https://jsonplaceholder.typicode.com/users/{employee_id}")
employee_details = response.json()
employee_name = employee_details["username"]

# Get employee TODO list
response = requests.get(f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos")
todo_list = response.json()

# Write to CSV file
with open(f"{employee_id}.csv", mode="w", newline="") as file:
    writer = csv.writer(file, delimiter=",", quotechar='"', quoting=csv.QUOTE_ALL)
    for task in todo_list:
        writer.writerow([employee_id, employee_name, task["completed"], task["title"]])
