# SAMPLE EMPLOYEE FOR EXPLAINING UNIT-TESTING IN OTHER SCRIPTS
# Santiago Garcia Arango

import requests


class Employee:
    """
    This is a cool simplified Employee class
    """

    def __init__(self, name, lastname, salary, job):
        self.annual_raise = 1.05
        self.name = name
        self.lastname = lastname
        self.salary = salary
        self.job = job

    @property
    def email(self):
        return "{}.{}@gmail.com".format(self.name, self.lastname).lower()

    @property
    def fullname(self):
        return "{} {}".format(self.name, self.lastname)

    def apply_raise_to_salary(self):
        if(self.job == "DevOps" or self.job == "Cloud"):
            self.salary = int(self.salary * (self.annual_raise + 0.03))
        else:
            self.salary = int(self.salary * (self.annual_raise))

    def get_monthly_schedule(self, month):
        response = requests.get(f"http://san99tiago_tech.com/{self.name}.{self.lastname}/{month}")
        if response.ok:
            return response.text
        else:
            return "ERROR: Bad Response in URL"


if __name__ == "__main__":
    santi = Employee("Santiago", "Garcia", 100, "DevOps")
    print("\n-----SHOWING INFO ABOUT OUR GREAT EMPLOYEE SANTI-----")
    print(santi.fullname)
    print(santi.email)
    print(santi.salary)
    print("Applying annual raise...")
    santi.apply_raise_to_salary()
    print(santi.salary)


    moni = Employee("Monica", "Hill", 100, "Finance")
    print("\n-----SHOWING INFO ABOUT OUR GREAT EMPLOYEE MONI-----")
    print(moni.fullname)
    print(moni.email)
    print(moni.salary)
    print("Applying annual raise...")
    moni.apply_raise_to_salary()
    print(moni.salary)
