
from datetime import datetime, timedelta

def display_current_datetime():
    """
    Function to display the current date and time.
    """
    current_date = datetime.now()  # Get the current date and time
    print("Current date and time:", current_date.strftime("%Y-%m-%d %H:%M:%S"))

def calculate_future_date():
    """
    Function to calculate a future date based on user input.
    """
    try:
        # Prompt the user to enter the number of days
        days_to_add = int(input("Enter the number of days to add to the current date: ").strip())
        # Get the current date
        current_date = datetime.now()
        # Calculate the future date
        future_date = current_date + timedelta(days=days_to_add)
        print("Future date:", future_date.strftime("%Y-%m-%d"))
    except ValueError:
        print("Invalid input! Please enter a valid number.")

if __name__ == "__main__":
    # Part 1: Display the current date and time
    display_current_datetime()

    # Part 2: Calculate and display a future date
    calculate_future_date()

