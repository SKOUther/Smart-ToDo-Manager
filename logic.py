#===================================Libraries====================================
from storage import save_data, use_data, save_user_info, use_user_data
from datetime import datetime, timedelta
from string import digits, ascii_lowercase
from confirmation import confirm_task
from ui import clear, custom_time, loading, RED, GREEN, BLUE, YELLOW, CYAN, RESET
#================================================================================

'''Class for task data & user data'''

class Task:

    #a list with dict insid(has all user tasks)
    to_do_list = []

    def __init__(self, task_title, task_time, task_status):
        self.task_title = task_title
        self.task_time = task_time
        self.task_status = task_status

    #Take the correct user input data and store each value in front of the appropriate key. and append to the to_do_list
    def add_task(self, title, time, status):
        adding_task = {
            "Task title": title,
            "Task time": time,
            "Task status": status
        }
        
        save_task = confirm_task(adding_task)
        if save_task:
            loading("Adding your task ", 4, "Your task has been added.", 1.2)
            return Task.to_do_list.append(adding_task)
        else:
            return save_task

    #first: print all tasks in the list, start with its number.
    #then: ask him to choose a num between 1 to the limit num task in a task list.
    #next: if it's return False contin, or if he type e to exit so do.
    #after that: if none of these, take his valid num he entered, and ask him again to edit his task.
    #later: enter to the list at the num he chosen_number - 1 to take his task index in the list. and replace edit task on that index.
    #finally: open the data file and update the task the user has edited.
    def update_task(self, wrong_time):
        index_num = None
        while True:
            #If his list is empty of tasks
            if not has_task():
                return False
            use_last_time = True #If it already contains data, you can go over the last task entered for some verification purposes.
            mark = True #Discrimination is always enabled to change the task status except in some exceptions.

            task_len = len(Task.to_do_list)
            self.show_tasks(True)
            num = is_valid_index(text="edit", limit=task_len, with_s=False, mark=False) #It returns only one value so that only one task is modified.
            if not num:
                continue
            elif num == 'e':
                break
            else:
                if not index_num:  
                    index_num = num[0] - 1
                if wrong_time: #If it contains values ​​other than zero, this means there is an error in its file.
                    use_last_time=False
                    mark = False

                user_task_title = is_valid_title("another", similar=True)
                user_task_time = is_valid_time(use_last_time, similar=True)
                user_task_status = is_valid_status(mark)
                task_dict = {
                    "Task title": user_task_title,
                    "Task time": user_task_time,
                    "Task status": user_task_status
                }

                if index_num >= 0:
                    Task.to_do_list[index_num] = task_dict
                    loading("Editing task ", 4, "", .5)
                    self.save_tasks()
                
                else:
                    print(f"An error occurred while deleting task number {index_num+1}. Please try again.")
                    custom_time(3)
                    return
    
    #Delete the tasks for which the user entered numbers, whether it's one number or more.
    #But check that the numbers are within the limits and are in the task list index.
    #Then delete that number's index from the task list.
    def delete_task(self):
        while True:
            if not has_task():
                return False
            
            task_len = len(Task.to_do_list)
            self.show_tasks(True)
            num = is_valid_index(text="delete", limit=task_len, with_s=True, mark=False)
            if not num:
                continue
            elif num == 'e':
                break
            else:
                for n in sorted(num, reverse=True):
                    index_num = n - 1
                    Task.to_do_list.pop(index_num)

                loading("Deleting your task on way ", 5, "Your task number\s has deleted.", 2)
                self.save_tasks()
    
    #Distinguish the task or tasks by one status: completed or not yet.
    #If he selects more than one task and it happens that a task's status is already as he wants it to change.
    #Then complete the loop, but pause briefly and tell him.
    def mark_tasks(self):
        set_status = False
        while not set_status:
            if not has_task():
                return False
            task_len = len(Task.to_do_list)
            set_status = is_valid_status(mark=True)
            
        num = None
        while True:
            self.show_tasks(True)
            num = is_valid_index(text="mark as "+set_status, limit=task_len, with_s=True, mark=True)
            if not num:
                continue
            if num == 'e':
                break
            else:
                for n in sorted(num, reverse=True):
                    index_num = n - 1
                    task_to_mark = Task.to_do_list[index_num]

                    if task_to_mark["Task status"] == "status is deleted":
                        print(f"Sorry, task number {n} is not a vaild status.\nPlease edit\delete the task.")
                        custom_time(3.3)
                        return

                    if task_to_mark["Task status"] not in ['not yet', 'completed']:
                        print("Please check the status of your tasks from your list first.\nA task cannot have a status other than 'completed' or 'not yet'.")
                        custom_time(4.2)
                        return

                    if task_to_mark["Task status"] == set_status:
                        clear()
                        print(f"task number {n} is actually '{set_status}'.")
                        custom_time(2.2)

                        if num:
                            clear()
                            print(GREEN + "We'll continue for your" + RESET)
                            custom_time(1.2)
                            clear()
                            continue

                    else:   
                        clear()
                        task_to_mark["Task status"] = set_status

            
                loading(f"Marking task as {set_status} on way ", 3, f"Your task/s marked as {set_status}", 2)
                self.save_tasks()

    #print to_do_list on the user screen
    #if the list has no task return False, else True
    def show_tasks(self, task_num):
        if not has_task():
            return False 
        print("\n          -----TASKS LIST-----\n")
        for t, tasks in enumerate(Task.to_do_list, start=1):
            print("")
            if task_num:
                print(BLUE + "Task number:" + RESET + CYAN + f"{t}" + RESET)
            for key, value in tasks.items():
                print(YELLOW + f"{key:14}" + RESET + GREEN + f": {value}" + RESET)
            print("")
            print("-"*40)
        return True

    #save to-do-list to file
    def save_tasks(self):
        save_data(Task.to_do_list)

    #open save file and read all task, and return it back to to-do-list
    #if it value is None, return None to to-do-list
    def read_tasks_file(self):
        Task.to_do_list = use_data(Task.to_do_list)
        self.save_tasks()


