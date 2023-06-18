import tkinter as tk

# Create the main window
window = tk.Tk()

# Set the window title
window.title("Fixed-size Window")

# Set the window size
window.geometry("400x300")  # Width x Height in pixels

# Create a label widget
label1 = tk.Label(window, text="Label 1:")
label1.pack()

# Create an entry widget
entry1 = tk.Entry(window)
entry1.pack()

# Create another label widget
label2 = tk.Label(window, text="Label 2:")
label2.pack()

# Create another entry widget
entry2 = tk.Entry(window)
entry2.pack()

# Run the main window event loop
window.mainloop()
