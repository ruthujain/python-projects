import random
print("0-stone,1-paper,2-sissor")
user_choice=int(input('enter your choice \n'))
computer_choice=random.randint(0,2)
print('comp choice is= ',computer_choice)
if user_choice>2 or user_choice<0:
    print('invalid input')
elif user_choice==0 and computer_choice==2:
    print('you win!')
elif user_choice==2 and computer_choice==0:
    print('you lose!')
elif user_choice<computer_choice:
    print('you lose!')
elif user_choice>computer_choice:
    print('you win!')
elif user_choice==computer_choice:
    print('its a draw')