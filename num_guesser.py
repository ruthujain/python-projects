from random import *
ran=randint(0,9)
print(ran)
print("WELCOME TO THE NUMBER GUESSING GAME!!!")
n=int(input("Enter the number of chances you would like to take: "))
for i in range(1,n+1):
    g1=int(input("Guess the number"))
    if (g1==ran):
        print("YOU HAVE GUESSED THE NUMBER CORRECTLY!!")
        break
    else:
        print("OOPS WROGN GUESS")
        continue
print("THANK YOU FOR PLAYING")
