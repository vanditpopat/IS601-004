from datetime import datetime
import json
import os

tasks = []
# constant, don't edit, use .copy()
TASK_TEMPLATE = {
    "name":"",
    "due": None, # datetime
    "lastActivity": None, # datetime
    "description": "",
    "done": False # False if not done, datetime otherise
}

# don't edit, intentionaly left an unhandled exception possibility
def str_to_datetime(datetime_str):
    """ attempts to convert a string in one of two formats to a datetime
    Valid formats (visual representation): mm/dd/yy hh:mm:ss or yyyy-mm-dd hh:mm:ss """
    try:
        return datetime.strptime(datetime_str, '%m/%d/%y %H:%M:%S')
    except:
        return datetime.strptime(datetime_str, '%Y-%m-%d %H:%M:%S')

def save():
    """ writes the tasks list to a json file to persist changes """
    f = open("tracker.json", "w")
    f.write(json.dumps(tasks, indent=4, default=str))
    f.close()

def load():
    """ loads the task list from a json file """
    if not os.path.isfile("tracker.json"):
        return
    f = open("tracker.json", "r")
    
    data = json.load(f)
    # Note about global keyword: https://stackoverflow.com/a/11867510
    global tasks
    tasks = data
    f.close()
    print(f"data {data}")    

def list_tasks(_tasks):
    """ List a summary view of all tasks """
    i = 0
    for t in _tasks:
        print(f"{i+1}) [{'x' if t['done'] else ' '}] Task: {t['name']} (Due: {t['due']})")
        i += 1
    if len(_tasks) == 0:
        print("No tasks to show")

# edits should happen below this line
def outofbound(index):
    task = {
        'check' : True,
        'mess' : []
    }

    try:
        task['check'] = True
        task['mess'] = tasks[index]
    except IndexError:
        task['check'] = False
        task['mess'] = "Index out of bound"
    
    return task

# def checkdate(due):
#     task = {
#         'check' : True,
#         'mess' : []
#     }

#     try:
#         task['check'] = True
#     except ValueError:
#         task['check'] = False
#         task['mess'] = "Invalid Format for date"
    
#     return task


def add_task(name: str, description: str, due: str):
    """ Copies the TASK_TEMPLATE and fills in the passed in data then adds the task to the tasks list """
    # VP645 02/20/2023 In this add task method I use the if conditions to check if the input is provided correctly
    #update the last Activity to the current datetime and add all this to the global variable tasks
    # Print a message to say the task is successfull and save it.
    task = TASK_TEMPLATE.copy() # don't delete this
    task["lastActivity"] = datetime.now()
    if len(name) == 0 and len(due) == 0 and len(description) == 0:
        print("Enter a Valid Input for the task")
    else:
        task["name"] = name
        task["due"] = due
        task["description"] = description
        tasks.append(task)
        print("New Task Added")
    save()

def process_update(index):
    """ extracted the user input prompts to get task data then passes it to update_task() """
    
    # get the task by index
    # consider index out of bounds scenarios and include appropriate message(s) for invalid index
    # show the existing value of each property where the TODOs are marked in the text of the inputs (replace the TODO related text)
    # include your ucid and date as a comment of when you implemented this, briefly summarize the solution
    task = outofbound(index)
    if not task['check']:
        print(task['mess'])
    else:
        name = input(f"What's the name of this task? {tasks[index]['name']} \n").strip()
        desc = input(f"What's a brief descriptions of this task? {tasks[index]['description']} \n").strip()
        due = input(f"When is this task due (format: m/d/y H:M:S) ({tasks[index]['due']}) \n").strip()
        update_task(index, name=name, description=desc, due=due)

def update_task(index: int, name: str, description:str, due: str):
    """ Updates the name, description , due date of a task found by index if an update to the property was provided """
    # VP645 02/20/2023 Here I am getting the task by Id and then trying to update the task, firstly I check if the input i provided or not 
    # Then I also check whether the input provided is different to the initial value and update the last Activity accordingly
    task = outofbound(index)
    if not task['check']:
        print(task['mess'])
    elif len(name) == 0 and len(description) == 0 and len(due) == 0 :
            print("Nothing was updated") 
    else:
        if tasks[index]['name'] != name and len(name) !=0:
            tasks[index]['name'] = name
            tasks[index]['lastActivity'] = datetime.now()
        elif tasks[index]['description'] != description and len(description) !=0 :
            tasks[index]['description'] = description
            tasks[index]['lastActivity'] = datetime.now()
        elif tasks[index]['due'] != due and len(due) !=0 :
            tasks[index]['due'] = due
            tasks[index]['lastActivity'] = datetime.now()
        print("Updates Were Made")
    save()

def mark_done(index):
    """ Updates a single task, via index, to a done datetime"""
    #VP645 02/20/2023 Here I basically find the task by index if not present send a message and if present 
    #change the done to present time
    task = outofbound(index)
    if not task['check']:
        print(task['mess'])
    elif not tasks[index]['done']:
        tasks[index]['done'] = datetime.now()
        print("Marked as done")
    
    else:
        print("The Task is Already Completed")
    save()

