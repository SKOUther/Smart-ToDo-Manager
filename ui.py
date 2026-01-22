#===================================Libraries====================================
import time, os
#================================================================================

#colors
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
CYAN = "\033[36m"
RESET = "\033[0m"

#================================================================================

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# - - -
#Set a custom downtime
def custom_time(t):
    time.sleep(float(t))

# - - -
#load_text: The download message that will be written gradually.
#load_time: The number of ellipses that will be written next to the previous text.
#show_message: The message that will appear after downloading. Which might be something like "" In some cases.
#show_time: The exact or decimal time for displaying the last message after downloading, Which could be a fraction of a second in some cases.
def loading(load_text, load_time, show_message, show_time):
    for l_text in load_text:
        print(YELLOW + l_text, flush=True, end='' + RESET)
        custom_time(.2)
    for l_time in range(load_time):
        l_time = '.'
        print(l_time, flush=True, end=' ')
        custom_time(.3)
    clear()
    print(GREEN + show_message + RESET)
    custom_time(float(show_time))
    clear()

# - - -
def wait_user():
    print("\n" + "-"*30)
    input("Done reading? Press [Enter] to return to menu...")
    custom_time(.5)

# - - -
def Search_loading():
    print("This may take time...")
    custom_time(1)
    loading("Searching ", 3, "", 0)

#================================================================================