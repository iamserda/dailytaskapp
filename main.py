from helpers import add, edit, show_list_size, mark_complete, exit, show_list_items as show, show_completed_items as show_comp


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
    task_list_arr = []
    completed_task = []
    menu_option_prompt = """
Select an option from this menu:
    '1' or 'add'            - To add a new item.
    '2' or 'edit'           - To modify an item.
    '3' or 'complete'       - To mark a task as completed.
    '4' or 'show -open'           - To show the list of open tasks.
    '5' or 'show -completed'- To show the list of completed tasks.
    '6' or 'x' or 'exit'    - To exit.\n"""

    flag = True
    show_list_size(task_list_arr)

    while flag:
        try:
            user_input = input(
                "".join([menu_option_prompt, "\nPlease enter your selection: "]))
            if not user_input:
                show_list_size(task_list_arr)
                local_message = "You did not enter a value.\nNo changes made, ending Program!"
                raise ValueError(local_message)

            match user_input:
                case 'x':
                    flag = exit()
                case '5':
                    flag = exit()
                case'exit':
                    flag = exit()
                case '1':
                    flag = add(task_list_arr)
                case 'add':
                    flag = add(task_list_arr)
                case '2':
                    flag = edit(task_list_arr)
                case 'edit':
                    flag = edit(task_list_arr)
                case '3':
                    flag = mark_complete(task_list_arr, completed_task)
                case 'complete':
                    flag = mark_complete(task_list_arr, completed_task)
                case '4':
                    flag = show(task_list_arr)
                case 'show -open':
                    flag = show(task_list_arr)
                case '6':
                    show_comp(completed_task)
                case 'show -completed':
                    show_comp(completed_task)
                case _:
                    # ~ default case:
                    print('case _')
                    flag = False
                    raise

            if not flag:
                raise ValueError("Invalid value.")
            
            print("Message: Success!")
            show_list_size(task_list_arr)
            continue

        except Exception as err:
            print("Message:",err)
            flag = True if input(
                'Would you like to try again? Enter Yes or No: ').lower() == 'yes' else False
            if not flag:
                print("Ending Program...")
                break
            continue
    show(task_list_arr)
main()
