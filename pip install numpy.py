import numpy as np
import json

def calculate_repayment_schedule(loan_amount, annual_interest_rate, loan_term_years):
    # Calculate monthly interest rate and total number of payments
    monthly_interest_rate = annual_interest_rate / 100 / 12
    total_payments = loan_term_years * 12
    
    # Calculate monthly payment
    monthly_payment = loan_amount * (monthly_interest_rate / (1 - (1 + monthly_interest_rate) ** (-total_payments)))
    
    # Initialize lists for the repayment schedule
    schedule = []
    
    remaining_balance = loan_amount
    
    for month in range(1, total_payments + 1):
        interest_payment = remaining_balance * monthly_interest_rate
        principal_payment = monthly_payment - interest_payment
        remaining_balance -= principal_payment
        
        # Store payment details in the schedule
        payment_details = {
            "Month": month,
            "Total Payment": monthly_payment,
            "Principal Payment": principal_payment,
            "Interest Payment": interest_payment,
            "Remaining Balance": remaining_balance if remaining_balance > 0 else 0
        }
        schedule.append(payment_details)
        
    return schedule

# Loan details
loan_amount = 100000  # e.g., $100,000
annual_interest_rate = 5  # e.g., 5%
loan_term_years = 30  # e.g., 30 years

# Calculate the repayment schedule
repayment_schedule = calculate_repayment_schedule(loan_amount, annual_interest_rate, loan_term_years)

# Convert the repayment schedule to JSON format
repayment_schedule_json = json.dumps(repayment_schedule, indent=4)

# Print the JSON
print(repayment_schedule_json)
