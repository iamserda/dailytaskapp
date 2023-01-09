
def show_list_items(items):
    """Iterates over a items list and displays each value to the usesr.

    Args: items: a python list where we store each tasks as user adds, modifies and delete values.

    Returns:
        bool: _description_
    """
    if not len(items):
        return False
    
    print(f"List Size: {len(items)}")
    print("List Items: ")
    for index, value in enumerate(items):
        print(f'{index + 1} - {value}')
    return True


def show_completed_items(items):
    """Iterates over a items list and displays each value to the usesr.

    Args: items: a python list where we store each tasks as user adds, modifies and delete values.

    Returns:
        bool: _description_
    """
    if not len(items):
        print("You haven't completed any tasks recently.")
        return False
    print( f"Completed Tasks List: \nSize: {len(items)}\nItems:\n")
    for index, value in enumerate(items):
            print(f'{index + 1} - {value}')
    print("")
    return

def show_list_size(tasks_store):
    """Displays the number of open tasks in the console.

    Args:
        tasks_store (list/array): list containing all the open task currently available
        to the user. Task that haven't been completed.
    """
    print(f"Open Tasks Count: {len(tasks_store)}")


def mark_complete(tasks_store, completed_store):
    if not len(tasks_store):
        print("Your current list is empty. \nPlease add items, and try again.")
        return False
    
    try:
        show_list_items(tasks_store)
        user_input = input( 'Select an item from the list above. Use integer only: 1, 2, 3...: ').strip()
        index = int(user_input) if user_input.isnumeric() and int(user_input) < len(tasks_store) else -1
        index = index - 1
        if index < 0 or index > len(tasks_store)-1:
            raise ValueError("Invalid Index!")
        completed_store.append( tasks_store.pop(index-1) )
        return True
    except Exception as err:
        print(f'Error: {err}')
        return False


def edit(tasks_store):
    """ edit:
        a function to edit an item from the list.
        if the list is empty, it warns the user that editing can only be done on a list that has items.
        else it prints the items, and allow user to select which item should be edited.
    """
    if not len(tasks_store):
        print("Your current list is empty. You can't edit an empty list. \nPlease add items, and try again.")
        return False

    show_list_items(tasks_store)
    # ask user which item to edit
    try:
        message = """Which item would you like to edit or replace?
        Please enter an integer only. Ex: 1 for the first item: """
        user_input = input(message).strip()
        
        if not user_input.isnumeric():
            message = "User input was an invalid data type. Please enter integer only."
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
        print("Success!")
        return True
    except Exception as err:
        print(err)
        return False


def exit():
    """ Ends the applications on user's request. Takes no arguments. Always returns False. 
    False should be used to terminate the program inside of main.
    """
    print('exiting...')
    print("Ending Program at User's request!")
    return False


def add(storage_array):
    """ Prompts user for a new item.
    adds it to the list
            returns true once completed.
    """
    message = "Enter item to be added to list.\nEx: 'Buy a carton of eggs!': "
    user_prompt = input(message).strip()

    if not user_prompt:
        message = "Message: Error Adding new item. User did not enter any value. No changes made."
        raise ValueError(message)

    storage_array.append(user_prompt)
    return True


# def open_tasks_to_json(open_tasks):
#     try:
#         import json
#         data = {
#             'open-tasks': open_tasks,
#         }
#         with open('storage/open_tasks.json', 'w') as opentasks:
#             json.dump(data[open_tasks], opentasks)
#         return True

#     except Exception as err:
#         print("Failed to save files as json:")
#         print(f"Error: {err}")
#         return False


# def completed_tasks_to_json(completed_tasks):
#     try:
#         import json
#         data = {
#             'completed-tasks': completed_tasks,
#         }
#         with open('storage/completed_tasks.json', 'w') as completedtasks:
#             json.dump(data[completed_tasks], completedtasks)
#         return True

#     except Exception as err:
#         print("Failed to save files as json:")
#         print(f"Error: {err}")
#         return False