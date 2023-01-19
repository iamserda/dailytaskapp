from helpers import add, basic_editing, complex_editing, mark_complete
from helpers import show_completed_tasks as showc, show_open_tasks as showo


def main():
    """
    summary: 
    Daily task list app. Keep a tab on your day via the command line.
    
    To add a new item: 'add' or '1'
    
    To modify an item: 'edit' or '2'
    
    To complete a task: 'comp' or '3' 
    
    To show open tasks: 'show', 'showo', 'show -o' or '4'
    
    To show completed tasks: 'showc', 'show -c', or '5'
    
    To exit: 'x', 'exit', '0'
    
    Raises:
        ValueError: 
        If user enters something that's not an option on the menu, 
        we raise a ValueError and offer the user the option to try again or end the program.
    Returns None.
    """
    menu = """Select an option from this menu:
    To add a new item: 'add' or '1'
    To modify an item: 'edit' or '2'
    To complete a task: 'comp' or '3' 
    To show open tasks: 'show', 'showo', 'show -o' or '4'
    To show completed tasks: 'showc', 'show -c', or '5'
    To exit: 'x', 'exit', '0'\n"""

    flag = True

    try:
        while flag:
            user_input = input(
                "".join([menu, "\nPlease enter your selection: "]))
            if not user_input:
                local_message = "You did not enter a value.\nNo changes made, ending Program!"
                raise ValueError(local_message)

            user_input.strip()

            if user_input[0] in ['x', '0', '1', '2', '3', '4', '5']:
                match user_input[0]:
                    case 'x':
                        print("Ending on user's request...")
                        break
                    case '0':
                        print("Ending on user's request...")
                        break
                    case '1':
                        new_item = user_input[2:].strip()
                        flag = add(new_item)
                    case '2': flag = basic_editing()
                    case '3': flag = mark_complete()
                    case '4': flag = showo()
                    case '5': flag = showc()
                    case _:
                        # ~ default case:
                        raise ValueError("'_' is not a valid value.")
            elif user_input.startswith('add'):
                new_item = user_input[3:].strip()
                if new_item:
                    flag = add(new_item)

            elif user_input.startswith('exit'):
                print("Ending on user's request...")
                break
            elif user_input.startswith(('comp', 'complete')):
                setup_arr = user_input.split(" ", maxsplit=2)
                if len(setup_arr) < 2:
                    raise ValueError("User did not provide an index.")
                if not setup_arr[1].isdigit():
                    raise ValueError(
                        "Invalid Index Value provided. Must be a integer.")
                mark_complete(setup_arr[1])
            elif user_input.startswith('edit'):
                # expecting: ['edit', 'index', 'new value'] from the next line.
                setup_arr = user_input.split(" ", maxsplit=2)
                flag = complex_editing(setup_arr)
            elif user_input.startswith('show'):
                match user_input:
                    case 'show': flag = showo()
                    case 'show -o': flag = showo()
                    case 'show -open': flag = showo()
                    case 'showc': flag = showc()
                    case 'show -c': flag = showc()
                    case 'show -completed': flag = showc()
            if not flag:
                raise Exception(
                    "Failed to execute your command! Exiting now...")
    except Exception as err:
        print("Error:", err)


main()
