import unittest

class TestExample(unittest.TestCase):

    def test_number_of_lines(self):
        with open("./test-input", "r") as test_input_file:
            i = 0
            for line in test_input_file:
                print(line)
                i += 1
            self.assertEqual(i, 4)


if __name__ == '__main__':
    unittest.main()