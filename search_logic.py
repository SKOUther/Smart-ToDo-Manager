#===================================Libraries====================================
from logic import Task
from ui import custom_time, clear, Search_loading, RED, RESET
from datetime import datetime
#================================================================================

'''search in task list'''

def search_for_title(title_search):
    clear()
    found = 0
    show_message = True
    Search_loading()
    try:
        for i, search in enumerate(Task.to_do_list, start=1):
            if search["Task title"] == title_search:
                found += 1
                if show_message and found:
                    print("")
                    print(f"The following tasks were found as title: '{title_search}':\n\n")
                    custom_time(.5)
                    print("====Task Search====\n\n")
                    show_message = False

                print("Task number:", i)
                for key, value in search.items():
                    print(key, ":", value)
                print("-" * 30)
                print("")
    except:
        print("Something went wrong!")
        custom_time(1.5)
        return False

    if not found:
        return False
    else:
        return True

def search_for_time(time_search):
    clear()
    found = 0
    show_message= True

    real_time = datetime.now()
    time_of_year = real_time.strftime("%Y-%m-%d")

    earlier_time = None
    modern_time = None
    coming_time = None

    stop_print1 = False
    stop_print2 = False
    stop_print3 = False

    Search_loading()
    try:

        for i, search in enumerate(Task.to_do_list, start= 1):
            if search["Task time"] == "time is deleted":
                print(RED + "task time was deleted!")
                custom_time(1)
                print("Please adjust the task time." + RESET)
                custom_time(1.2)
                return False
            
            if search["Task time"][11:] == time_search:
                found += 1

                #=================================================================
                #Determine times
                #=================================================================

                #Past time
                #If there were different times in the 'past', but they all held the same clock time
                if search["Task time"][0:10] < time_of_year and stop_print1 and earlier_time:
                    if earlier_time == search["Task time"][0:10]:
                        stop_print1 = True
                    else:
                        earlier_time = search["Task time"][0:10]
                        stop_print1 = False

                if search["Task time"][0:10] < time_of_year and not earlier_time:
                    earlier_time = search["Task time"][0:10]
                #=================================================================
                
                #Present time
                if search["Task time"][0:10] == time_of_year:
                    modern_time = search["Task time"][0:10]
                #=================================================================

                #Future time
                #If there are different times in the 'future', but they all hold the same clock time
                if search["Task time"][0:10] > time_of_year and stop_print3 and coming_time:
                    if coming_time == search["Task time"][0:10]:
                        stop_print3 = True
                    else:
                        coming_time = search["Task time"][0:10]
                        stop_print3 = False

                if search["Task time"][0:10] > time_of_year and not coming_time:
                    coming_time = search["Task time"][0:10]
                #=================================================================

                if show_message and found:
                    print("")
                    print(f"The following tasks were found as time: '{time_search}':\n\n")
                    custom_time(.5)
                    print("====Task Search====\n\n")
                    show_message = False

                #Past
                if earlier_time:
                    if not stop_print1:
                        print(f"\n====Task\s on {earlier_time}====\n")
                        stop_print1 = True

                    if search["Task time"][0:10] == earlier_time and search["Task time"][11:] == time_search:
                        print("Task number:", i)
                        for key, value in search.items():
                            print(key, ":", value)
                        print("-" * 30)
                        print("")
                # - - -

                #Present
                if modern_time:
                    if not stop_print2:
                        print(f"\n====Task\s on today====\n")
                        stop_print2 = True

                    if search["Task time"][0:10] == modern_time and search["Task time"][11:] == time_search:
                        print("Task number:", i)
                        for key, value in search.items():
                            print(key, ":", value)
                        print("-" * 30)
                        print("")
                # - - -

                #Future
                if coming_time:
                    if not stop_print3:
                        print(f"\n====Coming Task\s====\n")
                        stop_print3 = True

                    if search["Task time"][0:10] == coming_time and search["Task time"][11:] == time_search:
                        print("Task number:", i)
                        for key, value in search.items():
                            print(key, ":", value)
                        print("-" * 30)
                        print("")
                # - - -
    
    except:
        print("Something went wrong!")
        custom_time(1.5)
        return False

    if not found:
        return False
    else:
        return True
            
def search_for_status(status_search):
    clear()
    found = 0
    show_message = True
    Search_loading()
    try:
        for i, search in enumerate(Task.to_do_list, start= 1):
            if search["Task status"] == status_search:
                found += 1
                if show_message and found:
                    print("")
                    print(f"The following tasks were found as status: '{status_search}':\n\n")
                    custom_time(.5)
                    print("====Task Search====\n\n")
                    show_message = False
                
                print("Task number:", i)
                for key, value in search.items():
                    print(key, ":", value)
                print("-" * 30)
                print("")
                
    except:
        print("Something went wrong!")
        custom_time(1.5)
        return False
    
    if not found:
        return False
    else:
        return True
    
def do_custom_search(title_search, time_search, status_search):
    clear()
    found = 0
    tasks_found = []
    one_task = f"We found a task that matches your search data.\n\n"
    more_tasks = f"We found several tasks that match your search criteria.\n\n"
    Search_loading()
    try:
        for i, search in enumerate(Task.to_do_list, start=1):
            if search["Task title"] == title_search and \
               search["Task time"][11:] == time_search and \
               search["Task status"] == status_search:
                found += 1
                tasks_found.append({
                    "Task number": i,
                    "Task title": search["Task title"],
                    "Task time": search["Task time"],
                    "Task status": search["Task status"]
                })

        if not found:
            return False
        
        print("\n" + (one_task if found == 1 else more_tasks))
        custom_time(.5)
        print("====Task Search====\n\n")

        for t in tasks_found:
            for k, v in t.items():
                print(f"{k:14} : {v}")
            print("-" * 30 + "\n")           
        return True 
                
    except:
        print("Something went wrong!")
        custom_time(1.5)
        return False  

#================================================================================