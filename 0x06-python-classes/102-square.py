#!/usr/bin/python3
"""Square class definition"""


class Square:
    """Square class"""

    def __init__(self, size=0):
        """Square constructor

        Args:
            size (int): length of a side of the Square
        """
        self.__size = size

    @property
    def size(self):
        """Property for the size of the Square

        Raises:
            TypeError: If size is not an integer
            ValueError: If size is less than 0
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for the size of the Square

        Args:
            value (int): The new size value

        Raises:
            TypeError: If size is not an integer
            ValueError: If size is less than 0
        """
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """Calculate the area of the Square

        Returns:
            int: The area of the Square
        """
        return self.__size * self.__size

    def __le__(self, other):
        return self.area() <= other.area()

    def __lt__(self, other):
        return self.area() < other.area()

    def __ge__(self, other):
        return self.area() >= other.area()

    def __ne__(self, other):
        return self.area() != other.area()

    def __gt__(self, other):
        return self.area() > other.area()

    def __eq__(self, other):
        return self.area() == other.area()

