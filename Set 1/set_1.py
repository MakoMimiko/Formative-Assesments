#!/usr/bin/env python
# coding: utf-8

# In[9]:


'''Programming Set 1

This assignment will familiarize you with Python's basics.
'''

def savings(gross_pay, tax_rate, expenses):
    '''Savings.

    This function calculates the money remaining
        for an employee after taxes and expenses.

    To get the take-home pay of an employee, we will
        follow the following process:
        1. Apply the tax rate to the gross pay of the employee; round down
        2. Subtract the expenses from the after-tax pay of the employee

    Parameters
    ----------
    gross_pay: int
        the gross pay of an employee for a certain time period, expressed in centavos
    tax_rate: float
        the tax rate for a certain time period, expressed as a number between 0 and 1 (e.g., 0.12)
    expenses: int
        the expenses of an employee for a certain time period, expressed in centavos

    Returns
    -------
    int
        the number of centavos remaining from an employee's pay after taxes and expenses
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    tax = float(gross_pay) * tax_rate
    after_tax = round(float(gross_pay) - tax)
    home_pay = after_tax - expenses
    return home_pay

in_1 = int(input("gross pay: "))
in_2 = float(input("tax rate: "))
in_3 = int(input("expenses: "))
savings(in_1, in_2, in_3)


# In[13]:


def material_waste(total_material, material_units, num_jobs, job_consumption):
    '''Material Waste.

    This function calculates how much material input will be wasted
        after running a certain number of jobs that consume
        a set amount of material.

    To get the waste of a set of jobs:
        1. Multiply the number of jobs by the material consumption per job.
        2. Subtract the total material consumed from the total material available.

    The users of this function also want you to format the output as a string, annotated with the
        units in which the material is expressed. Do not add a space between the number and the unit.

    Parameters
    ----------
    total_material: int
        the total material available
    material_units: str
        the units used to express a quantity of the material (e.g., "kg", "L", etc.)
    num_jobs: int
        the number of jobs to run
    job_consumption: int
        the amount of material consumed per job

    Returns
    -------
    str
        the amount of remaining material expressed with its unit (e.g., "10kg").
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    mat_cons_job = num_jobs * job_consumption
    mat_remaining = total_material - mat_cons_job
    return(str(mat_remaining) + material_units)
in_1 = int(input("total material: "))
in_2 = input("material units: ")
in_3 = int(input("number of jobs: "))
in_4 = int(input("job consumption: "))
material_waste(in_1, in_2, in_3, in_4)


# In[ ]:


def interest(principal, rate, periods):
    '''Interest.

    This function calculates the final value of an investment after
        gaining simple interest over a number of periods.

    To calculate simple interest, simply multiply the principal to the quantity (rate * time).
        Add this amount to the principal to get the final value.

    Round down the final amount.

    Parameters
    ----------
    principal: int
        the principal (i.e., starting) amount invested, expressed in centavos
    rate: float
        the interest rate per period, expressed as a decimal representation of a percentage (e.g., 3% is 0.03)
    periods: int
        the number of periods invested

    Returns
    -------
    int
        the final value of the investment
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    interest = principal * (rate * periods)
    investment = round(principal + interest)
    return(investment)
in_1 = int(input("total material: "))
in_2 = float(input("material units: "))
in_3 = int(input("number of jobs: "))
material_waste(in_1, in_2, in_3, in_4)


# In[20]:


pip install --upgrade 'nbconvert>=7' 'mistune>=2'

