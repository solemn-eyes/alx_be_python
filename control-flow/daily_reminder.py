task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").strip().lower()
time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

match priority:
    case "high":
        message = f"Reminder: '{task}' is high priority."
    case "medium":
        message = f"Reminder: '{task}' is medium priority."
    case "low":
        message = f"Reminder: '{task}' is low priority."
    case _:
        message = "Invalid priority level. Please enter high, medium, or low."

if time_bound == "yes":
        message += "This task requires immediate attention today!"
else:
    message += "Consider completing it when you have free time."



print(message)

