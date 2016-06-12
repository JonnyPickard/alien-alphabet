from minglish import answer
import unittest

class TestMyFunctions(unittest.TestCase):
    def test_returns_correct_string(self):
        self.assertEqual(answer(["z", "yx", "yz"]), "xzy")

    # def test_returns_correct_string(self):
    #     self.assertEqual(answer(),)

if __name__ == '__main__':
    unittest.main(exit=False)
