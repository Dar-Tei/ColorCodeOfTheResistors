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
            str: A string representation of the resistor resistance value in ohms.
        """
        value = (self.color_codes[self.band1] * 10 + self.color_codes[self.band2]) * (
                    10 ** self.color_codes[self.band3])

        return f"resistance: {value} ohms"

    def get_tolerance(self):
        """
        Calculates the tolerance value of the resistor based on the color code of its fourth band.

        Returns:
            str: A string representation of the resistor tolerance value as a percentage (if applicable).
        """
        if self.band4:
            tolerance_values = {"brown": 1, "red": 2, "green": 0.5, "blue": 0.25, "violet": 0.1, "gray": 0.05, "gold": 5, "silver": 10}
            return f"tolerance: {tolerance_values[self.band4]}%"
        else:
            return None

    def get_band_colors(self):
        """
        Returns a string representation of the color codes of the resistor bands.

        Returns:
            str: A string representation of the color codes of the resistor bands.
        """
        return f"band colors: {self.band1}, {self.band2}, {self.band3}, {self.band4}"


if __name__ == '__main__':
    resistor = Resistor("yellow", "violet", "brown", "gold")
    print(resistor.get_band_colors())
    print(resistor.get_resistance())
    print(resistor.get_tolerance())

