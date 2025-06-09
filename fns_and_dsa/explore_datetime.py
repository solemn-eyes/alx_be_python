import datetime
def display_current_datetime():
    current_date = datetime.datetime.now()
    print("Current Date and Time:", current_date.strftime("%Y-%m-%d %H:%M:%S"))

display_current_datetime()
def calculate_future_date():
    future_date = input("Enter a number of days to add to the current date: ")
    future_date = datetime.datetime.now() + datetime.timedelta(days=int(future_date))
    print("Future Date:", future_date.strftime("%Y-%m-%d %H:%M:%S"))
calculate_future_date()