class User:

    data_now = datetime.now()
    user_data = []

    def __init__(self, name, age, gender, date_birth):
        self.name = name
        self.age = age 
        self.gender = gender
        self.date_birth = date_birth

    #print user info
    def show_user_info(self):
        user_stage = None
        if self.gender == "private":
            say_gender = "private"
        else:
            if user_stage is None:
                user_stage = self.age_stage()
                if user_stage is None:
                    say_gender = "we can't read your age!"

                if user_stage == "Adult":
                    if self.gender == "male":
                        say_gender = "man"
                    else:
                        say_gender = "woman"

                elif user_stage == "Teen":
                    if self.gender == "male":
                        say_gender = "boy"
                    else:
                        say_gender = "girl"
                        
                else:
                    if self.gender == "male":
                        say_gender = "little boy"
                    else:
                        say_gender = "little girl"

        print("\n\n-----Your info-----")
        print(BLUE + f"Your name:" + RESET + GREEN + f" {self.name}." + RESET)
        print(BLUE + f"You are:" + RESET + RED + f" {self.age} years old." + RESET)
        print(BLUE + f"You are:" + RESET + RED + f" a {say_gender}." + RESET)
        print(BLUE + f"You were born at:" + RESET + GREEN + f" {self.date_birth}" + RESET)
        print("-"*25)
        print(YELLOW + f"\n\nNice to know you {self.name}❤️" + RESET)

    #ask him for his info, and save it at user_data list
    #Take his age and convert his birth date to the current year.
    def take_user_info(self):
        user_name = get_name()
        if user_name:
            while True:
                user_age = get_age()

                #If he is under 7 years old, do not let him use it again.
                if user_age < 7:
                    user_year = User.data_now.year - user_age
                    birth = datetime(
                        year= user_year,
                        month= 1,
                        day= 1
                        )
                    user_birth = birth.strftime("%Y-%m-%d")
                    return User(name=user_name, age=user_age, gender="private", date_birth=user_birth)
                #==================================================================================
                
                else:
                    user_year = get_birth(user_age)
                    if not user_year:
                        continue
                    else:
                        y, m, d = user_year
                        birth = datetime(
                            year= y,
                            month= m,
                            day= d
                        )
                        user_birth = birth.strftime("%Y-%m-%d")
                        break 
            user_gender = get_gender()
        else:
            return False

        return User(name=user_name, age=user_age, gender=user_gender, date_birth=user_birth)
    
    #itype: Data type (nameو ageو gender)
    #inew: New value
    def changing(self, itype, inew):
        if itype == "name":
            stype = self.name
        elif itype == "age":
            stype = self.age
        elif itype == "gender":
            stype = self.gender
        else:
            stype = self.date_birth

        data = User.user_data[0]
        stype = inew
        data[itype] = stype
        return stype

    #Change the data type value based on user input.
    def change_user_info(self, info_type):
        while True:
            if info_type == "new_name":
                new_name = get_name()
                if new_name == self.name:
                    print(f"Sorry, you cannot change your name to {self.name}, because it already is.")
                    custom_time(2.3)
                    break
                new_info = self.changing("name", new_name)
                self.name = new_info
                self.save_user()
                clear()
                break

            elif info_type == "new_age":
                while True:
                    new_age = get_age()
                    if new_age == self.age:
                        print(f"Sorry, you cannot change your age to {self.age}, because it already is.")
                        custom_time(2.3)
                        break
                    if new_age < 7:
                        exit()
                    else:
                        new_year = get_birth(new_age)
                        if not new_year:
                            continue
                        else:
                            y, m, d = new_year
                            user_birth = datetime(
                                year= y,
                                month= m,
                                day= d
                            )
                            new_birth = user_birth.strftime("%Y-%m-%d")
                            new_age_info = self.changing("age", new_age)
                            new_birth_info = self.changing("birth", new_birth)

                            self.age = new_age_info
                            self.date_birth = new_birth_info
                            self.save_user()
                            clear()
                            break 
                break

            elif info_type == "new_gender":
                new_gender = get_gender()
                new_info = self.changing("gender", new_gender)
                self.gender = new_info
                self.save_user()
                clear()
                break

            else:
                print("Sorry, something went wrong. or we can't find what you looking for!\nPleace try again.")
                custom_time(2.5)
                break
                
    #print welcome messagee and added his name
    def say_welcome(self):
        if self.name == "name is deleted":
            name = '\n*invalid name!\n\n'
        else:
            name =  f"\nWelcome {self.name}, Nice to see you here.\n\n"
        print(name)
    
    #from his name know his age stage and return it
    def age_stage(self):
        if not self.age:
            print("error in your age!")
            custom_time(1.5)
            clear()
            return None
        user_age_stage = "Adult" if self.age >= 18 else ("Teen" if 17 >= self.age >= 12 else "Child")
        return user_age_stage

    #return his birth from his age
    def calculate_birth(age):
        user_year = User.data_now.year - age
        return user_year

    #take his info and save it in a file to use it later
    def save_user(self):
        User.user_data = []
        User.user_data.append({
            "name": self.name,
            "age": self.age,
            "gender": self.gender,
            "birth": self.date_birth
        })
        save_user_info(User.user_data)

    #if user has an info in his file, use it, or return it, else return none
    def read_user_file(self):
        User.user_data = use_user_data(User.user_data)

        if not User.user_data:
            return None

        data = User.user_data[0]

        self.name = data.get("name")
        self.age = data.get("age")
        self.gender = data.get("gender")
        self.date_birth = data.get("birth")
        self.save_user()

        return self

