class Task:
    def __init__(self, task_id, title, description, priority, status):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.priority = priority
        self.status = status

    def __str__(self):
        return f"ID: {self.task_id}, Title: {self.title}, Description: {self.description}, Priority: {self.priority}, Status: {self.status}"
    

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
    
    def view_all_tasks(self):
        if len(self.tasks) == 0:
            print("No Task Added!")
            return
        else:
            for task in self.tasks:
                print(task)
        print("\n")

    def delete_task(self, id):
        if len(self.tasks) == 0:
            print("No Task left to delete!\n")
        else:
            for task in self.tasks:
                if id == task.task_id:
                    self.tasks.remove(task)
                    print("Task Removed!")
                    return
        print("Invalid Task ID!\n")

    # Get task By priority
    def get_task_by_priority(self, priority):
        for task in self.tasks:
            if task.priority == priority:
                print(task)
        return None
    
    # Editing Task
    def edit_task(self, task_id, title, description, priority, status):
        for task in self.tasks:
            if task_id == task.task_id:
                if title == "":
                    pass
                else:
                    task.title = title
                if description == "":
                    pass
                else:
                    task.description = description
                
                if priority == "":
                    pass
                else:
                    task.priority = priority
                if status == "":
                    pass
                else:
                    task.status = status


# choices 
def Choice_menu():
    print("1. Add Task")
    print("2. Edit Task")
    print("3. Delete Task")
    print("4. View All Tasks")
    print("5. Filter Tasks by Priority")
    print("6. Exit")
    print("\n")

def main():
    task_mngr = TaskManager()
    task_id = 0
    while True:
        
        try:

            Choice_menu()
            choice = int(input("Enter your choice. (1-6): "))
        
            if choice == 6:
                break

            elif choice == 1:
                task_id += 1
                task_title = input("Enter the task title: ")
                task_desc = input("Enter task description: ")

                # checking for mismatch in task prior
                while True:
                    task_prior = input("Enter task priority (High/Medium/Low): ")
                    task_prior = task_prior.lower()
                    if task_prior in ["high","medium","low"]:
                        task_prior = task_prior.capitalize()
                        break
                    else:
                        print("Invalid Task Priority!")
                        

                # checking for mismatch in task status
                while True:
                    task_stat = input("Enter the status (Pending/In Progress/Completed): ")
                    task_stat = task_stat.lower()
                    if task_stat in ["pending","in progress","completed"]:
                        task_stat = task_stat.capitalize()
                        break
                    else:
                        print("Invalid Task Status!")
                        
                # adding the tasks
                task = Task(task_id,task_title,task_desc,task_prior,task_stat)
                task_mngr.add_task(task)


            # View All tasks
            elif choice == 4:
                task_mngr.view_all_tasks()

            # task deletion
            elif choice == 3:
                # Delete by task id
                id = int(input("Enter The Task ID to Delete: "))
                task_mngr.delete_task(id)

            # filter by priority
            elif choice == 5:
                priority = input("Enter priority to filter task (High/Medium/Low): ")
                priority = priority.lower()
                if priority in ["high","low","medium"]:
                    priority = priority.capitalize()
                    task_mngr.get_task_by_priority(priority)
                else:
                    print("Invalid Priority!\n")

            # edit task
            elif choice == 2:
                if len(task_mngr.tasks) == 0:
                    print("No tasks Left to edit!\n")
                else:
                    id = int(input("Enter the task ID to edit: "))
                    new_title = input("Enter new title (leave blank to keep existing): ")
                    new_desc = input("Enter new description (leave blank to keep existing): ")

                    # check for mismatch in new priority update
                    while True:
                        new_prior = input("Enter new priority (leave blank to keep existing): ")
                        new_prior = new_prior.lower()
                        if new_prior in ["high","low","medium"]:
                            new_prior = new_prior.capitalize()
                            break
                        else:
                            print("Invalid new Task Priority!")

                    # check for mismatch in new status update
                    while True:
                        new_stat = input("Enter new status (leave blank to keep existing): ")
                        if new_stat in ["pending","in progress","completed"]:
                            new_stat = new_stat.capitalize()
                            break
                        else:
                            print("Invalid new Task Status!")

                    task_mngr.edit_task(id,new_title,new_desc,new_prior,new_stat)
                    
        except:
            print("Invalid Input!")



main()