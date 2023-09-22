# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 00:12:11 2023

@author: khanb
"""

# Input values
balance = float(input("Enter the outstanding balance on the credit card: "))
annualInterestRate = float(input("Enter the annual interest rate (as a decimal): "))
monthlyPaymentRate = float(input("Enter the minimum monthly payment rate (as a decimal): "))

# Constants
months_per_year = 12

# Initialize variables
total_paid = 0

# Calculate balance for each month in the year
for month in range(months_per_year):
    # Minimum monthly payment
    min_payment = balance * monthlyPaymentRate
    
    # Monthly interest rate
    monthly_interest_rate = annualInterestRate / months_per_year
    
    # Interest paid for the month
    interest_paid = balance * monthly_interest_rate
    
    # Principal paid for the month
    principal_paid = min_payment - interest_paid
    
    # Update the balance for the month
    balance -= principal_paid
    
    # Accumulate total payments
    total_paid += min_payment

# Print the remaining balance at the end of the year
print("Remaining balance: {:.2f}".format(balance))