#================================================================================


'''valid input user on task options'''
#make sure that his number is between 1 to limit only, if it's, return his number, else False.
def is_valid_num(limit, ask_type):
    try:
        if ask_type == "help":
            type1 = f"Enter the number you need {ask_type} with"
            enter = type1
        elif ask_type == "change":
            type2 = f"Enter the number you want to {ask_type}"
            enter = type2
        elif ask_type == "search":
            type3 = f"Enter the number of what you want to {ask_type} for"
            enter = type3

        num = input(f"{enter} 1-{limit}: ")
        custom_time(.3)
        clear()
        if not num.isdigit():
            print(f"Enter only a number 1-{limit}.")
            custom_time(1.2)
            clear()
            return False
        if int(num) > limit or int(num) < 1:
            print(f"Enter only a number 1-{limit}.\n*(Not a number less than 1 or a number greater than {limit})*")
            custom_time(2)
            clear()
            return False
        else:
            clear()
            custom_time(.3)
            return num
    except:
        print("Sorry, something went wrong, try again.")
        custom_time(1.3)
        clear()
        return False

# - - - 
'''valid input user on info options'''
#take his num if user want to edit, or take his num\s if user want to delete or mark
def is_valid_index(text, limit, with_s, mark):
    try:
        #if user want delete or mark. If he wants to specify more than one task.
        if with_s or mark:
            s = '\s'
            comma_text = "\nIf you want more than one number, separate them with a comma."
        #or want edit. He can modify his task each time.
        else:
            s = ''
            comma_text = '\n'

        print(comma_text)
        num = input(f"Type task number{s} to '{text}' 1-{limit} (or type 'e' to exit): ")
        if num.lower() == 'e':
            return 'e'
        
        parts = [p.strip() for p in num.split(',')]

        #user can type more than one number, On condition separated by a comma, Otherwise return False
        if with_s or mark:
            #if in the parts list you found '' that mean he enter a double comma, so return False
            if any(p == '' for p in parts):
                print("You cannot enter a double comma.")
                custom_time(1.2)
                clear()
                return False

            #if his entered not in all comma and number\s, return False
            if not all(p.isdigit() for p in parts if p != ''):
                print("Please enter a correct number separated by a comma.")
                custom_time(1.8)
                clear()
                return False
            
        #user can type one number only, Otherwise return False
        else:
            #donn't accept a double comma in a parts list. let him enter again.
            if any(p == '' for p in parts):
                print("You cannot enter a double comma.")
                custom_time(1.2)
                clear()
                return False
            
            #if he entered more than one number. donn't let him.
            if len(parts) > 1:
                print("You can edit one task at a time, so please enter only one number.") 
                custom_time(2.3)
                clear()
                return False  
            
            #if he enterd any thing not number
            for num in parts:
                if not num.isdigit():
                    print("Enter only a correct number.")
                    custom_time(1.2)
                    clear()
                    return False 
            
        parts = [int(p) for p in parts] #make all parts list as an int not str.

        #make sure that his num\s he entered between the limit.
        for num in parts:
            if num > limit or num <= 0:
                print(f"Can't Enter a number graeter than '{limit}' or less than 1.")
                custom_time(2)
                clear()
                return False
        
        #if everything is valid return his num\s
        else:
            custom_time(.3)
            clear()
            return parts
    except:
        print("Sorry, something went wrong, try again.")
        custom_time(1.7)
        clear()
        return False


