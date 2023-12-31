#!/usr/bin/python3
"""A script to retrieve data in json format
    Args:
        todo_list : data retrieved from the website

    todo:
        json_object: json format
"""

import json
import requests
import sys

if __name__ == "__main__":
    employee_id = int(sys.argv[1])

    # Get employee details
    response = requests.get(f"https://jsonplaceholder.typicode.com/users/{employee_id}")
    employee_details = response.json()
    employee_name = employee_details["username"]

    # Get employee TODO list
    response = requests.get(f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos")
    todo_list = response.json()

    # Create JSON object
    tasks = []
    for task in todo_list:
        tasks.append({"task": task["title"], "completed": task["completed"], "username": employee_name})
    json_obj = {employee_id: tasks}

    # Write to JSON file
    with open(f"{employee_id}.json", mode="w") as file:
        json.dump(json_obj, file)
