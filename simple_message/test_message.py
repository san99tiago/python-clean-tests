# EXAMPLE OF UNIT-TESTING FOR A SIMPLE-MESSAGE (WITH MULTIPLE IMPORTANT METHODS)
# Santiago Garcia Arango

# Own imports
import simple_message

# Built-in imports
import unittest


class TestSimpleMessage(unittest.TestCase):
    """
    This is a simple TestCase for Simple Messages and the idea is to show the 
    most common setUp and tearDown methods for the unittest framework.
    """
    @classmethod
    def setUpClass(cls):
        print("\n-----> setUpClass execution (only at beggining)")

    @classmethod
    def tearDownClass(cls):
        print("\n--> tearDownClass execution (only at end)")

    def setUp(self):
        print("\n--> setUp execution")

    def tearDown(self):
        print("\n--> tearDown execution")

    def test_simple_message_length(self):
        message = simple_message.SimpleMessage(
            "Santi", "Moni", "Discipline, will sooner or later, defeat intelligence")
        self.assertEqual(len(message.get_message()), 91)

    def test_simple_message_words(self):
        message = simple_message.SimpleMessage(
            "Santi", "George", "Well done is better than well said")
        self.assertTrue(message.get_message().startswith("Sender"))
        self.assertTrue(message.get_message().endswith("said"))

    def test_simple_message_instance(self):
        message = simple_message.SimpleMessage(
            "Santi", "Myself", "Until it is my turn, I will keep celebrating other's success")
        self.assertIsInstance(message, simple_message.SimpleMessage)


if __name__ == "__main__":
    unittest.main()
