# Ask the user to input a task description and save it into a task variable
task = input("Enter your task: ")

# Prompt for the task’s priority (high, medium, low) and save it into a priority variable
priority = input("Priority (high/medium/low): ")

# In a time_bound variable, Ask if the task is time-bound (yes or no)
time_bound = input("Is it time-bound? (yes/no): ")

# Use a Match Case statement to react differently based on the task’s priority.
match priority:
    case 'high':
        if time_bound == 'yes':
            print(f"Reminder: '{task}' is a {priority} priority task that requires immediate attention today!")
        else:
            print(f"Reminder: '{task}' is a {priority} priority task that does not require immediate attention today!")

    case 'medium':
        if time_bound == 'yes':
            print(f"Reminder: '{task}' is a {priority} priority task that requires immediate attention today!")
        else:
            print(f"Reminder: '{task}' is a {priority} priority task that does not require immediate attention today!")

    case 'low':
        if time_bound == 'yes':
            print(f"Reminder: '{task}' is a {priority} priority task that requires immediate attention today!")
        else:
            print(f"Reminder: '{task}' is a {priority} priority task that does not require immediate attention today!")