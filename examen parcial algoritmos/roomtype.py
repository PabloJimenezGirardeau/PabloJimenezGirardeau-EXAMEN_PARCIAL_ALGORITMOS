from enum import Enum

class HotelRoomType(Enum):
    """Python class to implement an enumeration for the attribute Hotel Room Type.

    This Python class implements an enumeration for the attribute Hotel Room Type.
    It simplifies the representation of room types within a hotel management system.

    Syntax
    ------
      obj = HotelRoomType.Enum

    Parameters
    ----------

    Returns
    -------
      obj : HotelRoomType
          Python object output parameter that represents an instance
          of the class HotelRoomType.

    Attributes
    ----------
    INDIVIDUAL: 'Individual' - Represents an individual room type.
    DOBLE: 'Doble' - Represents a double room type.
    SUITE: 'Suite' - Represents a suite room type.
    """
    INDIVIDUAL = "Individual"
    DOBLE = "Doble"
    SUITE = "Suite"


def main():
    # TESTING
    print("=================================================================.")
    print("Test Case 1: Check Class HotelRoomType.")
    print("=================================================================.")

    if isinstance(HotelRoomType.INDIVIDUAL, HotelRoomType):
        print("Test PASS. The enum for Individual has been correctly set.")
    else:
        print("Test FAIL. Check the enum definition.")

    if isinstance(HotelRoomType.DOBLE, HotelRoomType):
        print("Test PASS. The enum for Doble has been correctly set.")
    else:
        print("Test FAIL. Check the enum definition.")

    if isinstance(HotelRoomType.SUITE, HotelRoomType):
        print("Test PASS. The enum for Suite has been correctly set.")
    else:
        print("Test FAIL. Check the enum definition.")

if __name__ == "__main__":
    main()
