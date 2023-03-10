from ColorCodeOfTheResistors.ResistorsColor.ResistorsColorCode import Resistor


def test_resistance():
    r1 = Resistor("brown", "black", "red")
    assert r1.get_resistance() == 'resistance: 1.000 Kohms'

    r2 = Resistor("yellow", "violet", "brown")
    assert r2.get_resistance() == "resistance: 470.000 ohms"

    r3 = Resistor("orange", "orange", "orange", "gold")
    assert r3.get_resistance() == "resistance: 33.000 Kohms"


def test_band_colors():
    r1 = Resistor("brown", "black", "red")
    assert r1.get_band_colors() == "band colors: brown, black, red, None"

    r2 = Resistor("yellow", "violet", "brown")
    assert r2.get_band_colors() == "band colors: yellow, violet, brown, None"

    r3 = Resistor("orange", "orange", "orange", "gold")
    assert r3.get_band_colors() == "band colors: orange, orange, orange, gold"
