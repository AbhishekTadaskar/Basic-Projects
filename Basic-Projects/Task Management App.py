# TASK MANAGEMENT APP #

def task():
    tasks = [] 
    print("--- WELCOME TO TASK MANAGEMENT APP ---")

    total_task = int(input("Enter how many task you to add = "))
    for i in range(1,total_task+1):
        task_name = input(f"Enter task {i} = ")
        tasks.append(task_name)

    print(f"Today's tasks are\n{tasks}")

    while True:
        try:
            operation = int(input("Enter 1-Add\n2-Update\n3-Delete\n4-View\n5-Exit/Stop/"))
        except ValueError:
            print("please enter a valid number")
            continue
        
        if operation == 1:
            add = input("Enter task you want to add = ").lower()
            tasks.append(add)
            print(f"Task {add} has been successfully added...")

        elif operation == 2:
            updated_val = input("Enter the task name you want to update = ").lower()
            if updated_val in tasks:
                up = input("Enter new task = ").lower()
                ind =tasks.index(updated_val)
                tasks[ind] = up
                print(f"Updated task {up}")
            else:
                print("Task not found")

        elif operation == 3:
            del_val = input("Enter task which you want to delete = ").lower()
            if del_val in tasks:
                ind = tasks.index(del_val)
                del tasks[ind]
                print(f"Task {del_val} has been deleted...")
            else:
                print("Task not found")

        elif operation == 4:
            print(f"Total Tasks ={tasks}")

        elif operation == 5:
            print("Closing the Program")
            break
        else:
            print("Invalid Input")

task()


