from enum import Enum

# Define un enum para los tipos de habitación permitidos.
class RoomType(Enum):
    INDIVIDUAL = "Individual"
    DOBLE = "Doble"
    SUITE = "Suite"

class Room:
    """Python class to implement a basic version of a hotel room.

    This Python class implements the basic functionalities of a hotel room in a 
    simple hotel management system.

    Syntax
    ------
    obj = Room(room_type, room_number, room_state, room_price)

    Parameters
    ----------
    [in] room_type : RoomType
        Valid values are RoomType.INDIVIDUAL, RoomType.DOBLE, RoomType.SUITE.
    [in] room_number : int
        Unique number of the room.
    [in] room_state : str
        Occupancy state of the room. Expected values are "Ocupada" or "Desocupada".
    [in] room_price : float
        Price per night for the room.

    Returns
    -------
    obj : Room
        Python object output parameter that represents an instance of the class Room.
    """

    def __init__(self, room_type, room_number, room_state, room_price):
        if not isinstance(room_type, RoomType):
            raise ValueError("Invalid room type. Must be a 'RoomType' enum.")
        if not isinstance(room_number, int):
            raise ValueError("Room number must be an integer.")
        if room_state not in ["Ocupada", "Desocupada"]:
            raise ValueError("Room state must be 'Ocupada' or 'Desocupada'.")
        if not isinstance(room_price, (int, float)):
            raise ValueError("Room price must be a numeric value.")

        self.room_type = room_type
        self.room_number = room_number
        self.room_state = room_state
        self.room_price = room_price

    def is_occupied(self):
        return self.room_state == "Ocupada"

    def check_in(self):
        if self.is_occupied():
            return "La habitación ya está ocupada."
        self.room_state = "Ocupada"
        return "Check-in realizado con éxito."

    def check_out(self):
        if not self.is_occupied():
            return "La habitación ya está desocupada."
        self.room_state = "Desocupada"
        return "Check-out realizado con éxito."


def main():
    #TESTING
    print("=================================================================")
    print("Test Case 1: Create a Room.")
    print("=================================================================")
    room1 = Room(RoomType.DOBLE, 101, "Desocupada", 150)

    if room1.room_type == RoomType.DOBLE:
        print("Test PASS. The parameter room_type has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if room1.room_number == 101:
        print("Test PASS. The parameter room_number has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if room1.room_state == "Desocupada":
        print("Test PASS. The parameter room_state has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if room1.room_price == 150:
        print("Test PASS. The parameter room_price has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    print("=================================================================")
    print("Test Case 2: Check-in a Room.")
    print("=================================================================")
    check_in_result = room1.check_in()

    if check_in_result == "Check-in realizado con éxito." and room1.is_occupied():
        print("Test PASS. Check-in functionality has been implemented correctly.")
    else:
        print("Test FAIL. Check the method check_in().")

    print("=================================================================")
    print("Test Case 3: Check-out a Room.")
    print("=================================================================")
    check_out_result = room1.check_out()

    if check_out_result == "Check-out realizado con éxito." and not room1.is_occupied():
        print("Test PASS. Check-out functionality has been implemented correctly.")
    else:
        print("Test FAIL. Check the method check_out().")

if __name__ == "__main__":
    main()