#================================================================================

'''Take task data'''

#Take a correct address value and return it; if it's incorrect, return "False".
def is_valid_title(text, similar):
    while True:
        try:
            clear()
            title = input(f"Enter your {text} task title:\n").lower()
            custom_time(.3)
            clear()
            if not all(t in ascii_lowercase + digits + ' ' for t in title):
                print("Enter only a text or a numbers.")
                custom_time(1.2)
                continue
            
            #Count both the numbers and letters in the task title.
            count_digit = sum(d.isdigit() for d in title)
            count_string = sum(s.isalpha() for s in title)

            if count_string < 3:
                print("Your task length to short. make sure to type 3 letters at least.")
                custom_time(2)
                continue
            if count_digit > 5:
                print("Your task is to have a number that cannot exceed 5 digits.")
                custom_time(2)
                continue
        
            else:
                found = 0
                for task_title in Task.to_do_list:
                    if found ==1:
                        break
                    #If the title he chose is similar to the title of another task
                    if similar:
                        if task_title["Task title"] == title:
                            found +=1
                            while True:
                                clear()
                                #Inform him of the matter and let him make his decision.
                                print("Dear user, the title you entered exactly matches the title of another task.")
                                edit_title = input("Do you want to continue or re-enter the title again?\ntype(continue/again): ")
                                custom_time(.3)
                                clear()
                                if edit_title.lower() in ['a', 'again']:
                                    break
                                elif edit_title.lower() in ['c', 'continue', 'contin']:
                                    found = 0
                                    print("Title added.")
                                    custom_time(1)
                                    clear()
                                    break
                                else:
                                    print(f"'{edit_title}' is invalid input!\ntype(continue/again)")
                                    custom_time(2)
                                    continue
                if found:
                    continue
                clear()
                custom_time(.3)
                return title
        except:
            print("Sorry, something went wrong, try again.")
            custom_time(1.5)
            continue

