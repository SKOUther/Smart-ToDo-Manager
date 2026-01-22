#===================================Libraries====================================
from logic import Task, User
#================================================================================

'''Read the value of each file.'''

#Read the value from the task file and check if it contains the correct values.
def read_task_file_if_true():
    wrong_task = []

    for index, task in enumerate(Task.to_do_list):

        wrong_in_title = (task["Task title"] == "title is deleted")
        wrong_in_time = (task["Task time"] == "time is deleted")
        wrong_in_status = (task["Task status"] == "status is deleted")

        #If any one of them is wrong → add the task number
        if wrong_in_title or wrong_in_time or wrong_in_status:
            wrong_task.append(index)

        wrong_in_title = None
        wrong_in_time = None
        wrong_in_status = None

    return wrong_task

# - - -
#Read the value from the user file and check if it contains a valid value.
def read_user_file_if_true():
    #We used a set (group) to prevent word duplication if the error occurred with more than one user.
    wrong_fields = set() 

    for info in User.user_data:
    
        if info.get("name") == "name is deleted":
            wrong_fields.add("name")
        
        if info.get("age") == "age is deleted":
            wrong_fields.add("age")
            
        if info.get("gender") == "gender is deleted":
            wrong_fields.add("gender")
            
        if info.get("birth") == "birth is deleted":
            wrong_fields.add("birth")     

    #Convert it to a list upon return.
    return list(wrong_fields)

#================================================================================