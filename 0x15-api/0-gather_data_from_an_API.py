#!/usr/bin/python3
"""
This script retrieves the TODO list progress for a specified employee 
from a REST API and displays it.
"""

from sys import argv
import requests

def main():
    if len(argv) < 2:
        print("Usage: script.py <employeeID>")
        return

    try:
        employeeID = int(argv[1])
    except ValueError:
        print("Employee ID must be an integer.")
        return

    api_link = f'https://jsonplaceholder.typicode.com/users/{employeeID}'
    response = requests.get(api_link)

    if not response.ok:
        print("Failed to retrieve employee data.")
        return

    employeeData = response.json()

    tasks_url = f'https://jsonplaceholder.typicode.com/users/' \
                f'{employeeID}/todos'
    tasks_response = requests.get(tasks_url)

    if not tasks_response.ok:
        print("Failed to retrieve tasks data.")
        return

    tasksData = tasks_response.json()

    employeeName = employeeData.get('name', 'N/A')
    totalTasks = len(tasksData)
    completedTasks = sum(task.get('completed', False) for task in tasksData)

    outputString = (f"Employee {employeeName} is done with tasks"
                    f"({completedTasks}/{totalTasks}):")
    for task in tasksData:
        if task.get('completed', False):
            outputString += f"\n\t {task.get('title', 'No Title')}"

    print(outputString)

if __name__ == "__main__":
    main()
