class Resistor:
    """
    A class that represents an electrical resistor and calculates its resistance
    and tolerance based on the color code of its bands.
    """

    color_codes = {
        "black": 0,
        "brown": 1,
        "red": 2,
        "orange": 3,
        "yellow": 4,
        "green": 5,
        "blue": 6,
        "violet": 7,
        "gray": 8,
        "white": 9
    }

    def __init__(self, band1, band2, band3=None, band4=None):
        """
        Initializes a new Resistor object with the given color codes for its bands.

        Args:
            band1 (str): The color code of the first band.
            band2 (str): The color code of the second band.
            band3 (str, optional): The color code of the third band (if applicable).
            band4 (str, optional): The color code of the fourth band (if applicable).
        """
        self.band1 = band1.lower()
        self.band2 = band2.lower()
        self.band3 = band3.lower() if band3 else None
        self.band4 = band4.lower() if band4 else None

    def get_resistance(self):
        """
        Calculates the resistance value of the resistor based on the color code of its bands.

        Returns:
            tuple: A tuple containing the resistance value of the resistor in ohms and a string representation of the value with its unit.
        """
        value = (self.color_codes[self.band1] * 10 + self.color_codes[self.band2]) * (
                    10 ** self.color_codes[self.band3])
        units = ["ohms", "Kohms", "Mohms", "Gohms"]
        i = 0
        while value >= 1000 and i < len(units) - 1:
            value /= 1000
            i += 1
        return f"resistance: {value:.3f} {units[i]}"

    def get_band_colors(self):
        """
        Returns a list of the color codes of all four bands of the resistor.

        Returns:
            list: A list of strings representing the color codes of the resistor's bands.
        """
        return f"band colors: {self.band1}, {self.band2}, {self.band3}, {self.band4}"


if __name__ == '__main__':
    resistor = Resistor("brown", "black", "red")
    print(resistor.get_resistance())
    print(resistor.get_band_colors())
