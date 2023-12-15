print("WELCOME TO THE QUIZ GAME!!!")
print("Type yes if you want to play \n Type no to exit")
a=input("DO YOU WANT TO PLAY THE GAME? ")
if a.lower()=="yes":
    print("Okay,lets begin.")
name=input("Enter your name:")
print("Hi  "+name+"  ,  HERE WE GO!")
score=0
q1=input("Who is the first president of India?")
if q1.lower()=="rajendra prasad":
    print("CORRECT ANSWER!!")
    score+=1
else:
    print("SORRY WRONG ANSWER!!")

q2=input("Who is the first  female president of India?")
if q2.lower()=="prathibha patil":
    print("CORRECT ANSWER!!")
    score+=1
else:
    print("SORRY WRONG ANSWER!!")

q3=input("Who is the present president of India?")
if q3.lower()=="droupadi murmu":
    print("CORRECT ANSWER!!")
    score+=1
else:
    print("SORRY WRONG ANSWER!!")

print("Your score is ",score)

