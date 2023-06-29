import turtle
turtle.bgcolor('pink')
t=turtle.Turtle() #creating an object 
colors=['red','blue']
for number in range(100): #loop is from 0-100
    t.forward(number+1)#number is a variable
    t.right(79)
    t.pencolor(colors[number%2])
turtle.done()#to keep the windows on