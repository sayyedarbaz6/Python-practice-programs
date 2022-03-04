#Display Calendar of leap year
import calendar 

list1 = []
stryear=int(input("Enter a Starting year from which you want to  you want to check leap year:"))
endyear=int(input("Enter a Ending year till you want to check leap year:"))
print('Leap Years Are:')

#Checking leap year or Not
for i in range (stryear,endyear+1):
    x = calendar.isleap(i)
    if x == True:
        list1.append(i)
print(list1)

#Displaying leap year calendar
ans=input("Are you want to display calendar from above displayed leap year (Y/N):")
if ans == 'Y':
    yy=int(input("Which leap year calendar you want to display:"))
    for numbers in list1:
        if numbers == int(yy):
           print(calendar.calendar(yy))
    else:
        print('choose year from above list')