def view_task(index):
    """ View more info about a specific task fetch by index """
    #VP645 02/20/2023 Here I check for the index first if present I just take that dictionar and print it out using print statement
    task = outofbound(index)
    if not task['check']:
        print(task['mess'])
    else:    
        task = {}
        task[index] = tasks[index]
        print(f"""
        [{'x' if task[index]['done'] else ' '}] Task: {task[index]['name']}\n 
        Description: {task[index]['description']} \n 
        Last Activity: {task[index]['lastActivity']} \n
        Due: {task[index]['due']}\n
        Completed: {task[index]['done'] if task[index]['done'] else '-'} \n
        """.replace('  ', ' '))


def delete_task(index):
    """ deletes a task from the tasks list by index """
    # VP645 02/20/2023/ delete/remove task from list by index and consider out of bound using del function call
    task = outofbound(index)
    if not task['check']:
        print(task['mess'])
    else:
        del tasks[index]
        print("Task Deleted Successfully")
    save()

def get_incomplete_tasks():
    """ prints a list of tasks that are not done """
    # VP645 02/20/2023 Here I iterate through the list and check if done is still false if yes
    # Append that task to a different list and then print that list out if not then print that message
    _tasks = []
    for i in tasks:
        if not i['done']:
            _tasks.append(i)
    list_tasks(_tasks)

def get_overdue_tasks():
    """ prints a list of tasks that are over due completion (not done and expired) """
    # VP645 02/20/2023 This shows the overdue task by checking if the done attribute is false and the due date is before today
    # If so show the task or else the message of no such tasks
    _tasks = []
    for i in tasks:
        if not i['done'] and datetime.strptime(i['due'],'%m/%d/%y %H:%M:%S') < datetime.now():
            _tasks.append(i)
    list_tasks(_tasks)

def get_time_remaining(index):
    """ outputs the number of days, hours, minutes, seconds a task has before it's overdue otherwise shows similar info for how far past due it is """
    # VP645 02/20/2023 Get task by id and when present convert the now to the format and then subtract that from due
    # Get the days using .days and seconds using .second and then find hours minutes left to that day and display it
    # Also check for overdue assignment
    task = {}
    task = outofbound(index)
    if not task['check']:
        print(task['mess'])
    else:
        now = datetime.now()
        a = now.strftime('%m/%d/%y %H:%M:%S')
        c = datetime.strptime(a, '%m/%d/%y %H:%M:%S')
        b = datetime.strptime(tasks[index]['due'] , '%m/%d/%y %H:%M:%S')
        value = b - c
        days , second = value.days, value.seconds
        hours = days * 24 + second
        minute = (second % 3600)
        second = second % 60
        dayss = int(days)
        if days < 0:
            print(f"The Task is overdue by {abs(days)} days, {hours} hours, {minute} minutes, {second} seconds")
        else:
            print(f"The time remaining is {days} days, {hours} hours, {minute} minutes, {second} seconds")
    
# no changes needed below this line

command_list = ["add", "view", "update", "list", "incomplete", "overdue", "delete", "remaining", "help", "quit", "exit", "done"]
def print_options():
    """ prints a readable list of commands that can be typed when prompted """
    print("Choices")
    print("add - Creates a task")
    print("update - updates a specific task")
    print("view - see more info about a task by number")
    print("list - lists tasks")
    print("incomplete - lists incomplete tasks")
    print("overdue - lists overdue tasks")
    print("delete - deletes a task by number")
    print("remaining - gets the remaining time of a task by number")
    print("done - marks a task complete by number")
    print("quit or exit - terminates the program")
    print("help - shows this list again")

def run():
    """ runs the program until terminated or a quit/exit command is used """
    print("Welcome to Task Tracker!")
    load()
    print_options()
    while(True):
        opt = input("What would you like to do?\n").strip() # strip removes whitespace from beginning/end
        if opt not in command_list:
            print("That's not a valid option")
        elif opt == "add":
            name = input("What's the name of this task?\n").strip()
            desc = input("What's a brief descriptions of this task?\n").strip()
            due = input("When is this task due (visual format: mm/dd/yy hh:mm:ss)\n").strip()
            add_task(name, desc, due)
        elif opt == "view":
            num = int(input("Which task do you want to view? (hint: number from 'list') ").strip())
            index = num-1
            view_task(index)
        elif opt == "update":
            num = int(input("Which task do you want to update? (hint: number from 'list') ").strip())
            index = num-1
            process_update(index)
        elif opt == "done":
            num = int(input("Which task do you want to complete? (hint: number from 'list') ").strip())
            index = num-1
            mark_done(index)
        elif opt == "list":
            list_tasks(tasks)
        elif opt == "incomplete":
            get_incomplete_tasks()
        elif opt == "overdue":
            get_overdue_tasks()
        elif opt == "delete":
            num = int(input("Which task do you want to delete? (hint: number from 'list') ").strip())
            index = num-1
            delete_task(index)
        elif opt == "remaining":
            num = int(input("Which task do you like to get the duration for? (hint: number from 'list') ").strip())
            index = num-1
            get_time_remaining(index)
        elif opt in ["quit", "exit"]:
            print("Good bye.")
            quit()
        elif opt == "help":
            print_options()
        
if __name__ == "__main__":
    run()