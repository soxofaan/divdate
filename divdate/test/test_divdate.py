import unittest
import datetime
from divdate import ddate


class DivDateTest(unittest.TestCase):
    def test_year(self):
        year = ddate / 2015
        self.assertIsInstance(year, datetime.date)
        self.assertEqual(datetime.date(2015, 1, 1).timetuple(), year.timetuple())

    def test_month(self):
        month = ddate / 2015 / 11
        self.assertIsInstance(month, datetime.date)
        self.assertEqual(datetime.date(2015, 11, 1).timetuple(), month.timetuple())

    def test_invalid_month(self):
        self.assertRaises(ValueError, lambda: ddate / 2015 / 13)

    def test_day(self):
        day = ddate / 2015 / 11 / 23
        self.assertIsInstance(day, datetime.date)
        self.assertEqual(datetime.date(2015, 11, 23).timetuple(), day.timetuple())

    def test_invalid_day(self):
        self.assertRaises(ValueError, lambda: ddate / 2015 / 11 / 32)

    def test_hour(self):
        hour = ddate / 2015 / 11 / 23 / 14
        self.assertIsInstance(hour, datetime.datetime)
        self.assertEqual(datetime.datetime(2015, 11, 23, 14, 0, 0).timetuple(), hour.timetuple())

    def test_invalid_hour(self):
        self.assertRaises(ValueError, lambda: ddate / 2015 / 11 / 23 / 26)

    def test_minute(self):
        minute = ddate / 2015 / 11 / 23 / 14 / 53
        self.assertIsInstance(minute, datetime.datetime)
        self.assertEqual(datetime.datetime(2015, 11, 23, 14, 53, 0).timetuple(), minute.timetuple())

    def test_invalid_minute(self):
        self.assertRaises(ValueError, lambda: ddate / 2015 / 11 / 23 / 14 / 72)

    def test_second(self):
        second = ddate / 2015 / 11 / 23 / 14 / 53 / 57
        self.assertIsInstance(second, datetime.datetime)
        self.assertEqual(datetime.datetime(2015, 11, 23, 14, 53, 57).timetuple(), second.timetuple())

    def test_invalid_second(self):
        self.assertRaises(ValueError, lambda: ddate / 2015 / 11 / 23 / 14 / 53 / 89)

    def test_microsecond(self):
        ms = ddate / 2015 / 11 / 23 / 14 / 53 / 57 / 12345
        self.assertIsInstance(ms, datetime.datetime)
        self.assertEqual(datetime.datetime(2015, 11, 23, 14, 53, 57, 12345).timetuple(), ms.timetuple())
        self.assertEqual(12345, ms.microsecond)

    def test_invalid_microsecond(self):
        self.assertRaises(ValueError, lambda: ddate / 2015 / 11 / 23 / 14 / 53 / 57 / 1234567)
