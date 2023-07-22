def calculate_due_date(ovulation_date):
    # Add 280 days to the ovulation date to get the estimated due date
    estimated_due_date = ovulation_date + datetime.timedelta(days=280)
    return estimated_due_date

def get_ovulation_date(last_period_date, cycle_length):
    # Calculate the ovulation date by adding 14 days to the last period date
    ovulation_date = last_period_date + datetime.timedelta(days=14)

    # Adjust the ovulation date based on the cycle length
    if cycle_length != 28:
        ovulation_date += datetime.timedelta(days=cycle_length - 28)

    return ovulation_date

# Get user input for last period date and cycle length
last_period_str = input("Enter the date of your last period (YYYY-MM-DD): ")
cycle_length = int(input("Enter your average cycle length (in days): "))

# Convert the user input into a datetime object
last_period_date = datetime.datetime.strptime(last_period_str, "%Y-%m-%d")

# Calculate the ovulation date
ovulation_date = get_ovulation_date(last_period_date, cycle_length)

# Calculate the due date
due_date = calculate_due_date(ovulation_date)

# Print the estimated due date
print("Your estimated due date is:", due_date.strftime("%Y-%m-%d"))
