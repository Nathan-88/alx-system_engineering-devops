#!/usr/bin/python3
"""
export data in the CSV format.
"""
import csv
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

    csv_file = USER_ID + ".csv"

    with open(csv_file, mode='w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)

        for task in tasks:
            writer.writerow([USER_ID, USERNAME,
                             task.get('completed'), task.get('title')])
