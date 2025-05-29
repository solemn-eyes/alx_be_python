task_description = input("Enter your task: ")
task_priority = input("Priority (high/medium/low): ").strip().lower()
task_time = input("Is it time-bound? (yes/no): ").strip().lower()

match task_priority:
    case "high":
        print(task_description + " is a high priority task.")
        if task_time == "yes":
            print("You need to complete it today!")
        else:
            print("You should complete it this week.")
    
    case "medium":
        print(task_description + " is a medium priority task.")
        if task_time == "yes":
            print("You should complete it this week.")
        else:
            print("You can complete it this month.")
    case "low":
        print(task_description + " is a low priority task.")
        if task_time == "yes":
            print("You can complete it this month.")
        else:
            print("You can complete it when you have time.")
    case _:
        print("Invalid priority level. Please enter high, medium, or low.")


