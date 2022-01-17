leap_year = False
input_year = int(input())
if input_year % 4 == 0 and input_year % 100 == 0:
    leap_year = False
if (input_year % 4 == 0 and input_year % 100 != 0) or input_year % 400 == 0:
    leap_year = True
print(int(leap_year))