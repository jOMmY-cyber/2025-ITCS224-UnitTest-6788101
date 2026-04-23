import unittest

# Functions to be tested
def is_child(age):
    return 0 <= age <= 9

def is_adult(age):
    return 18 <= age <= 59

def is_golden(age):
    return age >= 60

class TestAgeCategories(unittest.TestCase):

    def test_child_age(self):
        """Tests all valid ages in the child category (0-9)."""
        for age in range(10):  # Loops from 0 to 9
            with self.subTest(age=age):
                print(f"{age} is considered as a child.")
                self.assertTrue(is_child(age))

    def test_adult_age(self):
        """Tests all valid ages in the adult category (18-59)."""
        for age in range(18, 60):
            with self.subTest(age=age):
                # print(f"{age} is considered as an adult.") # Optional: matches example style
                self.assertTrue(is_adult(age))

    def test_golden_age(self):
        """Tests a range of valid ages in the golden category (60-80)."""
        for age in range(60, 81):
            with self.subTest(age=age):
                # print(f"{age} is considered as golden.") # Optional: matches example style
                self.assertTrue(is_golden(age))

if __name__ == '__main__':
    # Verbosity=2 is used to show individual test method results
    unittest.main(verbosity=2)