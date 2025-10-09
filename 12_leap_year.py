# Leap Year Checker

def is_leap_year(year):
    """
    Check if a year is a leap year
    Leap year rules:
    1. If year is divisible by 400 -> leap year
    2. If year is divisible by 100 but not 400 -> not leap year
    3. If year is divisible by 4 but not 100 -> leap year
    4. Otherwise -> not leap year
    """
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False

def is_leap_year_simple(year):
    """Simplified leap year check"""
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def get_leap_years_in_range(start_year, end_year):
    """Get all leap years in a given range"""
    leap_years = []
    for year in range(start_year, end_year + 1):
        if is_leap_year(year):
            leap_years.append(year)
    return leap_years

def days_in_month(month, year):
    """Get number of days in a month for a given year"""
    days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    if month == 2 and is_leap_year(year):
        return 29
    else:
        return days_in_months[month - 1]

# Input year
year = int(input("Enter a year to check if it's a leap year: "))

if is_leap_year(year):
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")

# Verify with simplified method
if is_leap_year_simple(year):
    print(f"Verified: {year} is a leap year (using simplified method)")
else:
    print(f"Verified: {year} is not a leap year (using simplified method)")

# Show leap years in a range
start = int(input("Enter start year for range: "))
end = int(input("Enter end year for range: "))

leap_years = get_leap_years_in_range(start, end)
print(f"Leap years between {start} and {end}: {leap_years}")

# Show days in February for the input year
feb_days = days_in_month(2, year)
print(f"February {year} has {feb_days} days")