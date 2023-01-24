"""
Eric Meyer

Created: 1/23/2023

Domain: Human Resources

This program uses classes, methods, and attributes to summarize, calculate, and output employee's:
    - Position details
    - PTO balance
    - Annual bonus
    - In or out of office status
    - Skills

"""

# first, import helpful modules to make our job easier

import datetime
import statistics
import math
from enum import Enum


class Positions(Enum):
    Manager = 1
    Welder = 2
    Salesman = 3
    Data_Analyst = 4


class PyBuddy:
    """ PyBuddy class for creating a study buddy."""

    def __init__(self, name, positions, yrs_service, pto_balance, is_available, skill_list):
        """ Built-in method to create a new instance."""
        self.name = name
        self.positions = positions
        self.yrs_service = yrs_service
        self.pto_balance = pto_balance
        self.is_available = is_available # In or out of the office
        self.skill_list = skill_list # Primary skills
        self.create_date = datetime.datetime.now()

    def __str__(self):
        """Built-in method to return a string describing this instance"""
        s0 = f"I'm {self.name}.\n\n"
        s1 = f"I'm a {self.positions} with {self.yrs_service} years of experience.\n"
        s2 = f"I currently have {self.pto_balance:.2f} hours of PTO.\n"
        em1 = f"My PTO balance is {self.compare_pto()} than average.\n" # Added a PTO comparison output that leverages the created compare_pto method.
        em2 = f"I get an annual bonus of ${self.annual_bonus():.2f}!\n"
        s3 = f"I've been alive for {self.get_age_string()}.\n"
        

        if self.is_available:
            s4 = "I'm in the office and available to help you!\n\n"
        else:
            s4 = "I'm out of the office and unable to help right now.\n\n"

        s5 = "I know:\n"

        s6 = ""
        for skill in self.skill_list:
            s6 = s6 + f"  - {skill}\n"

        s = s0 + s1 + s2 + em1 + em2 + s3 + s4 + s5 + s6 #used "em" to signal variables that I added
        return s

    def get_age_string(self):
        """Return the age as a string."""
        start = self.create_date
        end = datetime.datetime.now()
        duration = end - start
        ageString = str(duration)
        return ageString

    def compare_pto(self): # (1) Created this first method to compare the employees pto attribute to a calculated average.
        """Compare employee pto balance to user input list average."""
        pto_avg = statistics.mean(employee_pto_list) # Used list created by user input. Also used statistics function to calculate mean.

        if self.pto_balance < pto_avg:
            return "lower"
        elif self.pto_balance > pto_avg:
            return "higher"
        elif self.pto_balance == pto_avg:
            return "equal to"
    
    def annual_bonus(self): # (2) Created this second method to calculate an employee's annual bonus.
        """Calculating annual bonus for the employee based off years of
        service and end of year PTO balance (assuming performance is great for all in this scenario ;) )."""
        
        if 0 < self.pto_balance < 40:
            bonus_pto = 1200
        elif 40 < self.pto_balance < 80:
            bonus_pto = 2400
        elif 80 < self.pto_balance < 120:
            bonus_pto = 3600
        elif self.pto_balance > 120:
            bonus_pto = 4800

        service_bonus = ((self.yrs_service / 2) * 500)

        annual_bonus = bonus_pto + service_bonus
        
        return annual_bonus

    def display_welcome(self):
        print()
        print("Welcome, I'm an employee with your company.\n")
        # print using our built-in to string method
        print(self.__str__())




# -------------------------------------------------------------
# Call some functions and execute code!

# if this is the main file being run

# Asking user for five employee PTO balances.
employee_pto_list = []
list_length = 5

for test in range(list_length):
    pto = int(input('Enter employee PTO balance: ')) # Creating list to be used in compare_pto method.
    employee_pto_list.append(pto)

if __name__ == "__main__":
    # Create an instance of a PyBuddy
    Sarah = PyBuddy(
        "Sarah",
        Positions.Data_Analyst,
        2,
        32,
        True,
        ["Git", "GitHub", "Python", "Markdown", "VS Code"],
    )

    # Call the buddy's welcome() method
    Sarah.display_welcome()


    # Create another instance of a PyBuddy
    Charles = PyBuddy(
        "Charles",
        Positions.Welder,
        13,
        132,
        False,
        skill_list=["Welding", "Fabrication", "Assembly", "MS Excel", "NetSuite"],
    )

    Charles.display_welcome()