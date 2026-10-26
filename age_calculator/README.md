# Age Calculator

A beginner-friendly Python desktop application that calculates a person's exact age in years, months, and days from their date of birth.

## Features

- Calculates age using the computer's current date.
- Handles different month lengths and leap years.
- Rejects invalid dates and dates in the future.
- Simple Tkinter graphical interface.
- Clear button and Enter-key support.

## Requirements

- Python 3.10 or newer recommended.
- Tkinter (usually included with standard Python installations).

No third-party packages are required.

## Run the project

1. Install Python from https://www.python.org/downloads/ if it is not already installed.
2. Download or clone this repository.
3. Open a terminal in the project folder.
4. Run:

   ```bash
   python age_calculator.py
   ```

5. Enter your date of birth in `YYYY-MM-DD` format, such as `2005-08-17`.
6. Select **Calculate Age**.

## How it works

1. The program reads the date of birth from the input field.
2. Python's `date.fromisoformat()` validates the date.
3. `date.today()` fetches the current local date.
4. The program subtracts the birth year, month, and day from today's values.
5. If the day difference is negative, it borrows the number of days in the previous month. If the month difference is negative, it borrows 12 months.
6. The result is displayed in years, months, and days.

## Validation

- Incorrect date formats and impossible dates are rejected.
- A future date of birth is rejected.
- The calculation uses actual calendar month lengths, including February in leap years.

## Example

If today's date is `2026-10-26` and the date of birth is `2005-08-17`, the result is:

`21 years, 2 months, and 9 days`

The displayed result changes automatically based on the current date.

## Files

- `age_calculator.py` — complete application.
- `README.md` — project documentation.
