from ColorCodeOfTheResistors.ResistorsColor.ResistorsColorCode import Resistor


def test_resistance():
    r1 = Resistor("brown", "black", "red")
    assert r1.get_resistance() == 'resistance: 1000 ohms'

    r2 = Resistor("yellow", "violet", "brown")
    assert r2.get_resistance() == "resistance: 470 ohms"

    r3 = Resistor("orange", "orange", "orange", "gold")
    assert r3.get_resistance() == "resistance: 33000 ohms"


def test_tolerance():
    r1 = Resistor("red", "red", "orange", "red")
    assert r1.get_tolerance() == "tolerance: 2%"

    r2 = Resistor("yellow", "violet", "brown")
    assert r2.get_tolerance() is None

    r3 = Resistor("orange", "orange", "green", "gold")
    assert r3.get_tolerance() == "tolerance: 5%"


def test_band_colors():
    r1 = Resistor("brown", "black", "red")
    assert r1.get_band_colors() == "band colors: brown, black, red, None"

    r2 = Resistor("yellow", "violet", "brown")
    assert r2.get_band_colors() == "band colors: yellow, violet, brown, None"

    r3 = Resistor("orange", "orange", "orange", "gold")
    assert r3.get_band_colors() == "band colors: orange, orange, orange, gold"
