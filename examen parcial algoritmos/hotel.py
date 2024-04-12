from room import Room
from employee import Employee

class Room:
    def __init__(self, room_type, room_number, room_state, room_price):
        self.room_type = room_type
        self.room_number = room_number
        self.room_state = room_state
        self.room_price = room_price

class Employee:
    def __init__(self, emp_id, name, position, salary):
        self.emp_id = emp_id
        self.name = name
        self.position = position
        self.salary = salary

    def get_emp_id(self):
        return self.emp_id

class Hotel:
    """
    Python class to implement a comprehensive hotel management system.

    This class encompasses functionalities for managing hotel rooms, employees, and guest reservations,
    providing a foundational system for hotel operations.

    Syntax
    ------
    obj = Hotel(name, address)

    Parameters
    ----------
    [in] name : str
        The name of the hotel.
    [in] address : str
        The address of the hotel.

    Returns
    -------
    obj : Hotel
        An instance of the Hotel class, representing a single hotel with its management capabilities.

    Attributes
    ----------
    name : str
        The name of the hotel.
    address : str
        The address of the hotel.
    rooms : list
        A list of Room instances representing the rooms available in the hotel.
    employees : list
        A list of Employee instances representing the employees working at the hotel.
    reservations : dict
        A dictionary mapping room numbers to guest names, representing current reservations.
    """

    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.rooms = []
        self.employees = []
        self.reservations = {}

    def add_room(self, room):
        self.rooms.append(room)
        print(f"Room {room.room_number} added successfully.")

    def remove_room(self, room_number):
        self.rooms = [room for room in self.rooms if room.room_number != room_number]
        print(f"Room {room_number} removed successfully.")

    def add_employee(self, employee):
        self.employees.append(employee)
        print(f"Employee {employee.get_emp_id()} added successfully.")

    def remove_employee(self, emp_id):
        self.employees = [emp for emp in self.employees if emp.get_emp_id() != emp_id]
        print(f"Employee {emp_id} removed successfully.")

    def check_in(self, room_number, guest_name):
        room = next((room for room in self.rooms if room.room_number == room_number and room.room_state == "Desocupada"), None)
        if room:
            room.room_state = "Ocupada"
            self.reservations[room_number] = guest_name
            print(f"Check-in successful for {guest_name} in room {room_number}.")
        else:
            print("Room not available or already occupied.")

    def check_out(self, room_number):
        room = next((room for room in self.rooms if room.room_number == room_number), None)
        if room and room.room_state == "Ocupada":
            room.room_state = "Desocupada"
            guest_name = self.reservations.pop(room_number, "")
            print(f"Check-out successful for {guest_name} from room {room_number}.")
        else:
            print("Room not currently occupied or does not exist.")

    def find_room(self, room_number):
        return next((room for room in self.rooms if room.room_number == room_number), None)


def main():
    # TESTING
    print("=================================================================")
    print("Test Case 1: Create a Hotel.")
    print("=================================================================")
    hotel = Hotel("Grand Hotel", "123 Main St")
    if hotel.name == "Grand Hotel":
        print("Test PASS. The parameter name has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    print("=================================================================")
    print("Test Case 2: Add a Room to the Hotel.")
    print("=================================================================")
    room1 = Room("Doble", 101, "Desocupada", 150)
    hotel.add_room(room1)

    print("=================================================================")
    print("Test Case 3: Remove a Room from the Hotel.")
    print("=================================================================")
    hotel.remove_room(101)

    print("=================================================================")
    print("Test Case 4: Add an Employee to the Hotel.")
    print("=================================================================")
    emp1 = Employee(1, "John Doe", "Receptionist", 30000)
    hotel.add_employee(emp1)

    print("=================================================================")
    print("Test Case 5: Remove an Employee from the Hotel.")
    print("=================================================================")
    hotel.remove_employee(1)

    print("=================================================================")
    print("Test Case 6: Check-in a Guest.")
    print("=================================================================")
    room2 = Room("Suite", 102, "Desocupada", 300)
    hotel.add_room(room2)
    hotel.check_in(102, "Alice")

    print("=================================================================")
    print("Test Case 7: Check-out a Guest.")
    print("=================================================================")
    hotel.check_out(102)

    print("=================================================================")
    print("Test Case 8: Attempt Check-in on an Occupied Room.")
    print("=================================================================")
    hotel.check_in(102, "Bob")

if __name__ == "__main__":
    main()
