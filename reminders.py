from math import log10
import re

tasks = []

tasks.append({"content": "Do the dishes", "deadline": "Monday"})
tasks.append({"content": "Hang out the washing", "deadline": "Tuesday"})
tasks.append({"content": "Exercise", "deadline": "Wednesday the 15th of July 2020"})

def tabulate(records):
    # Tabulate a list of records.
    attributes = {}

    # Create a dictionary of all attributes as well as their max value lengths
    for r in records:
        for attr, value in r.items():
            length = len(str(value))
            if attr not in attributes:
                attributes[attr] = length
            else:
                if length > attributes[attr]: attributes[attr] = length

    n_digits = int(log10(len(tasks))) + 2

    # Print the column headings.
    print(" " * (n_digits+2), end="")
    for attr, max in attributes.items():
        print(attr.upper(), end="")
        print(" "*(max-len(attr)+2), end="")
    print()

    # Print each row/record
    i = 1
    for r in records:
        n = str(i)
        print(n + (" " * (n_digits-len(n)+2)), end="")
        i += 1
        for attr in r:
            print(r[attr], end="")
            print(" "*(attributes[attr]-len(r[attr])+2), end="")
        print()

for _ in range(100):
    tasks.append({"content": "oweirngwoeirng", "deadline": "asdiasdg"})

while True:
    cmd = input("Enter a command: ")
    if cmd == "show":
        # Generate and print a table of the reminders.
        if tasks:
            tabulate(tasks)
        else:
            print("No tasks to show. Start by creating a new task.")

    elif cmd == "new":
        content = input("Enter content: ")
        deadline = input("Enter deadline: ")

        tasks.append({"content": content, "deadline": deadline})


    elif re.search(r"^complete \d+$", cmd):
        n = int(re.search(r"^complete (\d+)$", cmd).group(1))
        if n > 0 and n <= len(tasks):
            del(tasks[n-1])
            print("Task %d Completed." % n)
        else:
            print("Task %d does not exist." % n)

    elif cmd == "exit":
        exit()

    else:
        print("ERROR: Unkown command.")
