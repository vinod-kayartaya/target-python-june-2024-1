import unittest
from myutils import max_days


class TestMyUtilsMaxDays(unittest.TestCase):

    def test_for_february_leap_year(self):
        want = 29
        got = max_days(2, 2024)
        self.assertEqual(want, got)
        got = max_days(2, 2028)
        self.assertEqual(want, got)
        got = max_days(2, 2020)
        self.assertEqual(want, got)

    def test_for_february_non_leap_year(self):
        want = 28
        got = max_days(2, 2021)
        self.assertEqual(want, got)

    def test_for_invalid_month(self):
        try:
            max_days(222, 2222)
            self.fail('Was expecting an error, didn\'t get one')
        except ValueError:
            pass
        except Exception as e:
            self.fail(f'Was expecting ValueError, but got {type(e)}')

    def test_for_invalid_year(self):
        with self.assertRaises(ValueError):
            max_days(1, 0)


# if the following is not included, run the tests using the command in the CLI: python -m unittest ex28_unit_tests.py
if __name__ == '__main__':
    unittest.main()
