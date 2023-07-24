#!/usr/bin/python3
"""
Using what you did in the task #0, extend your Python script
to export data in the JSON format
Requirements:
    Records all tasks from all employees
    Format must be: { "USER_ID": [ {"username": "USERNAME"
    "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS},
    {"username": "USERNAME", "task": "TASK_TITLE", "completed":
    TASK_COMPLETED_STATUS}, ... ], "USER_ID": [ {"username":
    "USERNAME", "task": "TASK_TITLE", "completed":
    TASK_COMPLETED_STATUS}, {"username": "USERNAME", "task":
    "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, ... ]}
    File name must be: todo_all_employees.json
"""

import json
import requests
import sys


if __name__ == '__main__':
    url = "https://jsonplaceholder.typicode.com/users"

    response = requests.get(url)
    users = response.json()

    dictionary = {}
    for user in users:
        user_id = user.get('id')
        username = user.get('username')
        url = 'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)
        url = url + '/todos/'
        response = requests.get(url)
        tasks = response.json()
        dictionary[user_id] = []
        for task in tasks:
            dictionary[user_id].append({
                "task": task.get('title'),
                "completed": task.get('completed'),
                "username": username
            })
    with open('todo_all_employees.json', 'w') as file:
        json.dump(dictionary, file)
