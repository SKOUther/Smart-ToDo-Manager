#===================================Libraries====================================
from logic import Task, User, is_valid_num, is_valid_title, is_valid_time, is_valid_status
from logic import is_user_available, has_task, ask_for_data
from file_logic import read_task_file_if_true, read_user_file_if_true
from search_logic import search_for_title, search_for_time, search_for_status, do_custom_search, search_by_number
from ui import custom_time, clear, loading, wait_user, RED, GREEN, BLUE, YELLOW, RESET
#================================================================================

clear()

user_task = Task(None, None, None)
user_info = User(None, None, None, None)

user_task.read_tasks_file()
user_info.read_user_file()
user_task.save_tasks()
user_info.save_user()

#loading("Please wait ", 3, "", 0)

time_show = 1
important_edit = False
read_user_file = True

#================================================================================

user_info = ask_for_data(user_info)

#================================================================================

while True:
    clear()

    if isinstance(user_info.age, int):
        if user_info.age < 7:
            print(RED + "Sorry, you are under the age limit, which is 7 years and above." + RESET)
            exit()

    if not user_info.name:
        print("\nwelcome in to-do-list program\n\n".upper())
    else:
        if time_show == 1:
            user_info.say_welcome()

    print("How can we help you?\n")
    
    #FIRST PART
    print(BLUE + "   ---task help:" + RESET)
    print(YELLOW + "   1) Add a task." + RESET)
    print("   2) Update a task.")
    print(RED + "   3) Delete a task." + RESET)
    print("   4) See my list.")
    print(GREEN + "   5) Mark as Completed.\n" + RESET)

    #MIDDEL PART
    print(BLUE + "   ---info help:" + RESET)
    print(YELLOW + "   6) Add my info." + RESET)
    print("   7) See my info.")
    print(RED + "   8) Change my info.\n" + RESET)

    #LAST PART
    print(BLUE + "   ---exit & search:" + RESET)
    print(GREEN + "   9) Search." + RESET)
    print(RED + "   10) Exit.\n" + RESET)

    if important_edit:
        help_with = '8'
    else:
        help_with = is_valid_num(10, "help")

    if not help_with: continue
    
    #===============Verify files=================
    time_show += 1
    user_task.read_tasks_file()
    user_info.read_user_file()

    it_has_wrong_task = read_task_file_if_true()
    if it_has_wrong_task:
        task_numbers = []
        for n in it_has_wrong_task:
            n += 1
            task_numbers.append(str(n))

        print(RED + f"Sorry, task number {', '.join(task_numbers)} gaveing with a wrong value!\nPlease edit\delete task." + RESET)
        custom_time(3.5)
        
        while True:
            try:
                clear()
                edit_delete = input("Type edit/delete: ").lower()

                if edit_delete in ["edit", "e", "ed"]:
                    clear()
                    custom_time(0.5)
                    user_task.update_task(task_numbers)
                    break
                elif edit_delete in ["delete", "d", "de"]:
                    clear()
                    custom_time(0.5)
                    user_task.delete_task()
                    break
                else:
                    print("Type only from the options.")
                    custom_time(1.5)

            except:
                print("Something went wrong! try again.")
                custom_time(1.5)
                continue
        continue
    
    if read_user_file:
        it_has_wrong_info = read_user_file_if_true()
        if it_has_wrong_info:
            print(RED + "Dear user, there's wrong in your:" + RESET)

            for num, all_worngs in enumerate(it_has_wrong_info):
                print(f"{num+1}. ",all_worngs)
                custom_time(.5)
            custom_time(3)
            clear()
            print(GREEN + "We will send you to the edit page to edit your data." + RESET)
            important_edit = True
            read_user_file = False
            custom_time(3)
            continue
    #============================================    

#---------------------------------------------
    #add task
    if help_with == '1':
        user_task_title = is_valid_title(text="new", similar=True)
        custom_time(.8)
        user_task_time = is_valid_time(use_last_time=True, similar=True)
        if user_task_time == "wrong":
            continue
        custom_time(.8)
        user_task_status = is_valid_status(mark=False)
        user_task.add_task(user_task_title, user_task_time, user_task_status)
        user_task.save_tasks()
        loading("Adding your task ", 4, "Your task has been added.", 1.2)
        continue

    #update task
    elif help_with == '2':
        user_task.update_task(wrong_time=0)

    #delete task
    elif help_with == '3':
        user_task.delete_task()
        
    #show list tasks
    elif help_with == '4':
        if not user_task.show_tasks(True): continue
        wait_user()
        continue 
        
    #mark task
    elif help_with == '5':
        user_task.mark_tasks()

