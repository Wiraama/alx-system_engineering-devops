#!/usr/bin/python3
"""Exports to-do list information for a given employee ID to JSON format."""
import json
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: {} <user_id>".format(sys.argv[0]))
        sys.exit(1)

        user_id = sys.argv[1]
        url = "https://jsonplaceholder.typicode.com/"
            
            try:
                user = requests.get(url + "users/{}".format(user_id)).json()
                username = user.get("username")
                todos = requests.get(url + "todos", params={"userId": user_id}).json()

                with open("{}.json".format(user_id), "w") as jsonfile:
                    json.dump(
                            {user_id: [
                                {
                                    "task": t.get("title"),
                                    "completed": t.get("completed"),
                                    "username": username
                                    } for t in todos
                                ]},
                            jsonfile,
                            indent=4  # Pretty-print the JSON data
                            )

            except requests.exceptions.RequestException as e:
                print("Error fetching data:", e)
            except Exception as e:
                print("An error occurred:", e)
