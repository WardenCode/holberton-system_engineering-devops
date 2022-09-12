#!/usr/bin/python3
"""
Using a REST API, returns information about
all users TODO list progress.
On JSON format.
"""
import json
from requests import get


if __name__ == "__main__":
    base_url = 'https://jsonplaceholder.typicode.com/users'
    name_file = 'todo_all_employees.json'

    all_users = get(base_url).json()

    with open(name_file, 'w', encoding='UTF8') as file:
        final_obj = {}

        for user in all_users:
            formated_tasks = []
            user_id = user.get("id")
            user_task = get("{}/{}/todos".format(base_url, user_id)).json()
            for task in user_task:
                tmp_obj = {
                    "username": user.get("name"),
                    "task": task.get("title"),
                    "completed": task.get("completed"),
                }
                formated_tasks.append(tmp_obj)
            final_obj[user_id] = formated_tasks
        json.dump(final_obj, file, indent=4)
