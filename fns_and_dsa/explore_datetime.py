from datetime import datetime, timedelta
def display_current_datetime():
    current_date = datetime.now()
    print("Current Date and Time:", current_date.strftime("%Y-%m-%d %H:%M:%S"))
display_current_datetime()

def calculate_future_date():
    future_date = input("Enter the number of days to add to the current date: ")
    future_date = datetime.now() + timedelta(days=int(future_date))
    print("Future Date:", future_date.strftime("%Y-%m-%d %H:%M:%S"))
calculate_future_date()