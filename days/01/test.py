import unittest
import solve

class TestExample(unittest.TestCase):

    def test_number_of_lines(self):
        expected = 142
        with open("./test-input", "r") as test_input_file:
            result = solve.solve_file(test_input_file)
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()