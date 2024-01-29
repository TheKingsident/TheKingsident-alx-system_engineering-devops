#!/usr/bin/python3
"""
This script retrieves the TODO list progress for a specified employee
from a REST API and displays it.
"""

import csv
import json
import requests
from sys import argv


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

    username = employeeData.get('username', 'N/A')
    userID = employeeData.get('id')
    filename = f"{userID}.csv"
    csv_data = []
    for task in tasksData:
        row = [
            task.get("userId", "N/A"),
            username,
            task.get("completed", "N/A"),
            task.get("title", "No Title")
        ]
        csv_data.append(row)

    # Writing data to CSV
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        writer.writerows(csv_data)

    json_filename = f"{userID}.json"
    export_to_json(json_filename, str(userID), tasksData, username)


def export_to_json(filename, user_id, tasks, username):
    json_data = {user_id: [{"task": task["title"],
                            "completed": task["completed"],
                            "username": username} for task in tasks]}
    with open(filename, 'w') as json_file:
        json.dump(json_data, json_file)


if __name__ == "__main__":
    main()