#Take the correct time value and return it; if it's incorrect, return an "False".
def is_valid_time(use_last_time, similar):
    while True:
        real_time = datetime.now()
        try:
            clear()
            print("You can press 'a' to set the time automatically.\nBut remember that it will add 30 minutes to the current time or the time of the last task.")
            custom_time(3.2)
            clear()
            time = input("Enter your task time (time you'll be done at, or press 'a' to set automatically):\n")
            custom_time(.3)
            clear()
            #=============================automatic set==================================
            if time.lower() == 'a':
                #If its list is empty, set the time automatically 30 minutes after its actual time.
                if not Task.to_do_list:
                    task_on_time = real_time + timedelta(minutes=30)

                #If he selected an automatic time and his list already contains tasks,
                #Take the time of the last task and add 30 minutes to it.
                if use_last_time and Task.to_do_list:
                    last_time = Task.to_do_list[-1]

                    #Make sure to check for errors if the time is omitted. for last task time.
                    if last_time["Task time"] == "time is deleted":
                        print(RED + "Sorry, your last task has no time limit. Please edit or delete it." + RESET)
                        custom_time(2.5)
                        clear()
                        return "wrong"
                    
                    take_time = last_time["Task time"]
                    
                    #Extract the time of the last task to increase the minutes by 30 minutes.
                    y = int(take_time[0:4])
                    m = int(take_time[5:7])
                    d = int(take_time[8:10])

                    h = int(take_time[11:13])
                    min = int(take_time[14:16])
                    s = 0

                    add_on_last_time = datetime(
                        year=y,
                        month=m,
                        day=d,

                        hour=h,
                        minute=min,
                        second=s
                    )

                    task_on_time = add_on_last_time + timedelta(minutes=30)

                #if the time become in the past add one day
                if task_on_time < real_time:
                    task_on_time += timedelta(days=1)

                clear()
                custom_time(.3)
                return task_on_time.strftime("%Y-%m-%d %H:%M")
            #=====================================================================

            if not all(t in digits + ":" for t in time):
                print("You can enter only *(hour:minutes)*.")
                custom_time(1.5)
                continue
            
            sum_of_digits = sum(d in digits for d in time)
            separate = time.count(":")

            if not sum_of_digits == 4:
                print("""Please ensure you enter two digits for the hour, and two digits for the minutes.
                *(If it's a single digit, precede it with a zero)*""")
                custom_time(3)
                continue

            if separate == 0 or separate > 1:
                print("Please separate the hours from the minutes using one ':'.")
                custom_time(2)
                continue

            else:
                #Determining the exact positions of both minutes and seconds.
                h = int(time[0:2])
                m = int(time[3:5])

                #Take real-time measurements with only minutes and seconds adjusted.
                task_on_time = datetime(
                year = real_time.year,
                month = real_time.month,
                day = real_time.day,
                hour = h,
                minute = m,
                second = 0
                )
                
                if similar:
                    if Task.to_do_list:
                        found = 0
                        #If you find a task that takes the same amount of time as the one you entered,
                        #tell him so and let him decide.
                        for task in Task.to_do_list:
                            if found == 1:
                                break
                            if task["Task time"] == task_on_time.strftime("%Y-%m-%d %H:%M"):
                                found +=1
                                while True:
                                    clear()
                                    print("Dear user, the time you entered exactly matches the time of another task.")
                                    edit_time = input("Do you want to continue or re-enter the time again?\ntype(continue/again): ")
                                    custom_time(.3)
                                    clear()
                                    if edit_time.lower() in ['a', 'again']:
                                        break
                                    elif edit_time.lower() in ['c', 'continue', 'contin']:
                                        found = 0
                                        print("Time added.")
                                        custom_time(1)
                                        clear()
                                        break
                                    else:
                                        print(f"'{edit_time}' is invalid input!\ntype(continue/again)")
                                        custom_time(2)
                                        continue
                        if found:
                            continue 
                    
                #if the time become in the past add one day
                if task_on_time < real_time:
                    task_on_time += timedelta(days=1)
                    clear()
                    custom_time(.3)
                
            return task_on_time.strftime("%Y-%m-%d %H:%M")

        except Exception as p:
            print("Sorry, something went wrong, try again.", p)
            custom_time(10)
            continue

