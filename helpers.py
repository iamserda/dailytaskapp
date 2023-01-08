
def show_list_items(items):
    """Iterates over a items list and displays each value to the usesr.

    Args: items: a python list where we store each tasks as user adds, modifies and delete values.

    Returns:
        bool: _description_
    """
    if not len(items):
        raise Exception("Yay! You have completed all the tasks. There are no task left on your Today's List.")
        return False
    print(f"List Size: {len(items)}")
    print("List Items: ")
    for index, value in enumerate(items): 
            print(f'{index + 1} - {value}')
    print("")
    return True


def show_completed_items(items):
    """Iterates over a items list and displays each value to the usesr.

    Args: items: a python list where we store each tasks as user adds, modifies and delete values.

    Returns:
        bool: _description_
    """
    if not len(items):
        return
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
        user_input = input( 'Select an item from the list above. Use integer only: 1, 2, 3...: ')
        index = int(user_input) if user_input.isnumeric() and int(user_input) < len(tasks_store) else -1
        if index-1 > -1:
            completed_store.append(tasks_store[index-1])
            return True            
        else:
            raise ValueError("Invalid Index!")
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
        user_input = input(message)
        if not user_input.isnumeric():
            message = "User input was an invalid data type. Please enter integer only."
            raise TypeError(message)
        index = int( float( user_input.strip() ) )
        if index < 0 or index > len(tasks_store):
            message = "Invalid Index! Either less than 0 or more than number of available items."
            raise ValueError(message)
        print(tasks_store[index - 1])
        user_input = input("Enter new value: ")
        if not user_input:
            raise ValueError("User didn't enter anything. Item cannot be blank.")
        tasks_store[index - 1] = user_input
        print("Success!")
        return True
    except Exception as err:
        print(err)
        return False

def exit():
    """exit function: ends the applications on user's request.

    Returns: bool: False(always, False terminates the program in main)
    """
    print('exiting...')
    print("Ending Program at User's request!")
    return False

def add(storage_array):
    """ add:
            prompts user for a new item, adds it to the list
            returns true once completed.
    """
    message = "Enter item to be added to list.\nEx: 'Buy a carton of eggs!': "
    user_prompt = input(message)

    if not user_prompt:
        message = "Message: Error Adding new item. User did not enter any value. No changes made."
        raise ValueError(message)

    storage_array.append(user_prompt)
    return True