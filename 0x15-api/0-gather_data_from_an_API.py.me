#!/usr/bin/python3
""" Write a Python script that, using this REST API
for a given employee ID
returns information about his/her TODO list progress """
import requests
import sys


def fetch_user(user_id):
    url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    response = requests.get(url)

    if response.status_code == 200:
        """ you can handle error """
        return response.json()


def fetch_todos(user_id):
    url = f"https://jsonplaceholder.typicode.com/todos"
    response = requests.get(url, params={"userId": user_id})

    if response.status_code == 200:
        """ you can handle error """
        return response.json()


if __name__ == "__main__":
    """ u can handle input error """
    user_id = sys.argv[1]

    """ u can check if its a digit by isdigit() """
    user = fetch_user(user_id)
    todos = fetch_todos(user_id)

    completed = [
            todo.get("title") for todo in todos if todo.get("completed")
            ]
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(completed), len(todos)))
    for complete in completed:
        print(f"\t {complete}")
