import conversions
from conversions_refactored \
import convert, ConversionNotPossible
import unittest


class ConversionFunctions(unittest.TestCase):
    # C to K
    def test_ck_function(self):
        with self.assertRaises(TypeError,
                               msg='Getting an incorrect type '
                                   'should raise a TypeError'):
            conversions.convertCelsiusToKelvin(999)

        cases = (
            (500.00, 773.15),
            (490.00, 763.15),
            (0.00,   273.15),
            (-10.00, 263.15),
            (-273.15,  0.00),
        )
        for c, k in cases:
            result = conversions.convertCelsiusToKelvin(c)
            self.assertEqual(result, k,
                             msg=f'Test case C:{c} K:{k} failed')

    # C to F
    def test_cf_function(self):
        with self.assertRaises(TypeError,
                               msg='Getting an incorrect type '
                                   'should raise a TypeError'):
            conversions.convertCelsiusToKelvin(999)

        cases = (
            (500.00,   932.00),
            (490.00,   914.00),
            (0.00,      32.00),
            (-10.00,    14.00),
            (-273.15, -459.67),
        )
        for c, f in cases:
            result = conversions.convertCelsiusToFahrenheit(c)
            self.assertEqual(result, f,
                             msg=f'Test case failed: C:{c} F:{f}')

    # F to C
    def test_fc_function(self):
        with self.assertRaises(TypeError,
                               msg='Getting an incorrect type '
                                   'should raise a TypeError'):
            conversions.convertFahrenheittoCelsius(999)

        cases = (
            (500.00,   932.00),
            (490.00,   914.00),
            (0.00,      32.00),
            (-10.00,    14.00),
            (-273.15, -459.67),
        )
        for c, f in cases:
            result = conversions.convertFahrenheittoCelsius(f)
            self.assertEqual(result, c,
                             msg=f'Test case failed: F:{f} C:{c}')

    # F to K
    def test_fk_function(self):
        with self.assertRaises(TypeError,
                               msg='Getting an incorrect type '
                                   'should raise a TypeError'):
            conversions.convertFahrenheittoKelvin(999)

        cases = (
            (773.15,   932.00),
            (763.15,   914.00),
            (273.15,    32.00),
            (263.15,    14.00),
            (0.00,    -459.67),
        )
        for k, f in cases:
            result = conversions.convertFahrenheittoKelvin(f)
            self.assertEqual(result, k,
                             msg=f'Test case failed: F:{f} K:{k}')

    # K to F
    def test_kf_function(self):
        with self.assertRaises(TypeError,
                               msg='Getting an incorrect type '
                                   'should raise a TypeError'):
            conversions.convertKelvintoFahrenheit(999)

        cases = (
            (773.15,   932.00),
            (763.15,   914.00),
            (273.15,    32.00),
            (263.15,    14.00),
            (0.00,    -459.67),
        )
        for k, f in cases:
            result = conversions.convertKelvintoFahrenheit(k)
            self.assertEqual(result, f,
                             msg=f'Test case failed: K:{k} F:{f}')

    # K to C
    def test_kc_function(self):
        with self.assertRaises(TypeError,
                               msg='Getting an incorrect type '
                                   'should raise a TypeError'):
            conversions.convertKelvintoCelsius(999)

        cases = (
            (500.00, 773.15),
            (490.00, 763.15),
            (0.00,   273.15),
            (-10.00, 263.15),
            (-273.15,  0.00),
        )
        for c, k in cases:
            result = conversions.convertKelvintoCelsius(k)
            self.assertEqual(result, c,
                             msg=f'Test case failed: C:{c} K:{k}')


class RefactoredConversions(unittest.TestCase):
    cases = {
        ('Celsius', 'Kelvin'): (
            (500.00, 773.15),
            (490.00, 763.15),
            (0.00, 273.15),
            (-10.00, 263.15),
            (-273.15, 0.00),
        ),
        ('Celsius', 'Fahrenheit'): (
            (500.00, 932.00),
            (490.00, 914.00),
            (0.00, 32.00),
            (-10.00, 14.00),
            (-273.15, -459.67),
        ),
        ('Fahrenheit', 'Celsius'): (
            (932.00, 500.00),
            (914.00, 490.00),
            (32.00, 0.00),
            (14.00, -10.00),
            (-459.67, -273.15),
        ),
        ('Fahrenheit', 'Kelvin'): (
            (932.00, 773.15),
            (914.00, 763.15),
            (32.00, 273.15),
            (14.00, 263.15),
            (-459.67, 0.00),
        ),
        ('Kelvin', 'Fahrenheit'): (
            (773.15, 932.00),
            (763.15, 914.00),
            (273.15, 32.00),
            (263.15, 14.00),
            (0.00, -459.67),
        ),
        ('Kelvin', 'Celsius'): (
            (773.15, 500.00),
            (763.15, 490.00),
            (273.15, 0.00),
            (263.15, -10.00),
            (0.00, -273.15),
        ),
        ('Mile', 'Yard'): (
            (0, 0),
            (1, 1760),
            (15, 26400),
            (19, 33440),
            (58, 102080),
        ),
        ('Mile', 'Meter'): (
            (0, 0),
            (1, 1609.34),
            (15, 24140.16),
            (19, 30577.54),
            (58, 93341.95),
        ),
        ('Yard', 'Mile'): (
            (0, 0),
            (100, 0.0568182),
            (1500, 0.8522727),
            (1900, 1.079545),
            (5800, 3.295455),
        ),
        ('Yard', 'Meter'): (
            (0, 0),
            (1, 0.9144),
            (15, 13.716),
            (19, 17.3674),
            (58, 53.0352),
        ),
        ('Meter', 'Mile'): (
            (0, 0),
            (100, 0.0621371),
            (1500, 0.9320568),
            (1900, 1.180605),
            (5800, 3.603953),
        ),
        ('Meter', 'Yard'): (
            (0, 0),
            (1, 1.09361),
            (15, 16.4042),
            (19, 20.7787),
            (58, 63.4296),
        ),
    }

    def test_refactored_conversions_function(self):

        for units, values in self.cases.items():
            for n, expected in values:
                from_unit, to_unit = units
                actual = convert(from_unit, to_unit, n)
                self.assertAlmostEqual(expected, actual, places=1,
                                       msg=f'{from_unit} to {to_unit}')

        self.assertEqual(123, convert('Meter', 'Meter', 123))

        with self.assertRaises(ConversionNotPossible,
                               msg='Converting from incompatible units '
                                   'should raise a '
                                   'ConversionNotPossible exception'):
            convert('Fahrenheit', 'Yard', 123)


if __name__ == '__main__':
    unittest.main()
