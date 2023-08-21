"""
NAME
    Age Calculator

DESCRIPTION
    This program prompts the user for date of birth as an input in (Month Day, Year) format, and returns
    the calculated age and days before their birthday.

FUNCTIONS
    is_valid(birthdate: str)
        Returns the checked format of birthday.
    month_to_integer(month: str)
        Returns the equivalent integer of the month.
    calculate_age(birthmonth: str, birthday: int, birthyear: int, today)
        Returns the age, and the number of days before birthday.
    calculate_days(birthday: int, birthmonth: str, today)
        Returns the number of days before birthday.
"""

from datetime import date
import re


def main():
    birthmonth, birthday, birthyear = is_valid(input("Enter Birthdate: ").lower())
    today = date.today()
    age = calculate_age(birthmonth, int(birthday), int(birthyear), today)
    days = calculate_days(birthmonth, int(birthday), today)
    print(f"Your age as of {date.today().strftime('%B %d, %Y')} is {age} years old.\n{days} days before your Birthday!")


def is_valid(birthdate: str):
    """
    Checks the format of the user's input.

    Args:
        birthdate (str): the string which format is to be checked.

    Raises:
        ValueError: Invalid Date Format.

    Returns: matches.group(1), matches.group(2), matches.group(3) (tuple): tuple that contains birthmonth,
    birthday and birthyear.
    """
    regex = r"^([a-z]{3,9})\s([0-2]?[0-9]|3[0-1]),\s?([0-9]{4})$"
    if matches := re.search(regex, birthdate, re.IGNORECASE):
        return matches.group(1), matches.group(2), matches.group(3)
    else:
        raise ValueError("Invalid Date Format.")


def month_to_integer(month: str):
    """
    Converts the given month to integer.

    Args:
        month (str): the string to be checked on the dictionaries of months and converted to.

    Raises:
        ValueError: Month not found.

    Returns:
        months["fullname"][month] (int): the integer representing the fullname format of the month.
        months["abbreviated_name"][month] (int): the integer representing the abbreviated format of the month.
    """

    months = {
        "fullname": {
            "january": 1,
            "february": 2,
            "march": 3,
            "april": 4,
            "may": 5,
            "june": 6,
            "july": 7,
            "august": 8,
            "september": 9,
            "october": 10,
            "november": 11,
            "december": 12,
        },
        "abbreviated_name": {
            "jan": 1,
            "feb": 2,
            "mar": 3,
            "apr": 4,
            "may": 5,
            "jun": 6,
            "jul": 7,
            "aug": 8,
            "sept": 9,
            "oct": 10,
            "nov": 11,
            "dec": 12,
        },
    }
    if month in months["fullname"]:
        return months["fullname"][month]
    elif month in months["abbreviated_name"]:
        return months["abbreviated_name"][month]
    else:
        raise ValueError("Month not found.")


def calculate_age(birthmonth: str, birthday: int, birthyear: int, today):
    """
    Calculates the age and days before birthday.

    Args:
        birthmonth (str): the string to be passed on month_to_integer function to be converted to integer.
        birthday (int): the integer which is to be checked to increment 1 to age if birthday had passed on.
        birthyear (int): the integer which is the subtrahend to calculate the age.
        today (datetime.date): function that returns today's date.

    Returns:
        total_age (int): the integer representing age.
    """

    total_age = (today.year - birthyear)
    if month_to_integer(birthmonth) > today.month:
        total_age -= 1
    elif month_to_integer(birthmonth) == today.month:
        if birthday > today.day:
            total_age -= 1

    return total_age


def calculate_days(birthmonth: str, birthday: int, today):
    """
    Calculates the days before birthday.

    Args:
        birthday (int): the integer for birthday.
        birthmonth (str): the string to be converted to integer for the birthmonth.
        today (datetime.date): function that returns today's date.

    Returns:
        time_to_birthday (int): the integer representing the days before birthday.
    """
    year_birthday = date(today.year, month_to_integer(birthmonth), birthday)
    if year_birthday < today:
        year_birthday = year_birthday.replace(year=today.year + 1)
    time_to_birthday = abs(year_birthday - today)

    return time_to_birthday.days


if __name__ == "__main__":
    main()
