#!/usr/bin/python3
"""
This script retrieves and exports the TODO list progress of all employees
from a REST API. The output is a JSON file with tasks of each employee.
"""

import json
import requests

def fetch_employee_tasks(employeeID):
    """
    Fetch tasks for a specific employee by their ID.
    Returns the username and tasks for the employee.
    Returns None, None if the request fails.
    """
    api_link = ('https://jsonplaceholder.typicode.com/users/'
                f'{employeeID}')
    response = requests.get(api_link)
    if not response.ok:
        return None, None

    employeeData = response.json()
    username = employeeData.get('username', 'N/A')

    tasks_url = ('https://jsonplaceholder.typicode.com/users/'
                 f'{employeeID}/todos')
    tasks_response = requests.get(tasks_url)
    if not tasks_response.ok:
        return None, None

    tasksData = tasks_response.json()
    return username, tasksData

def export_all_to_json(filename):
    """
    Exports all tasks from all employees to a JSON file.
    The file is named as per the provided filename.
    """
    all_tasks = {}
    for employeeID in range(1, 11):
        username, tasks = fetch_employee_tasks(employeeID)
        if username and tasks:
            user_tasks = [{"username": username, "task": task["title"],
                           "completed": task["completed"]}
                          for task in tasks]
            all_tasks[str(employeeID)] = user_tasks

    with open(filename, 'w') as json_file:
        json.dump(all_tasks, json_file)

def main():
    """
    Main function to trigger the export process.
    """
    export_all_to_json('todo_all_employees.json')

if __name__ == "__main__":
    main()
