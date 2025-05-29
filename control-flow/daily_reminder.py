task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").strip().lower()
time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

match priority:
    case "high":
        print(f"Reminder: '{task}' is high priority.") 
    case "medium":
        print(f"Reminder: '{task}' is medium priority.")
    case "low":
        print(f"Reminder: '{task}' is low priority.")
    case _:
        print("Invalid priority. Please choose high, medium, or low.")


if time_bound == "yes":
        print("This task requires immediate attention today!") 
else:
    print("Consider completing it when you have free time.")



