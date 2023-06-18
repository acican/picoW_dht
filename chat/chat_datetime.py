import tkinter as tk
from datetime import datetime

def update_datetime():
    current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    datetime_label.config(text=current_datetime)
    datetime_label.after(1000, update_datetime)  # Update every 1 second (1000 milliseconds)

# Create Tkinter window
window = tk.Tk()
window.title("Date and Time Display")

# Create label widget for displaying date and time
datetime_label = tk.Label(window, font=("Helvetica", 18), fg="black")
datetime_label.pack(pady=20)

# Update the date and time initially and start updating it periodically
update_datetime()

# Start the Tkinter event loop
window.mainloop()
