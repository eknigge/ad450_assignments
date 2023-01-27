from unittest import TestCase
from percent_gpa import calculate_gpa 

class Test_GPA(TestCase):
    int_answers = {
        95: 4.0,
        94:3.9,
        93: 3.8,
        67:1.2,
        55:0.0
    }
    float_answers = {
        75.2: 2.0,
        84.1: 2.9,
        90.5: 3.5,
        94.8: 3.9,
        55.0: 0.0,
        98.8: 4.0
    }

    def test_gpa_integers(self):
        for score in self.int_answers:
            expected = self.int_answers[score]
            calculated = calculate_gpa(score)
            self.assertEqual(expected, calculated)
    
    def test_gpa_float(self):
        for score in self.float_answers:
            expected = self.float_answers[score]
            calculated = calculate_gpa(score)
            self.assertEqual(expected, calculated)