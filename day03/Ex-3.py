year = int(input("which year u want to check "))

if year % 4 == 0: 
    if year % 100 == 0:  
        if year % 400 == 0:  
            print("this is a leap year")  # divisible by 400
        else:
            print("this is not a leap year")  # divisible by 100 but not by 400
    else:
        print("this is a leap year")  # divisible by 4 but not by 100
else:
    print("this is not a leap year")  # not divisible by 4
