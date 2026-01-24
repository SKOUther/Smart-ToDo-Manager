#===================================Libraries====================================
from ui import custom_time, clear, YELLOW, GREEN, RESET
#================================================================================
import os
#---------------------------------------------------------------

#Present the user's task in an organized manner
def display_task(user_task):
    print("\n    ====Confirm Task====\n\n")
    print("      ^Task Preview^\n")
    for key, value in user_task.items():
        print(YELLOW + f"{key:14}" + RESET + ":", GREEN + f"{value}" + RESET)
    print("=" * 30, "\n")

def confirm_action(message):
    try:
        confirm = input(f"{message} y/n: ").lower()
        custom_time(.3)
        clear()
        if confirm in ['y', 'yes', 'yea', 'ya']:
            return 'yes'
        elif confirm in ['n', 'no']:
            return 'no'
        else:
            print("You can only enter yes or no. (y, n).")
            custom_time(1.5)
            return False
    except:
        print("You can only enter a text value.")
        custom_time(1.5)
        return False

def confirm_task(user_task):
    while True:
        display_task(user_task)
        confirm = confirm_action(GREEN + "Save this task?" + RESET)
        if not confirm:
            clear()
            continue
        elif confirm == "yes":
            print(GREEN + "Task has been confirmed." + RESET)
            custom_time(.8)
            clear()
            return True
        else:
            print(GREEN + "This task will be ignored." + RESET)
            custom_time(1.1)
            clear()
            return False

#---------------------------------------------------------------

print(os.path.abspath(__file__))