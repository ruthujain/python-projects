#okay lets practice for my python finals!!!!!:)!
# the first program is to read the name and yer of birth of a person and to display if the person is a senior citizen or not
import datetime as dt
name=input("enter your name\n")
yob=int(input("enter your year of birth\n"))
currentYear=dt.datetime.now().year
age=currentYear-yob
if age>=60:
    print("yes")
else:
    print("no")
    