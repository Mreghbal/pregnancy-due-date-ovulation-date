import tkinter as tk
from tkinter import messagebox
import datetime

def calculate_due_date():
    try:
        # Get user input for last period date and cycle length
        last_period_str = last_period_entry.get()
        cycle_length = int(cycle_length_entry.get())

        # Convert the user input into a datetime object
        last_period_date = datetime.datetime.strptime(last_period_str, "%Y-%m-%d")

        # Calculate the ovulation date
        ovulation_date = get_ovulation_date(last_period_date, cycle_length)

        # Calculate the due date
        due_date = calculate_due_date(ovulation_date)

        # Show the estimated due date in a message box
        messagebox.showinfo("Due Date", "Your estimated due date is: {}".format(due_date.strftime("%Y-%m-%d")))

    except ValueError:
        messagebox.showerror("Error", "Invalid input!")

def get_ovulation_date(last_period_date, cycle_length):
    # Calculate the ovulation date by adding 14 days to the last period date
    ovulation_date = last_period_date + datetime.timedelta(days=14)

    # Adjust the ovulation date based on the cycle length
    if cycle_length != 28:
        ovulation_date += datetime.timedelta(days=cycle_length - 28)

    return ovulation_date

# Create the main window
window = tk.Tk()
window.title("Due Date Calculator")

# Create labels and entry fields for last period date and cycle length
last_period_label = tk.Label(window, text="Last Period Date (YYYY-MM-DD):")
last_period_label.pack()
last_period_entry = tk.Entry(window)
last_period_entry.pack()

cycle_length_label = tk.Label(window, text="Cycle Length (in days):")
cycle_length_label.pack()
cycle_length_entry = tk.Entry(window)
cycle_length_entry.pack()

# Create a button to calculate the due date
calculate_button = tk.Button(window, text="Calculate", command=calculate_due_date)
calculate_button.pack()

# Run the GUI event loop
window.mainloop()
