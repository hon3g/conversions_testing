def convert(fromUnit, toUnit, value):
    if fromUnit.lower() == toUnit.lower():
        return value
    return {
        'celsius kelvin':     lambda: value + 273.15,
        'celsius fahrenheit': lambda: value * 9/5 + 32,
        'fahrenheit celsius': lambda: (value - 32) * 5/9,
        'fahrenheit kelvin':  lambda: (value - 32) * 5/9 + 273.15,
        'kelvin fahrenheit':  lambda: (value - 273.15) * 9/5 + 32,
        'kelvin celsius':     lambda: value - 273.15,
        'mile yard':  lambda: value * 1760,
        'mile meter': lambda: value * 1609.344,
        'yard mile':  lambda: value / 1760,
        'yard meter': lambda: value / 1.094,
        'meter mile': lambda: value / 1609.344,
        'meter yard': lambda: value * 1.094,
    }.get(
        ''.join((fromUnit.lower(), ' ', toUnit.lower())),
        lambda: exec('raise(ConversionNotPossible())')
    )()


class ConversionNotPossible(Exception):
    pass
