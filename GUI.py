import tkinter as tk
import CarPark

def show_entry_field(prompt):
    ticket_entry.delete(0, tk.END)  # Clear the entry field
    ticket_entry.pack(side=tk.TOP, fill=tk.X, padx=20, pady=5)
    enter_operation_button.pack(side=tk.TOP, pady=5)
    result_label.config(text=prompt)

def hide_entry_field():
    ticket_entry.pack_forget()
    enter_operation_button.pack_forget()

def enter_car_park():
    reg_num = ticket_entry.get()
    message = CarPark.enter_car_park(reg_num)
    result_label.config(text=message)
    hide_entry_field()

def exit_car_park():
    reg_num = ticket_entry.get()
    message = CarPark.exit_car_park(reg_num)
    result_label.config(text=message)
    hide_entry_field()

def view_available_spaces():
    available_spaces = CarPark.view_available_spaces()
    result_label.config(text=f'Available parking spaces: {available_spaces}')

def query_parking_record():
    ticket = ticket_entry.get()
    message = CarPark.query_parking_record(ticket)
    result_label.config(text=message)
    hide_entry_field()

def execute_operation():
    operation_funcs = {
        "enter": enter_car_park,
        "exit": exit_car_park,
        "view_spaces": view_available_spaces,
        "query_record": query_parking_record
    }
    operation_funcs[last_operation]()

def set_last_operation(operation):
    global last_operation
    last_operation = operation
    if operation in ["enter", "exit", "query_record"]:
        prompts = {
            "enter": "Enter vehicle's registration number:",
            "exit": "Enter vehicle's registration number to exit:",
            "query_record": "Enter ticket number to query:"
        }
        show_entry_field(prompts[operation])
    else:
        execute_operation()

def quit_gui():
    CarPark.save_data()
    result_label.config(text="Thank you for using the Car Park Simulator.")
    root.after(2000, root.destroy)

def on_close(): # Data will still be saved if the close button is pressed instead of quit
    CarPark.save_data() 
    root.destroy()

# Main window stuff
root = tk.Tk()
root.title("Car Park Simulator")
root.protocol("WM_DELETE_WINDOW", on_close)

# Initialize CarPark data
CarPark.load_data()

# Button frames
button_frame = tk.Frame(root)
button_frame.pack(side=tk.LEFT, padx=10, pady=10)

# Buttons
enter_button = tk.Button(button_frame, text="Enter Car Park (Hourly Rate: £2)", command=lambda: set_last_operation("enter"))
exit_button = tk.Button(button_frame, text="Exit Car Park", command=lambda: set_last_operation("exit"))
view_spaces_button = tk.Button(button_frame, text="View Available Spaces", command=lambda: set_last_operation("view_spaces"))
query_record_button = tk.Button(button_frame, text="Query Parking Record", command=lambda: set_last_operation("query_record"))
quit_button = tk.Button(button_frame, text="Quit", command=quit_gui)

# Arrange buttons in the frame
enter_button.pack(fill=tk.X)
exit_button.pack(fill=tk.X)
view_spaces_button.pack(fill=tk.X)
query_record_button.pack(fill=tk.X)
quit_button.pack(fill=tk.X)

# Create an entry field and result label
ticket_entry = tk.Entry(root)
result_label = tk.Label(root, text="Welcome to the Car Park Simulator")
result_label.pack(side=tk.TOP, padx=10, pady=10)

# Create an Enter button for operations
enter_operation_button = tk.Button(root, text="Enter", command=execute_operation)

# Initially hide the entry field and Enter button
hide_entry_field()

# Run the application
root.mainloop()
