# Code to test, switch between 1 and 2 for different results!
code=1

if code==1:
    # Code 1
    year=int(input("Which year you want to  verify?:"))
    if year%4==0 and year%100!=0 or year %400==0:
        print("This year is a leap year!")
    else:
        print("This year isn't a leap year!")
else:
    # Code 2
    cm=int(input("Height in centimeters:"))
    ic=cm*0.394
    ft=cm*0.0328
    print("Height in inches is",ic)
    print("Height in feet is",ft)