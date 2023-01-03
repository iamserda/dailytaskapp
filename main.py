task_list_arr = []
menu_option_prompt = """
Menu:
    1 or add to add a new item.
    2 or edit to modify an item.
    3 or complete
    4 or x to exit.
"""


def main():
    flag = True
    show_list_size()

    while flag:
        try:
            user_input = input(menu_option_prompt +
                               "\nPlease enter your selection: ")
            if not user_input:
                show_list_size()
                local_message = "User did not enter any value. No changes made. Ending Program!"
                raise ValueError(local_message)
            if user_input == '4' or user_input == 'x' or user_input == 'exit':
                local_message = "Ending Program at User's request!"
                break

            if user_input == 'add' or user_input == '1':
                flag = add(task_list_arr)
            elif user_input == 'edit' or user_input == '2':
                flag = edit(task_list_arr)
            elif user_input == 'edit' or user_input == '3':
                flag = mark_complete(task_list_arr)
            if flag:
                print("message: Success!")
                print(f"Task List Size: {len(task_list_arr)}")
                continue
        except Exception as err:
            print(err)
            flag = True if input(
                'Would you like to try again? Enter Yes or No: ').lower() == 'yes' else False
            if not flag:
                print(
                    "message: No item was added to the list! User didn't enter. Ending Program!")
                break
            else:
                continue


def add(storage_array):
    """ add:
            prompts user for a new item, adds it to the list
            returns true once completed.
    """
    user_prompt = input(
        "Enter item to be added to list. Ex: 'Buy a carton of eggs!'")

    if not user_prompt:
        raise ValueError(
            "Message: Error Adding new item. User did not enter any value. No changes made.")

    storage_array.append(user_prompt)
    return True

def edit(storage_array):
    """ edit:
        a function to edit an item from the list.
        if the list is empty, it warns the user that editing can only be done on a list that has items.
        else it prints the items, and allow user to select which item should be edited.
    """
#     if not len(storage_array):
#         print("Your current list is empty. You can't edit an empty list. \nPlease add items, and try again.")
    return None

def exit(new_item, arr):
    return None

def mark_complete(storage_array):
    return None


def show_list_size():
    print(f"DailyTask Size: {len(task_list_arr)}")


main()