#Take a correct status value and return it; if it's incorrect, return an "False".
def is_valid_status(mark):
    while True:
        try:
            #If he wants to mark his task/s, tell him if the mark is complete or not yet.
            if mark:
                m = "Did you finished this task\s? (type 'y' as completed, or 'n' as not yet):\n"
            else:
                m = "Enter your task status (whether it is completed or not, or type 'a' to set automatic):\n"

            clear()
            status = input(m).lower()
            custom_time(.3)
            clear()
            if not status.isalpha():
                print("Please enter yes or no if the task has been completed, or not.")
                custom_time(1.5)
                continue

            if status == 'a':
                clear()
                custom_time(.3)
                return "not yet"

            if status in ['yes', 'y', "completed", 'comp']:
                clear()
                custom_time(.3)
                return "completed"
            
            elif status in ['no', 'n', "not yet", 'not']:
                clear()
                custom_time(.3)
                return "not yet"
            
            else:
                print("Enter only 'yes' or 'no' if the task has been completed, or not.")
                custom_time(2.2)
                continue
        except:
            print("Sorry, something went wrong, try again.")
            custom_time(1.5)
            continue


#================================================================================

'''Check availability'''

#Check if it is registered or not, if not return False.
def is_user_available(user_info):
    if user_info.name is None:
        print(RED + "You have not yet entered your data." + RESET)
        custom_time(2)
        return False
    return True

#Check if his list actually contains tasks, if not return False.
def has_task():
    if not Task.to_do_list:
        print("\n          -----TASKS LIST-----\n")
        print(RED + "Your to-do-list is empty.\nAdd a task first." + RESET)
        custom_time(3)
        return False
    return True


#================================================================================

'''Take user info'''

# - - - 
def get_name():
    while True:
        try:
            clear()
            name = input("Enter your beautiful name: ").lower()
            custom_time(.3)
            clear()
            
            if not all(char.isalpha() or char.isspace() for char in name):
                print("Your name must contain only letters and spaces.")
                custom_time(2)
                continue

            strip_name = [letters.strip() for letters in name]

            if len(strip_name) < 3:
                print("The name cannot contain fewer than 3 letters.")
                custom_time(2)
                continue

            if len(strip_name) > 25:
                print("Your name is too long and exceeds the limit of 25 characters.")
                custom_time(2.8)
                continue

            else:
                custom_time(.3)
                clear()
                return name
        except:
            print("sorry, something went wrong! try again.".capitalize())
            custom_time(1.3)
            continue

# - - - 
def get_age():
    while True:
        try:
            clear()
            age = input("Enter your real age: ")

            if not age.isdigit():
                print("Age must consist of whole numbers.")
                custom_time(1.5)
                continue

            age = int(age)

            if age <=0:
                print("Age cannot be zero or less.")
                custom_time(1.2)
                continue

            if age < 7:
                print("Sorry, the age limit for using this program is 7 years and above.")
                custom_time(1.9)
                return age
            
            if age > 100:
                print("An age over 100 is unrealistic. Please enter a valid age..")
                custom_time(1.9)
                continue

            else:
                custom_time(.3)
                clear()
                return age

        except:
            print("Sorry, someting went wrong! try again.")
            custom_time(1.5)
            continue

