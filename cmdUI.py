import CarPark

def main():
    CarPark.load_data()
    while True:
        print('\nCar Park Simulation')
        print('1. Enter the car park')
        print('2. Exit the car park')
        print('3. View available parking spaces')
        print('4. Query parking record by ticket number')
        print('5. Quit')
        choice = input('Enter your choice: ')

        if choice not in ['1', '2', '3', '4', '5']:
            print("Invalid choice. Please enter a number between 1 and 5.")
            continue

        if choice == '1':
            reg_num = input("Please enter the vehicle's registration number: ")
            message = CarPark.enter_car_park(reg_num)
            print(message)
        elif choice == '2':
            reg_num = input("Enter the vehicle's registration number: ")
            message = CarPark.exit_car_park(reg_num)
            print(message)
        elif choice == '3':
            available_spaces = CarPark.view_available_spaces()
            print(f'Available parking spaces: {available_spaces}')
        elif choice == '4':
            ticket = input("Please enter your ticket number: ")
            message = CarPark.query_parking_record(ticket)
            print(message)
        elif choice == '5':
            CarPark.save_data()
            print("Thank you for using the Car Park Simulator.")
            break

if __name__ == '__main__':
    main()
