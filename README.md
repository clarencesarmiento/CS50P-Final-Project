# Age Calculator
## Video Demo
### Description:
This program prompts the user for date of birth as an input in (Month Day, Year) format, and prints out the calculated age and days before their birthday. 

To calculate the age, subtract the birthyear from the current year.

The calculations of the age are based on the following factors:
> 1. If the birthmonth is greater than today's month, this means that the user has not yet celebrated his/her birthday (Example: Birthday is on October[10] and today's month is August[08]). Decrement 1 on age.
> 2. If the birthmonth and today's month is equal, check if the birthday is greater than today's day. This means that the user has not yet celebrated his/her birhtday (Example: Birthday is on August 25 and today's day is August 17). Decrement 1 on age.

To calculate the days before birthdate, subtract today's date from the birthdate in current year (Example: 2023, 10, 20 - 2023, 08, 19).
> If the birthday in current year is less than today's date (Example: Birthdate 2023, 02, 11; Today's date 2023, 08, 19) then, increment 1 to the birthyear. This will replace to 2024, 02, 11 - 2023, 08, 19.

### TODO:
#### How to Run the Program?
To run the program, go to ~cmd~
