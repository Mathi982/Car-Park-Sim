import csv
import datetime
import os

CSV_FILE = '20021974_parking_records.csv'
HOURLY_RATE = 2
MAX_PARKING_SPACES = 10

# Dictionary
car_park = {}


# Function to load data from the CSV file at startup
def load_data():
    try:
        with open(CSV_FILE, 'r') as file:
            reader = csv.reader(file)  # Reads each row and populates the car_park dictionary
            for row in reader:
                if len(row) == 6:
                    ticket, reg_num, entry_time, exit_time, space, fee = row  # Determines if car is currently parked
                    is_parked = exit_time == ''
                    car_park[ticket] = {
                        'registration': reg_num,
                        'entry_time': entry_time,
                        'exit_time': exit_time,
                        'space': space,
                        'fee': fee,
                        'is_parked': is_parked
                    }
    except FileNotFoundError:
        file = open(CSV_FILE, 'w')
        file.close() # If the file doesn't exist, do nothing


def save_data():
    file_exists = os.path.exists(CSV_FILE) and os.path.getsize(CSV_FILE) > 0  # Check if file exists and isn't empty
    with open(CSV_FILE, 'w', newline='') as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(['Ticket No.', 'Reg No.', 'Entry Time', 'Exit Time', 'Bay No.', 'Fee (£)'])  # Header for
            # table
        for ticket, details in car_park.items():
            writer.writerow([ticket,
                             details['registration'],
                             details['entry_time'],
                             details.get('exit_time', ''),
                             details['space'],
                             details.get('fee', '')])


def generate_ticket(reg_num):
    current_time = datetime.datetime.now()
    time_str = current_time.strftime('%H%M%S')  # Gets current time and formats into a string
    return reg_num + time_str  # Ticket is the registration plate + time of parking. Makes the ticket unique
    # avoids any mismatches


def enter_car_park(reg_num):
    reg_num = reg_num.strip()  # Makes sure there isn't any spaces that could interfere with the data
    if len([car for car in car_park.values() if car['is_parked']]) >= MAX_PARKING_SPACES:  # Checks if car-park is full
        return "Sorry, the car park is full."

    if not reg_num.strip(): # Can't leave the prompt empty
        return "Registration number cannot be empty."

    new_ticket = generate_ticket(reg_num)  # Use a different variable for the new ticket

    for existing_ticket, details in car_park.items():  # Checks existing tickets to see if car is already parked
        if details['registration'] == reg_num and details['is_parked']:
            return f"Vehicle with registration number {reg_num} is already in the car park."

    entry_time = datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')

    occupied_spaces = [int(details['space']) for details in car_park.values() if details['is_parked']]
    available_spaces = [str(space) for space in range(1, MAX_PARKING_SPACES + 1) if space not in occupied_spaces]
    if not available_spaces:
        return "Sorry, the car park is full."
    space = available_spaces[0]

    car_park[new_ticket] = {'registration': reg_num, 'entry_time': entry_time, 'space': space, 'fee': '0',
                            'is_parked': True}
    save_data()
    return f'Car parked at space {space} with ticket number {new_ticket}.'


def exit_car_park(reg_num):
    if not reg_num.strip():
        return "Registration number cannot be empty."
    parked_tickets = [t for t, details in car_park.items() if details['registration'] == reg_num and details['is_parked'
    ]]
    if not parked_tickets:
        return 'Vehicle not found in the car park.'
    ticket = parked_tickets[-1]
    entry_time = datetime.datetime.strptime(car_park[ticket]['entry_time'], '%d-%m-%Y %H:%M:%S')
    duration = (datetime.datetime.now() - entry_time).seconds / 3600
    fee = round(duration * HOURLY_RATE, 2)
    exit_time = datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')
    car_park[ticket]['exit_time'] = exit_time
    car_park[ticket]['fee'] = str(fee)
    car_park[ticket]['is_parked'] = False
    save_data()
    return f'Parking fee for {duration:.2f} hours is £{fee}.'


def view_available_spaces():
    available_spaces = MAX_PARKING_SPACES - len([car for car in car_park.values() if car['is_parked']])
    return available_spaces


def query_parking_record(ticket):
    if ticket in car_park:
        details = car_park[ticket]
        return (f'Registration: {details["registration"]}'
                f'\nEntry Time: {details["entry_time"]}'
                f'\nExit Time: {details.get("exit_time", "Not yet exited")}'
                f'\nParking Space: {details["space"]}'
                f'\nParking Fee: £{details.get("fee", "0")}')
    else:
        return 'Ticket number not found.'
