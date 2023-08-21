# Age Calculator
## [Video Demo](https://youtu.be/ubS7MI_pYKQ)
### Description:
This program prompts the user for date of birth as an input in `Month Day, Year` format, and prints out the calculated age and days before their birthday. 

#### How the Program Works?
The Program utilizes the python built-in library `Datetime`[^1] and import `date` object. 
To acquire the current local date, `.today()` class method from `date` was used which has `.day`, `.month`, and `.year` instance attributes.

The Program also utilizes the python built-in library `re`[^2] or `regular expression`. This library was used to check the format of the inputted birthdate and extracts the neccesarry data.

To calculate the age, subtract the birthyear from the current year.

The calculations of the age are based on the following factors:
1. If the birthmonth is greater than today's month, this means that the user has not yet celebrated his/her birthday (Example: Birthday is on October[10] and today's month is August[08]). Decrement 1 on age.
2. If the birthmonth and today's month is equal, check if the birthday is greater than today's day. This means that the user has not yet celebrated his/her birhtday (Example: Birthday is on August 25 and today's day is August 17). Decrement 1 on age.

To calculate the days before birthdate, subtract today's date from the birthdate in current year (Example: 2023, 10, 20 - 2023, 08, 19).
1. If the birthday in current year is less than today's date (Example: Birthdate 2023, 02, 11; Today's date 2023, 08, 19) then, increment 1 to the birthyear. This will replace to 2024, 02, 11 - 2023, 08, 19.

### TODO:
#### How to Run the Program?
1. Download the program python script.
2. Go to `cmd` and navigate to the program python script directory.
   - `cd 'directory'` 
4. Run the program python script with `python` keyword first, then `filename.py`.

#### How to Use the Program?
After successfully running the program, it will prompt for some birthdate.
Enter the birthdate following the given format `Month Day, Year`. 
- Example: October 20, 2000 or Oct 20, 2000.
>[!NOTE]
>The program is case-insensitive.

>[!IMPORTANT]
>Do not forget the comma `,` between the `day` and `year` of the birthdate.


## References
[^1]: [Datetime library](https://docs.python.org/3/library/datetime.html)
[^2]: [re library](https://docs.python.org/3/library/re.html)
