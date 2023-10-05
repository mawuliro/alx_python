import json
import requests

# Get all employees
response = requests.get("https://jsonplaceholder.typicode.com/users")
employees = response.json()

# Get TODO list for all employees
todo_all_employees = {}
for employee in employees:
    employee_id = employee["id"]
    employee_name = employee["username"]
    response = requests.get(f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos")
    todo_list = response.json()
    tasks = []
    for task in todo_list:
        tasks.append({"username": employee_name, "task": task["title"], "completed": task["completed"]})
    todo_all_employees[employee_id] = tasks

# Write to JSON file
with open("todo_all_employees.json", mode="w") as file:
    json.dump(todo_all_employees, file)
