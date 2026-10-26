# Rent Calculator

A Tkinter desktop app that adds monthly rent, utilities, and internet, then splits the total evenly among the number of people sharing.

## Run
```bash
python rent_calculator.py
```
Python 3 is required. Tkinter is usually included with Python.

## Features
- Calculates the total monthly shared cost.
- Calculates each person's equal share.
- Validates numbers and rejects negative expenses or zero people.
- Currency is shown in Indian rupees (₹).

## Calculation
Total = rent + utilities + internet  
Each person's share = total / number of people
