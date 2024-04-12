class Room:
    def __init__(self, room_type, room_number, room_state, room_price):
        self.room_type = room_type
        self.room_number = room_number
        self.room_state = room_state
        self.room_price = room_price

    def get_room_number(self):
        return self.room_number

    def get_room_type(self):
        return self.room_type

    def get_room_state(self):
        return self.room_state

    def get_room_price(self):
        return self.room_price

class Employee:
    def __init__(self, emp_id, name, position, salary):
        self.emp_id = emp_id
        self.name = name
        self.position = position
        self.salary = salary

    def get_emp_id(self):
        return self.emp_id

    def get_name(self):
        return self.name

    def get_position(self):
        return self.position

    def get_salary(self):
        return self.salary

class Hotel:
    def __init__(self, name):
        self.name = name
        self.rooms = []
        self.employees = []
        self.reservations = {}

    def add_room(self, room):
        self.rooms.append(room)

    def remove_room(self, room_number):
        self.rooms = [room for room in self.rooms if room.room_number != room_number]

    def add_employee(self, employee):
        self.employees.append(employee)

    def remove_employee(self, emp_id):
        self.employees = [emp for emp in self.employees if emp.get_emp_id() != emp_id]

    def check_in(self, room_number, guest_name):
        for room in self.rooms:
            if room.room_number == room_number and room.room_state == "Desocupada":
                room.room_state = "Ocupada"
                self.reservations[room_number] = guest_name
                return f"Check-in successful for {guest_name} in room {room_number}."
        return "Room not available or already occupied."

    def check_out(self, room_number):
        for room in self.rooms:
            if room.room_number == room_number and room.room_state == "Ocupada":
                room.room_state = "Desocupada"
                guest_name = self.reservations.pop(room_number, None)
                return f"Check-out successful for {guest_name} from room {room_number}."
        return "Room not currently occupied or does not exist."

def main_menu():
    print("\nWelcome to the Hotel Management System")
    print("1. Hotel Management")
    print("2. Employee Management")
    print("3. Room Management")
    print("4. Exit")
    return input("Please select an option (1-4): ")

def hotel_menu():
    print("\nHotel Management")
    print("1. Add Room")
    print("2. Remove Room")
    print("3. Add Employee")
    print("4. Remove Employee")
    print("5. Check-in Guest")
    print("6. Check-out Guest")
    print("7. Return to Main Menu")
    return input("Please select an option (1-7): ")

def employee_menu():
    print("\nEmployee Management")
    print("1. View Employee Details")
    print("2. Update Employee Position")
    print("3. Update Employee Salary")
    print("4. Return to Main Menu")
    return input("Please select an option (1-4): ")

def room_menu():
    print("\nRoom Management")
    print("1. Check Room Availability")
    print("2. Check-in to Room")
    print("3. Check-out of Room")
    print("4. Return to Main Menu")
    return input("Please select an option (1-4): ")

def main():
    hotel = Hotel("Grand Hotel")
    running = True
    while running:
        choice = main_menu()
        if choice == '1':
            while True:
                hotel_choice = hotel_menu()
                if hotel_choice == '1':
                    # Add Room
                    room_type = input("Enter room type (Individual, Doble, Suite): ")
                    room_number = int(input("Enter room number: "))
                    room_state = "Desocupada"
                    room_price = float(input("Enter price per night: "))
                    hotel.add_room(Room(room_type, room_number, room_state, room_price))
                    print("Room added successfully.")
                elif hotel_choice == '2':
                    # Remove Room
                    room_number = int(input("Enter room number to remove: "))
                    hotel.remove_room(room_number)
                    print("Room removed successfully.")
                elif hotel_choice == '3':
                    # Add Employee
                    emp_id = int(input("Enter employee ID: "))
                    name = input("Enter employee name: ")
                    position = input("Enter position: ")
                    salary = float(input("Enter salary: "))
                    hotel.add_employee(Employee(emp_id, name, position, salary))
                    print("Employee added successfully.")
                elif hotel_choice == '4':
                    # Remove Employee
                    emp_id = int(input("Enter employee ID to remove: "))
                    hotel.remove_employee(emp_id)
                    print("Employee removed successfully.")
                elif hotel_choice == '5':
                    # Check-in Guest
                    room_number = int(input("Enter room number for check-in: "))
                    guest_name = input("Enter guest name: ")
                    print(hotel.check_in(room_number, guest_name))
                elif hotel_choice == '6':
                    # Check-out Guest
                    room_number = int(input("Enter room number for check-out: "))
                    print(hotel.check_out(room_number))
                elif hotel_choice == '7':
                    break
                else:
                    print("Invalid option. Please try again.")
        elif choice == '2':
            # Since detailed Employee management functionality might require accessing the specific employee,
            # let's assume viewing details for now. Implementing edit functionalities would require storing employees in a more accessible way.
            print("Listing all employees:")
            for emp in hotel.employees:
                print(f"ID: {emp.get_emp_id()}, Name: {emp.get_name()}, Position: {emp.get_position()}, Salary: ${emp.get_salary()}")
            input("Press Enter to return to the main menu...")
        elif choice == '3':
            # Room management here is limited due to the Room's methods primarily being managed through the Hotel class.
            print("Listing all rooms:")
            for room in hotel.rooms:
                print(f"Room Number: {room.get_room_number()}, Type: {room.get_room_type()}, State: {room.get_room_state()}, Price: ${room.get_room_price()}")
            input("Press Enter to return to the main menu...")
        elif choice == '4':
            print("Exiting...")
            running = False
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
