#!/usr/bin/python3
"""
Using what you did in the task #0, extend your Python script to export data in the JSON format
"""

import json
import requests
import sys

if __name__ == "__main__":
    USER_ID = sys.argv[1]
    baseUrl = "https://jsonplaceholder.typicode.com/users"
    url = baseUrl + "/" + USER_ID

    response = requests.get(url)
    USERNAME = response.json().get('username')

    todoUrl = url + "/todos"
    response = requests.get(todoUrl)
    tasks = response.json()

    val_lists = []
    for task in tasks:
        val_lists.append({"task": task.get('title'),
                          "completed": task.get('completed'),
                          "username": USERNAME})

    json_dict = {USER_ID: val_lists}
    json_file = USER_ID + ".json"
    with open(json_file, "w") as f:
        json.dump(json_dict, f)