#---------------------------------------------
    #add user info
    elif help_with == '6':
        if user_info.name:
            print(BLUE + f"Dear user {user_info.name}, You've added your info actually." + RESET)
            custom_time(2.2)
            continue
        user_info = ask_for_data(user_info)

    #print user info
    elif help_with == '7':
        if not is_user_available(user_info): continue
        user_info.show_user_info()
        custom_time(5.5)

    #change user info
    elif help_with == '8':
        if not is_user_available(user_info): continue
        important_edit = False
        read_user_file = True
        while True:
            clear()
            print("\nI want change my:\n")
            print("   1) Name.")
            print(YELLOW + "   2) Age/Birth." + RESET)
            print("   3) Gender.")
            print(RED + "   4) Nothing.\n" + RESET)
            change = is_valid_num(4, "change")

            if not change: continue
            if change == '4': break

            if change == '1':
                user_info.change_user_info("new_name")
                loading("Updating your name ", 4, f"Your name has update to {user_info.name}.", 2)
            elif change == '2':
                user_info.change_user_info("new_age")
                loading("Updating your age ", 6, f"Your age has update to {user_info.age}, And your birth to {user_info.date_birth}", 2.8)
            elif change == '3':
                user_info.change_user_info("new_gender")
                loading("Updating your gender ", 4, f"Your gender has update to {user_info.gender}.", 2)
            else:
                print("sorry, someting went wrong! try again.")
                custom_time(1.5)
                continue

#---------------------------------------------
    #search
    elif help_with == '9':
        data_available = has_task()
        if not data_available: continue
        while True:
            clear()
            print("\nI want to search for:\n")
            print("   1) Title task/s.")
            print("   2) Time task/s.")
            print("   3) Status task/s.")
            print(YELLOW + "   4) Comprehensive/Customized Search." + RESET)
            print(YELLOW + "   5) By task number." + RESET)
            print(RED + "   6) Nothing.\n" + RESET)
            try:
                search_for = is_valid_num(6, "search")
                if not search_for: continue

                #title search
                if search_for == '1':
                    title_search = is_valid_title("searching", similar=False)
                    if not title_search: continue

                    search = search_for_title(title_search)
                    custom_time(.5)
                    if not search:
                        print("Sorry, we couldn't find a similar task.")
                        custom_time(1.5)
                        print("Or you can view your task list to confirm the name of the task you want,\nThen try again.")
                        custom_time(2.8)
                        continue
                    if search:
                       wait_user()
                       continue 

                #time search
                elif search_for == '2':
                    time_search = is_valid_time(True, False)
                    if not time_search: continue

                    if len(time_search) > 4:
                        time_search = time_search[11:] 
                    search = search_for_time(time_search)
                    custom_time(.5)
                    if not search:
                        print("Sorry, we couldn't find a similar task.")
                        custom_time(1.5)
                        print("Or make sure to check your task list first.")
                        custom_time(2)
                        continue
                    if search:
                       wait_user()
                       continue 

                #status search
                elif search_for == '3':
                    status_search = is_valid_status(False)
                    if not status_search: continue

                    search = search_for_status(status_search)
                    custom_time(.5)
                    if not search:
                        print("Sorry, we couldn't find a similar task.")
                        custom_time(1.5)
                        print("Or make sure to type only (completed/not yet), and try again.")
                        custom_time(1.9)
                        continue
                    if search:
                       wait_user()
                       continue 
                
                #custom Search
                elif search_for == '4':
                    while True:
                        title_search = is_valid_title("searching", similar=False)
                        if not title_search: continue
                        time_search = is_valid_time(True, False) 
                        if not time_search: continue
                        if len(time_search) > 4:
                            time_search = time_search[11:] 
                        status_search = is_valid_status(False)
                        if not status_search: continue
                        
                        search = do_custom_search(title_search, time_search, status_search)
                        custom_time(.5)
                        if not search:
                            print("Sorry, we couldn't find a similar task.")
                            custom_time(1.5)
                            continue
                        if search:
                            wait_user()
                            break
                    continue 

                #search by task number
                elif search_for == '5':
                    try:
                        clear()
                        num = int(input("Type task number: "))
                        custom_time(.3)
                        clear()
                        if num <= 0:
                            print("The task number cannot be zero or less.")
                            custom_time(1.5)
                            continue
                        if num > 0:
                            search = search_by_number(num)
                            if not search:
                                print(f"Sorry, we couldn't find a similar task has number {num}.")
                                custom_time(1.9)
                                continue
                            else:
                                wait_user()
                    except:
                        print("Enter only a whole number that is not equal to zero.")
                        custom_time(1.5)
                        continue
                #exit              
                elif search_for == '6': break

                else:
                    print("\nInvalid input. enter a value from options.")
                    custom_time(1.5)
                    continue
            
            except:
                print("\nSorry, something went wrong! try again.")
                custom_time(1.2)
                continue

    #exit...
    elif help_with == '10':
        loading("Exiting ", 5, "See you again❤️", 1)
        break

#======================================================================end===============================================================
