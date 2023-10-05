import requests
import sys

employee_id = sys.argv[1]

# Get employee details
response = requests.get(f"https://jsonplaceholder.typicode.com/users/{employee_id}")
employee_details = response.json()
employee_name = employee_details["name"]

# Get employee TODO list
response = requests.get(f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos")
todo_list = response.json()

# Calculate progress
total_tasks = len(todo_list)
completed_tasks = sum(1 for task in todo_list if task["completed"])

# Display progress
print(f"Employee {employee_name} is done with tasks({completed_tasks}/{total_tasks}):")
for task in todo_list:
    if task["completed"]:
        print(f"\t {task['title']}")
