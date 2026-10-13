day = int(input("Enter the day : "))
month =  int(input("Enter the month : "))
year = int(input("Enter the year : "))

is_leap_year = (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0)

if month in (1 , 3 , 5 , 7 , 8 , 10 ,12) :
    days_in_month = 31 
elif month in (4 , 6 , 9 ,11) :
    days_in_month = 30 
elif month == 2 :
    if is_leap_year :
        days_in_month = 29
    else :
        days_in_month = 28 
else :
    days_in_month = 0 


is_valid = year >= 1 and day >= 1 and day <= days_in_month

if is_valid :
    print(f"Valid date is {year:04d}-{month:02d}-{day:02d}")
else :
    print("Invalid data")    
