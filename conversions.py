def convertCelsiusToKelvin(celsius):
    """Takes in a float representing a Celsius measurement,
    and returns that temperature converted into Kelvins"""
    if not isinstance(celsius, float):
        raise TypeError
    kelvins = celsius + 273.15
    kelvins = round(kelvins, 2)
    return kelvins


def convertCelsiusToFahrenheit(celsius):
    """Takes in a float representing a Celsius measurement,
    and returns that temperature converted into Fahrenheit"""
    if not isinstance(celsius, float):
        raise TypeError
    fahrenheit = celsius * 9/5 + 32
    fahrenheit = round(fahrenheit, 2)
    return fahrenheit


def convertFahrenheittoCelsius(fahrenheit):
    """Takes in a float representing a Fahrenheit measurement,
    and returns that temperature converted into Celsius"""
    if not isinstance(fahrenheit, float):
        raise TypeError
    celsius = (fahrenheit - 32) * 5/9
    celsius = round(celsius, 2)
    return celsius


def convertFahrenheittoKelvin(fahrenheit):
    """Takes in a float representing a Fahrenheit measurement,
    and returns that temperature converted into Kelvin"""
    if not isinstance(fahrenheit, float):
        raise TypeError
    kelvin = (fahrenheit - 32) * 5/9 + 273.15
    kelvin = round(kelvin, 2)
    return kelvin


def convertKelvintoFahrenheit(kelvin):
    """Takes in a float representing a Kelvin measurement,
    and returns that temperature converted into Fahrenheit"""
    if not isinstance(kelvin, float):
        raise TypeError
    fahrenheit = (kelvin - 273.15) * 9/5 + 32
    fahrenheit = round(fahrenheit, 2)
    return fahrenheit


def convertKelvintoCelsius(kelvin):
    """Takes in a float representing a Kelvin measurement,
    and returns that temperature converted into Celsius"""
    if not isinstance(kelvin, float):
        raise TypeError
    celsius = kelvin - 273.15
    celsius = round(celsius, 2)
    return celsius
