import json


def add():
    """ Prompts user for a new item.
    adds it to the list
            returns true once completed.
    """
    try:
        # read any data that was already saved, move a copy to memory.
        read_fs = open('storage/data_store.json', 'r')
        data_store = json.load(read_fs) #this is a python dictionary object
        open_tasks = data_store['open-tasks']
        read_fs.close()
        
        #get the new list item from the user, save it into open-tasks.
        message = "Enter item to be added to list.\nEx: 'Buy a carton of eggs!': "
        user_prompt = input(message).strip()
        if not user_prompt:
            message = "Message: Could not add a new item. User did not enter any value. No changes made."
            raise ValueError(message)
        open_tasks.append(user_prompt)
        
        # save the open-tasks to a json file.
        write_fs = open('storage/data_store.json', 'w')
        json.dump(data_store, write_fs, indent=4)
        write_fs.close()
        return True
    except Exception as err:
        # if there were errors, print them.
        print(f"Error: {err}")
        return False


def edit():
    """ edit:
        a function to edit an item from the list.
        if the list is empty, it warns the user that editing can only be done on a list that has items.
        else it prints the items, and allow user to select which item should be edited.
    """
    try:
    # open file in read mode:
        read_fs = open('storage/data_store.json', 'r')
        data_store = json.load(read_fs)
        tasks_store = data_store['open-tasks']
        read_fs.close()
    # editing logic:
        if not len(tasks_store):
            print("Your current list is empty. You can't edit an empty list")
            print("Please add items, and try again.")
            return False

        show_open_tasks()
        
        # ask user which item to edit
        message = """Which item would you like to edit or replace?\n
        Please enter an integer only. Ex: 1 for the first item: """
        user_input = input(message).strip()
        
        if not user_input.isnumeric():
            message = "User input was an invalid data type.\nPlease enter integer only."
            raise TypeError(message)
        
        index = int(user_input) - 1
        if index < 0 or index > len(tasks_store) - 1:
            message = "Invalid Index! Either less than 0 or more than number of open tasks."
            raise ValueError(message)
        
        print(tasks_store[index])
        user_input = input("Enter new value: ")
        if not user_input:
            raise ValueError("User didn't enter anything. Item cannot be blank.")
        tasks_store[index] = user_input
    # save the changes into the json file.
        write_fs = open('storage/data_store.json', 'w')
        json.dump(data_store, write_fs, indent=4)
        write_fs.close()
        return True
    except Exception as err:
        print(f'Error: {err}')
        return False


def mark_complete():
    """ Allow users to mark an item on the open tasks list completed. Moves completed task to a different list named "completed-tasks-list." Completed tasks are saved for historical purposes.

    Args:
        tasks_store (list/array): list containing all the open task currently available
        to the user. Task that haven't been completed.
    """
    read_fs = open('storage/data_store.json')
    data_store = json.load(read_fs)
    tasks_store = data_store['open-tasks']
    completed_store = data_store['completed-tasks']
    read_fs.close()
    
    if not len(tasks_store):
        print("Your current list is empty. \nPlease add items, and try again.")
        return False
    
    try:
        show_open_tasks()
        user_input = input( 'Select an item from the list above. Use integer only: 1, 2, 3...: ').strip()
        index = int(user_input) if user_input.isnumeric() and int(user_input) < len(tasks_store) else -1
        index = index - 1
        if index < 0 or index > len(tasks_store)-1:
            raise ValueError("Invalid Index!")
        completed_store.append( tasks_store.pop(index-1) )
        write_fs = open('storage/data_store.json', 'w')
        json.dump(data_store, write_fs, indent=4)
        write_fs.close()
        return True
    except Exception as err:
        print(f'Error: {err}')
        return False


def exit():
    """
    Ends the applications on user's request. Takes no arguments. Always returns False. 
    False should be used to terminate the program inside of main.
    """
    print('exiting...')
    print("Ending Program at User's request!")
    return False


def show_open_tasks():
    """Iterates over a items list and displays each value to the usesr.
    Args: items: a python list where we store each tasks as user adds, modifies and delete values.
    Returns:
        bool: _description_
    """
    read_fs = open("storage/data_store.json", "r")
    data_store = json.load(read_fs)
    items = data_store['open-tasks']
    
    if not len(items):
        return False
    
    print(f"List Size: {len(items)}")
    print("List Items: ")
    for index, value in enumerate(items):
        print(f'{index + 1} - {value}')
    return True


def show_completed_tasks():
    """
    Iterates over a items list and displays each value to the usesr.
    Args: items: a python list where we store each tasks as user adds, modifies and delete values.
    Returns:
        bool: _description_
    """
    read_fs = open("storage/data_store.json", "r")
    data_store = json.load(read_fs)
    items = data_store['completed-tasks']
    
    if not len(items):
        print("You haven't completed any tasks recently.")
        return False
    print( f"Completed Tasks List: \nSize: {len(items)}\nItems:\n")
    for index, value in enumerate(items):
            print(f'{index + 1} - {value}')
    print("")
    return

def show_list_size(tasks_store):
    """
    Displays the number of open tasks in the console.
    Args:
        tasks_store (list/array): list containing all the open task currently available
        to the user. Task that haven't been completed."""
    print(f"Open Items: {len(tasks_store)}")
