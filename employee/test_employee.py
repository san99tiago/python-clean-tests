# EXAMPLE OF UNIT-TESTING FOR A EMPLOYEE
# Santiago Garcia Arango

# Own imports
from employee import Employee

# Built-in imports
import unittest
from unittest.mock import patch


class TestEmployee(unittest.TestCase):
    """
    TestEmployee inherits from unittest.TestCase in order to get special 
    methods that enable testing our Employee.
    """

    def setUp(self):
        print("\n-----Setting up employees to test-----")
        self.emp_1 = Employee("Santiago", "Garcia", 100, "DevOps")
        self.emp_2 = Employee("Monica", "Hill", 100, "Finance")

    def test_email(self):
        print("Testing email creation...")
        self.assertEqual(self.emp_1.email, "santiago.garcia@gmail.com")
        self.assertEqual(self.emp_2.email, "monica.hill@gmail.com")

        # Change name and lastname respectively and validate result
        self.emp_1.name = "Tiago"
        self.emp_2.lastname = "Garcia"

        self.assertEqual(self.emp_1.email, "tiago.garcia@gmail.com")
        self.assertEqual(self.emp_2.email, "monica.garcia@gmail.com")

    def test_fullname(self):
        print("Testing fullnames...")
        self.assertEqual(self.emp_1.fullname, "Santiago Garcia")
        self.assertEqual(self.emp_2.fullname, "Monica Hill")

        # Change name and lastname respectively and validate result
        self.emp_1.name = "Tiago"
        self.emp_2.lastname = "Garcia"

        self.assertEqual(self.emp_1.fullname, "Tiago Garcia")
        self.assertEqual(self.emp_2.fullname, "Monica Garcia")

    def test_apply_raise(self):
        print("Testing salary raises...")
        self.emp_1.apply_raise_to_salary()
        self.emp_2.apply_raise_to_salary()

        # The results should be different because of the raise conditions
        self.assertEqual(self.emp_1.salary, 108)
        self.assertEqual(self.emp_2.salary, 105)

    def test_get_monthly_schedule(self):
        print("Testing the acquisition of monthly schedules...")
        with patch("employee.requests.get") as mocked_get:
            # Test an OK response
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = "Success"
            emp_1_schedule = self.emp_1.get_monthly_schedule("Sep")
            mocked_get.assert_called_with("http://san99tiago_tech.com/Santiago.Garcia/Sep")
            self.assertEqual(emp_1_schedule, "Success")

            # Test a NOT OK response
            mocked_get.return_value.ok = False
            emp_2_schedule = self.emp_2.get_monthly_schedule("Jan")
            mocked_get.assert_called_with("http://san99tiago_tech.com/Monica.Hill/Jan")
            self.assertEqual(emp_2_schedule, "ERROR: Bad Response in URL")


if __name__ == "__main__":
    unittest.main()