# - - - 
def get_gender():
    while True:
        try:
            clear()
            gender = input("What's your gender? (male, female, prefer not to say):\n").lower()
            custom_time(.3)
            clear()
            if not gender.isalpha():
                print("Please enter a text, from the options available to you.")
                custom_time(2)
                continue

            gender = gender.strip()

            if gender in ['not', 'n', 'no', 'private', 'p']:
                print("You will be assigned to us as a male as a general term;\nyou can change this later.")
                custom_time(2.3)
                clear()
                return 'private'

            if gender in ['man', 'boy', 'm', 'b', 'male']:
                custom_time(.3)
                clear()
                return 'male'

            elif gender in ['woman', 'girl', 'w', 'g', 'f', 'female']:
                custom_time(.3)
                clear()
                return 'female'
            
            else:
                print("Sorry, we couldn't recognize what you entered.\nPlease enter text from the options available to you")
                custom_time(2.9)
                continue
            
        except:
            print("Sorry, something went wrong! Please try again")
            custom_time()
            continue

# - - - 
def get_birth(age):
    while True:
        try:
            user_year = User.calculate_birth(age)
            year = input(f"Were you born at {user_year}? y/n: ").lower()
            
            if year in ['yes', 'y']:
                while True:
                    try:
                        clear()
                        user_month_day = input("Enter your m/d: ").strip().replace(" ", "")
                        custom_time(.3)
                        clear()

                        if user_month_day.count('/') != 1:
                            print("Use only one '/' between month and day.")
                            custom_time(1.5)
                            continue

                        if not all(birth.isdigit() or birth == '/' for birth in user_month_day):
                            print("Make sure to enter your month separated by '/' then your day.")
                            custom_time(1.8)
                            continue

                        month, day = user_month_day.split('/')

                        if not month.isdigit() or not day.isdigit():
                            print("Month and day must be numbers.")
                            custom_time(1.5)
                            continue

                        if not len(month) == 2 or not len(day) == 2:
                            print("The month & day consists of two digits, and if it's a single digit, precede it with a zero.")
                            custom_time(2.4)
                            continue

                        month = int(month)
                        day = int(day)

                        if not (1 <= month <= 12):
                            print("Month must be between 1 and 12.")
                            custom_time(1.5)
                            continue

                        if not (1 <= day <= 31):
                            print("Day must be between 1 and 31.")
                            custom_time(1.5)
                            continue

                        else:
                            print("You birth day is:")
                            print(f"--> {user_year}/{month}/{day}")
                            rihgt_birth = input("Is't rihgt? y/n: ").lower()
                            if rihgt_birth in ['yes', 'y']:
                                return user_year, month, day
                            elif rihgt_birth in ['no', 'n']:
                                return False
                            else:
                                print("Invalid input")
                                custom_time(1.2)
                                continue
                    except:
                        print("Sorry, somthing went wrong! try again.")
                        custom_time(1.5)
                        continue
            
            elif year in ['no', 'n']:
                return False
        except:
            print("Sorry, somthing went wrong! try again.")
            custom_time(1.5)
            continue


'''Ask for take his data'''

def ask_for_data(user_info):
    while user_info.name is None:
        clear()
        print("Do you want add your info in this program? (you can skip this for leter)")
        add_info = input("Type your answer y/n: ").lower()

        if add_info in ['y', 'yes', 'yea', 'yah']:
            user_info = user_info.take_user_info()
            if user_info.age < 7:
                user_info.save_user()
                exit()
            loading("Adding your info ", 3, '', 0)
            user_info.save_user()

        elif add_info in ['n', 'no', 'skip']:
            clear()
            print("You can added your info later")
            custom_time(1.5)
            break
        else:
            print("We did't get what you typed. you can add your info anytime.")
            custom_time(2.8)
            break
    return user_info

#================================================================================

