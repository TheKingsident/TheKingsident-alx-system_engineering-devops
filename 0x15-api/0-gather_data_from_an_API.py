#!/usr/bin/python3

from sys import argv
import requests

employeeID = argv[1]
api_link = 'https://jsonplaceholder.typicode.com/users/' + employeeID
response = requests.get(api_link)
employeeData = response.json()

tasks_respoonse = requests.get('https://jsonplaceholder.typicode.com/users/' + employeeID + '/todos')
tasksData = tasks_respoonse.json()

employeeName = employeeData['name']
totalTasks = len(tasksData)
completedTasks = sum(task['completed'] for task in tasksData)

outputString = f"Employee {employeeName} is done with tasks({completedTasks}/{totalTasks}):"
for task in tasksData:
    if task['completed']:
        outputString += f"\n\t {task['title']}"


print(outputString)
