#!/usr/bin/python3
"""Exports to-do list information for a given employee ID to CSV format."""
import csv
import requests
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: {} <user_id>".format(sys.argv[0]))
        sys.exit(1)

        user_id = sys.argv[1]
        url = "https://jsonplaceholder.typicode.com/"

        try:
            user = requests.get(url + "users/{}".format(user_id)).json()
            username = user.get("username")
            todos = requests.get(url + "todos", params={"userId": user_id}).json()

            print("User ID:", user_id)
            print("Username:", username)
            print("Number of tasks:", len(todos))

            with open("{}.csv".format(user_id), "w", newline="") as csvfile:
                writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
                for t in todos:
                    writer.writerow([user_id, username, t.get("completed"), t.get("title")])

        except requests.exceptions.RequestException as e:
            print("Error fetching data:", e)
        except Exception as e:
            print("An error occurred:", e)

if __name__ == "__main__":
    main()
