"""

Eric Meyer - 1/21/2023
Learning the math module in this python file. 

Use built-in functions and 
functions from the math module.

To illustrate the ability to call functions and 
display useful results to the user. 

Use your textbook and the examples in this repo to get ideas.

"""

import math

# define some functions

def get_area_of_lot(length, width):  # get_area_of_lot function takes 2 arguments (length and width)
    """
    Return area of a lot given the length and width of the lot.

    Could this fail?

    """

    # Use a try / except / finally block when something 
    # could go wrong
    try: 
        area = length * width # fix this -- lenth and width (arguments for defined function) were not used in the area equation
        return area
    except Exception as ex:
        print(f"Error: {ex}")
        return None


# define more functions here (see instuctions)

## Prorated employee PTO calculator function (custom function 1):

def prorated_pto_balance(annual_accrual, start_month):
    """
    Calculate an employee's prorated PTO balance for the year based off what month they start during the
    course the calendar year.

    Argument considerations:
        - How many PTO hours do employees receive annaully based off years of experience? (1-2 years of experience = 80 hours pto, 3-5 years of experience = 120 hours pto, etc.)
        - Start month is straight forward (1-3 = january through march, 4-6 = april through june, 7-9 = july through september, and 10-12 = october through december)

    """

    if start_month <= 3:
            start_month == float(1)
    elif start_month >= 4 and start_month <= 6:
            start_month = float(0.75)
    elif start_month >= 7 and start_month <= 9:
            start_month = float(0.5)
    elif start_month >= 10 and start_month <= 12:
            start_month = float(0.25)
    
    try:
        prorated_pto = start_month * annual_accrual
        return prorated_pto
    except Exception as ex:
        print(f"Error: {ex}")
        return None
    
## Employee time off totaling calculator (custom function 2):

def total_employee_time_off_work(hours_off1, hours_off2, hours_off3, hours_off4):
    """
    Simply adding up an employee's hours over the course of a year in order to calculate
    the employee's total hours off work.

    hours_off should be a floating number!

    """

    time_off_list = [hours_off1, hours_off2, hours_off3, hours_off4]

    try:
        total_time_off = math.fsum(time_off_list) # used math module's fsum function
        return total_time_off
    except Exception as ex:
        print(f"Error: {ex}")
        return None
    
## Employee weekend pay payroll calculator (custom function 3):

def weekend_prem_payroll(base_payroll, weekend_nights_out):
    """
    Adding premium pay to an employee's payroll. Simply adding $150 per weekend night out
    with this payroll function.

    """

    weekend_premium = weekend_nights_out * 150   # $150 for each weekend night out for work

    try:
        total_payroll = base_payroll + weekend_premium
        return total_payroll
    except Exception as ex:
        print(f"Error: {ex}")
        return None

# -------------------------------------------------------------
# Call some functions and execute code!

# This is very standard Python - it means
# "If this module is the one being executed, i.e., the main module"
# (as opposed to being imported by another module)
# Literally: "if this module name == the name of the main module"
if __name__ == "__main__":

    # call your functions here (see instructions)
    print('Exploring the math module by defining functions!')
    print()
    print(f"math.comb(10,1) = {math.comb(10,1)}") # testing various number combos in order to grasp the combination and permuatation math functions
    print(f"math.perm(10,1) = {math.perm(10,1)}")
    print()
    print(f"math.comb(10,2) = {math.comb(10,2)}")
    print(f"math.perm(10,2) = {math.perm(10,2)}")
    print()
    print(f"get_area_of_lot(30,15) = {get_area_of_lot(30,15)}")
    print(f"get_area_of_lot(30,0) = {get_area_of_lot(30,0)}")
    print(f"get_area_of_lot(0,15) = {get_area_of_lot(0,15)}")
    print(f"get_area_of_lot(6,2) = {get_area_of_lot(6,2)}")
    print()
    print(f"prorated_pto_balance(80,5) = {prorated_pto_balance(80,5)}")
    print(f"prorated_pto_balance(80,1) = {prorated_pto_balance(80,1)}")
    print(f"prorated_pto_balance(80,8) = {prorated_pto_balance(80,8)}")
    print(f"prorated_pto_balance(80,11) = {prorated_pto_balance(80,11)}")
    print()
    print(f"total_employee_time_off_work(32,8,40,4.5) = {total_employee_time_off_work(32,8,40,4.5)}")
    print(f"total_employee_time_off_work(1,2,3,4) = {total_employee_time_off_work(1,2,3,4)}")
    print(f"total_employee_time_off_work(80,8,8,16) = {total_employee_time_off_work(80,8,8,16)}")
    print()
    print(f"weekend_prem_payroll(2200,3) = {weekend_prem_payroll(2200,3)}")
    print(f"weekend_prem_payroll(4000,1) = {weekend_prem_payroll(4000,1)}")
    print(f"weekend_prem_payroll(3200,0) = {weekend_prem_payroll(3000,0)}")