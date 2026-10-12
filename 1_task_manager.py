# project 1: task manager
# a simple to-do list that saves your tasks to a file so they are still there the next time you run it

import json
import os

# the name of the file where tasks are saved
FILE_NAME = "tasks.json"


def load_tasks():
    # if the file does not exist yet, start with an empty list
    if not os.path.exists(FILE_NAME):
        return []

    # try to read the file, and start fresh if something is wrong with it
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            return json.load(file)
    except json.JSONDecodeError:
        print("could not read the tasks file, starting with an empty list")
        return []


def save_tasks(tasks):
    # write the list of tasks into the file
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        json.dump(tasks, file, indent=2)


def show_tasks(tasks):
    if len(tasks) == 0:
        print("no tasks yet")
        return

    # enumerate gives each task a number, starting from 1
    for number, task in enumerate(tasks, start=1):
        if task["done"]:
            status = "[x]"
        else:
            status = "[ ]"
        print(number, status, task["title"])


def add_task(tasks):
    title = input("what is the task? ").strip()

    # do not allow empty tasks
    if title == "":
        print("the task can't be empty")
        return

    # each task is a dictionary with a title and a done flag
    tasks.append({"title": title, "done": False})
    save_tasks(tasks)
    print("task added")


def ask_for_task_number(tasks, question):
    # asks the user for a number and checks it matches a real task
    # returns the position in the list, or None if the number is not valid
    try:
        number = int(input(question))
    except ValueError:
        print("please type a number")
        return None

    if number < 1 or number > len(tasks):
        print("there is no task with that number")
        return None

    # lists start at 0, so we take away 1
    return number - 1


def mark_done(tasks):
    position = ask_for_task_number(tasks, "which task number is done? ")
    if position is not None:
        tasks[position]["done"] = True
        save_tasks(tasks)
        print("nice work, task marked as done")


def delete_task(tasks):
    position = ask_for_task_number(tasks, "which task number do you want to delete? ")
    if position is not None:
        removed = tasks.pop(position)
        save_tasks(tasks)
        print("deleted:", removed["title"])


def main():
    tasks = load_tasks()

    # keep showing the menu until the user chooses to quit
    while True:
        print()
        print("1) add a task")
        print("2) show tasks")
        print("3) mark a task as done")
        print("4) delete a task")
        print("5) quit")
        choice = input("choose 1-5: ").strip()

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            show_tasks(tasks)
        elif choice == "3":
            mark_done(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("bye!")
            break
        else:
            print("please choose a number from 1 to 5")


# this makes the program start when you press run
if __name__ == "__main__":
    main()
