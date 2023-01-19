import json


def add(new_item=None):
    """ allows users to ADD a new item to the end of the 'open-tasks' list."""
    try:
        # read any data that was already saved, move a copy to memory.
        data_store = get_data_store('storage/data_store.json')
        open_tasks = data_store['open-tasks']
        # get the new list item from the user, save it into open-tasks.
        if new_item:
            open_tasks.append(new_item)
        # save the open-tasks to a json file.
        set_data_store(data_store)
        return True

    except Exception as err:
        # if there were errors, print them.
        print(f"Error: {err}")
        return False


def basic_editing():
    """ 
        ex: edit 1 Return the bad fruit basket to the grocery store.

        Allows user to edit an item based on its position on the list of open tasks.

        If the list is empty, meaning there are no tasks, it warns the user that editing can only be done on a list.

        Otherwise, it tries locates which items user wants to edit, and updates it accordingly.

        In case where the item, index or location, is out of bound or not available, it throws an error, and returns False.
    """
    try:
        # open file in read mode:
        data_store = get_data_store()
        tasks_store = data_store['open-tasks']
        # editing logic:
        if not len(tasks_store):
            print("Your current list is empty. You can't edit an empty list")
            print("Please add items, and try again.")
            return False

        show_open_tasks(tasks_store)

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
            raise ValueError(
                "User didn't enter anything. Item cannot be blank.")
        tasks_store[index] = user_input
    # save the changes into the json file.
        set_data_store(data_store)
        return True
    except Exception as err:
        print(f'Error: {err}')
        return False


def complex_editing(setup_arr=list()):
    """ 
    ex: edit 1 Return the bad fruit basket to the grocery store.

    Allows user to edit an item based on its position on the list of open tasks.

    If the list is empty, meaning there are no tasks, it warns the user that editing can only be done on a list.

    Otherwise, it tries locates which items user wants to edit, and updates it accordingly.

    In case where the item, index or location, is out of bound or not available, it throws an error, and returns False.
    """
    try:
        data_store = get_data_store()
        tasks_store = data_store['open-tasks']

        if not setup_arr or len(setup_arr) != 3:
            raise ValueError(
                """Please enter the number you want to change, followed by the new value you wish to use as its replacement. For example:\n ex: edit 2 Miami Dolphins """)

        if len(setup_arr) == 3:
            index = int(setup_arr[1]) - 1
            message = setup_arr[2]
            if index > len(tasks_store) or index < 0:
                raise ValueError(f"Invalid position. Next possible location is {len(tasks_store)}.")
            tasks_store[index] = message
            set_data_store(data_store)
        else:
            raise ValueError("")
        return True
    except Exception as err:
        print(f"Error: {err}")
        return False


def mark_complete(index=-1):
    """ Allow users to mark an item on the open tasks list completed. Moves completed task to a different list named "completed-tasks-list." Completed tasks are saved for historical purposes.

    Args:
        tasks_store (list/array): list containing all the open task currently available
        to the user. Task that haven't been completed."""

    data_store = get_data_store('storage/data_store.json')
    tasks_store = data_store['open-tasks']
    completed_store = data_store['completed-tasks']

    if not len(tasks_store):
        print("Your current list is empty. \nPlease add items, and try again.")
        return False

    try:
        if not index:
            raise Exception("Failed to provide a valid index")
        
        index = int(index) - 1
        if index < 0 or index > len(tasks_store) - 1:
            raise Exception(f"The position provided is not valid! Select between 1 and {len(tasks_store)}")

        completed_store.append(tasks_store.pop(index))
        set_data_store(data_store)
        return True
    except Exception as err:
        print(f'Error: {err}')
        return False


def show_open_tasks(task_store=None):
    """Iterates over a items list and displays each value to the usesr.
    Args: items: a python list where we store each tasks as user adds, modifies and delete values.
    Returns:
        bool: _description_
    """
    try:
        data_store = get_data_store()
        items = data_store['open-tasks']

        if not len(items):
            return False
        print("List Items: ")
        for index, value in enumerate(items):
            print(f'{index + 1} - {value}')
        print("\n")
        print(f"Size: {len(items)}\n")
        return True
    except Exception as err:
        print(f"Error: {err}")


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
    print(f"Completed Tasks List: \nSize: {len(items)}\nItems:\n")
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


def get_data_store(file_path='storage/data_store.json'):
    read_fs = open(file_path, 'r')
    data_store = json.load(read_fs)  # this is a python dictionary object
    read_fs.close()
    return data_store


def set_data_store(data_store, file_path='storage/data_store.json'):
    write_fs = open(file_path, 'w')
    json.dump(data_store, write_fs, indent=4)
    write_fs.close()
