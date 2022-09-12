#!/usr/bin/python3
"""
Using a REST API, for a given employee ID,
returns information about his/her TODO list progress.
On JSON format.
"""
import json
from requests import get
from sys import argv


if __name__ == "__main__":
    base_url = 'https://jsonplaceholder.typicode.com/users/'
    user_id = argv[1]

    user_url = '{}{}'.format(base_url, user_id)
    todo_url = '{}{}/todos'.format(base_url, user_id)

    user = get(user_url).json()
    all_tasks = get(todo_url).json()

    name = user.get('name')
    name_file = '{}.json'.format(user_id)

    with open(name_file, 'w', encoding='UTF8') as file:
        final_obj = {
            user_id: []
        }
        for task in all_tasks:
            tmp_obj = {
                "task": task.get("title"),
                "completed": task.get("completed"),
                "username": name,
            }
            final_obj[user_id].append(tmp_obj)
        json.dump(final_obj, file, indent=4)
