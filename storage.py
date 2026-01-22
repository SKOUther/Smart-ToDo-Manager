#===================================Libraries====================================
import json, os
from datetime import datetime
from ui import custom_time, clear
#================================================================================

file_path = "ToDoList.json"
file_path2 = "UserInfo.json"

#================================================================================
'''task file'''

#Save the task list as data in the file.
def save_data(tasks_list):
    with open (file_path, "w", encoding="utf-8") as f:
        json.dump(tasks_list, f, ensure_ascii=False, indent=4)

# - - -
#Use the file data if it contains data, or return an empty list.
#If it contains data, verify each type.
#Create a new list that retrieves the data from the file and modifies it.
#In the new list, add three main keys: Task Title, Task Time, and Task Status.
#If the data value is incorrect, enter the data name and the phrase "Is Deleted".
def use_data(tasks_list):
    #if the file is exists
    if os.path.exists(file_path):
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                loaded_data = json.load(f)

                tasks = []

                for user_task in loaded_data:
                    #Start each task with a blank value
                    title_value = None
                    time_value = None
                    status_value = None

                    values = list(user_task.values())

                    for v in values:
                        v = v.strip()

                        if "is deleted" in v: continue
                        
                        # -------------------------
                        # 1) Checking the task time
                        # -------------------------
                        if time_value is None:
                            try:
                                real_time = datetime.strptime(v, "%Y-%m-%d %H:%M")
                                time_value = real_time.strftime("%Y-%m-%d %H:%M")
                                continue
                            except:
                                pass  # If you cannot change the time in the task, return None

                        # -------------------------
                        # 2) Checking the task status
                        # -------------------------
                        if status_value is None:
                            if v in ['not yet', 'completed']:
                                status_value = v


                        # -------------------------
                        # 3) Checking the task title
                        # -------------------------
                        #If it does not contain a value
                        if title_value is None: 
                            #Allow the task title to include letters, spaces and digits only.
                            #The letters must be at least 3 letters long.
                            #The numbers also do not exceed 5 digits.
                            is_not_time = not ("-" in v and ":" in v)
                            if not is_not_time:
                                continue
                            title_condition1 = all(t.isalpha() or t.isspace() or t.isdigit() for t in v)
                            sum_of_letters = sum(letter.isalpha() for letter in v) 
                            sum_of_digits = sum(digit.isdigit() for digit in v)
                            title_condition2 = sum_of_letters >= 3 and sum_of_digits <= 5
                            if title_condition1 and title_condition2 and is_not_time \
                                and v not in ['not yet', 'completed']:
                                title_value = v
                
                    # -------------------------
                    # 4) Compensating for missing values
                    # -------------------------
                    if title_value is None:
                        title_value = "title is deleted"

                    if time_value is None:
                        time_value = "time is deleted"

                    if status_value is None:
                        status_value = "status is deleted"

                    # -------------------------
                    # 5) Building the new, error-free task
                    # -------------------------
                    tasks.append({
                        "Task title": title_value,
                        "Task time": time_value,
                        "Task status": status_value
                    })
                tasks_list.clear()
                tasks_list.extend(tasks)

        #If the file contains a programming error
        #Recreate it from scratch
        except json.JSONDecodeError:
            clear()
            print("Don't worry 😊, the file had a little error, but it's fixed and ready for you!")
            custom_time(3)
            with open(file_path, "w", encoding="utf-8") as f:
                f.write('[]')
            clear()

    #If you don't find a file with this title, create it.
    else:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write('[]')

    return tasks_list

#================================================================================
'''user file'''

#Save user data as file data
def save_user_info(user_data):
    with open (file_path2, "w", encoding="utf-8") as f :
        json.dump(user_data, f, ensure_ascii=False, indent=4)

# - - -
#Read the file, retrieve its data, and verify each type before returning it to the system.
#Create a new list containing a dictionary with key terms.
#Name, Age, Gender, Birth
#If it is correct, restore it as is; otherwise, state: the name of the information that "is deleted".
def use_user_data(user_data):
    if os.path.exists(file_path2):
        try:
            real_time = datetime.now().year
            with open (file_path2, "r", encoding="utf-8") as f:
                loaded_data = json.load(f)

                info = []

                for user_info in loaded_data:
                    name_value = None
                    age_value = None
                    gender_value = None
                    birth_value = None

                    values = list(user_info.values())

                    on_record = False
                    for v in values:
                        if v is None: break
                        #If data is found in the file, it is already registered and needs verification.
                        on_record = True 
                        v = str(v).strip()

                        if "is deleted" in v: continue

                        # 1) Verify the user's gender
                        if gender_value is None:
                            if v in ['private', 'male', 'female']:
                                gender_value = v

                        # 2) Verify the user's birth
                        if birth_value is None:
                            try:
                              
                                # 1. Read the date in year-month-day format, Without (hours:minutes)
                                birth_time = datetime.strptime(v, "%Y-%m-%d")
                                
                                # 2. Birth date storage in a standardized format (year-month-day)
                                birth_value = birth_time.strftime("%Y-%m-%d")
                                
                                # 3. Age is automatically calculated based on the current year if you are able to convert.
                                age_value = real_time - birth_time.year
                            except:
                                pass  
                                
                        # 3) Verify the user's age
                        if age_value is None:

                            # 1. Make sure that the total number of digits you stand on does not exceed 3 digits.
                            if v.isdigit() and len(v) < 4:
                                age = int(v)
                             
                                # 2. Make sure the age is between 7-100 years old
                                if 100 >= age >= 7:
                                    age_value = age

                        # 4) Verify username
                        if name_value is None:
                            #The username contains only spaces and letters; no numbers or symbols.
                            #The maximum number of characters is only 3.
                            name_condition1 = all(name.isalpha() or name.isspace() for name in v)
                            letters_sum = sum(letter.isalpha() for letter in v)
                            name_condition2 = letters_sum >= 3
                            if name_condition1 and name_condition2 and v not in ['private', 'male', 'female']:
                                name_value = v

                    if on_record:
                        # 4) Replace the empty values ​​with the ones you previously verified, and if it's empty, write "(info type)is deleted".
                        if name_value is None:
                            name_value = "name is deleted"

                        if age_value is None:
                            age_value = "age is deleted"
                            birth_value = "birth is deleted"

                        if gender_value is None:
                            gender_value = "gender is deleted"
                        
                        if birth_value is None:
                            birth_value = "birth is deleted"
                            age_value = "age is deleted"

                    info.append({
                        "name": name_value,
                        "age": age_value,
                        "gender": gender_value,
                        "birth": birth_value
                    })

                user_data.clear()
                user_data.extend(info)
                
        except json.JSONDecodeError:
            clear()
            print("Don't worry 😊, the file had a little error, but it's fixed and ready for you!")
            custom_time(3)
            with open(file_path, "w", encoding="utf-8") as f:
                f.write('[]')
            clear()
    else:
        with open (file_path2, "w", encoding="utf-8") as f:
            f.write("[]")
            return None

    return user_data

#================================================================================    