# daily_reminder.py

# Prompt the user to input their task
task = input("Enter your task: ")

# Prompt the user to input the priority level of the task
priority = input("Priority (high/medium/low): ").lower()

# Prompt the user to specify if the task is time-bound
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Initialize the reminder message
reminder = ""

# Process the priority level using a match-case statement
match priority:
    case "high":
        reminder = f"'{task}' is a high priority task."
    case "medium":
        reminder = f"'{task}' is a medium priority task."
    case "low":
        reminder = f"'{task}' is a low priority task."
    case _:
        reminder = f"'{task}' has an unspecified priority. Please update the task priority."

# Modify the reminder based on time sensitivity using an if statement
if time_bound == "yes":
    reminder += " It requires immediate attention today!"
else:
    reminder += " Consider completing it when you have free time."

# Print the final reminder
print(f"\nReminder: {reminder}")
