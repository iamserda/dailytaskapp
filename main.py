from helpers import add, edit, mark_complete, exit as x, show_completed_tasks as showc, show_open_tasks as showo


def main():
    """
    summary: 
    Daily task list app. Keep a tab on your day via the command line.

    Raises:
        ValueError: 
        If user enters something that's not an option on the menu, 
        we raise a ValueError and offer the user the option to try again or end the program.
    Returns None.
    """
    menu_option_prompt = """
Select an option from this menu:
    '1' or 'add'            - To add a new item.
    '2' or 'edit'           - To modify an item.
    '3' or 'complete'       - To mark a task as completed.
    '4' or 'show -open'           - To show the list of open tasks.
    '5' or 'show -completed'- To show the list of completed tasks.
    '9' or 'x' or 'exit'    - To exit.\n"""

    flag = True
    
    while flag:
        try:
            user_input = input(
                "".join([menu_option_prompt, "\nPlease enter your selection: "]))
            if not user_input:
                local_message = "You did not enter a value.\nNo changes made, ending Program!"
                raise ValueError(local_message)

            match user_input:
                case 'x':
                    flag = x()
                case '0':
                    flag = x()
                case'exit':
                    flag = x()
                case '1':
                    flag = add()
                case 'add':
                    flag = add()
                case '2':
                    flag = edit()
                case 'edit':
                    flag = edit()
                case '3':
                    flag = mark_complete()
                case 'complete':
                    flag = mark_complete()
                case '4':
                    flag = showo()
                case 'show -open':
                    flag = showo()
                case '5':
                    showc()
                case 'show -completed':
                    showc()
                case _:
                    # ~ default case:
                    raise ValueError("'_' is not a valid value.")
            if not flag:
                raise TypeError("User input error! see previous message.")
            print("Message: Success!")
            continue

        except Exception as err:
            print("Error:", err)
            flag = True if input('Would you like to try again? Enter Yes or No: ').lower() == 'yes' else False
            if not flag:
                print("Ending Program...")
                break
            continue
main()
