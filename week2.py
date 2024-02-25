import tkinter
import turtle


#exercise1
# age=int(input('Please enter your age: '))
# print(f'You are {age} years old.')
# #
# # #exercise2
# color=input("What's your favorite color? ")
# print("It's " + color)
#
# #exercise3
# a=int(input('enter a value'))
# b=a + 2
# a=b * 4
# b=a/3.14
# a=b - 8
# print(a,b)

#exercise4
# w=5
# x=4
# y=8
# z=2
#
# result_a=x+y
# result_b=z*2
# result_c=y/x
# result_d=y-z
# result_e=w//z
#
# #exercise5
# product=10 * 14
# print(product)
#
# #exercise6
# total=100
# down_payment=20
# due=total - down_payment
# print(due)
#
# #exercise7
# subtotal=100
# total=subtotal * 0.15
# print(total)
#
# #exercise8
# a=5
# b=2
# c=3
# result=a+b *c
# print(result)

#exercise9
# num=99
# new_num=num
# num=5
# new_num = num + 5
# print(num)
#
# #exercise10
# sales=1000000000.11111111
# print(f'{sales:.2f}')
#
# #exercise11
# number=1234567.456
# print(f'{number:,.1f}')

#part1
# num1=int(input('Please enter an integer: '))
# num2=int(input('Please enter another integer: '))
# sum=num1 + num2
# print(f'The sum of the digits is {sum}')


#part2
# class My_GUI:
#     def __init__(self):
#         self.window=tkinter.Tk()
#         self.window.title('MY GUI Program')
#
#         self.label=tkinter.Label(text='Programming is fun! I like Python Programming.')
#         self.label.pack()
#
#         tkinter.mainloop()
#
# my_gui=My_GUI()



#part3

#1
#turtle.forward(100)

#2
# turtle.forward(100)
# turtle.left(90)
# turtle.forward(100)
#
# #3
# turtle.forward(100)
# turtle.right(45)
# turtle.forward(100)

#4
# turtle.forward(50)
# turtle.setheading(90)
# turtle.forward(100)
# turtle.setheading(180)
# turtle.forward(50)
# turtle.setheading(270)
# turtle.forward(100)

#5
# turtle.forward(10)
# turtle.penup()
# turtle.forward(5)
# turtle.pendown()
# turtle.forward(10)
# turtle.penup()
# turtle.forward(5)
# turtle.pendown()
# turtle.forward(10)


# #6
# turtle.circle(100)
#
# #8
# turtle.pensize(5)
# turtle.pencolor('red')
# turtle.circle(50)
#

#9
# turtle.goto(0,100)
# turtle.goto(100,0)
# turtle.goto(0,0)

# #10
# turtle.write('Hello World')
#
# #11
# name=turtle.textinput('Input','Enter your name')
# turtle.write('Your name is '+name)
#
# #12
# age=turtle.numinput('Input','Enter your name')
# turtle.write('Your age is '+ str(age))
#
# #13
# turtle.hideturtle()
# turtle.fillcolor('red')
# turtle.begin_fill()
# turtle.circle(100)
# turtle.end_fill()
#
# #14
# turtle.hideturtle()
# turtle.fillcolor('blue')
# turtle.begin_fill()
# turtle.goto(100,0)
# turtle.goto(100,100)
# turtle.goto(0,100)
# turtle.goto(0,0)
# turtle.end_fill()
#
# #15
turtle.hideturtle()
turtle.goto(100,0)
turtle.goto(100,100)
turtle.goto(0,100)
turtle.goto(0,0)
#
# turtle.penup()
# turtle.goto(50,20)
# turtle.fillcolor('red')
# turtle.begin_fill()
# turtle.circle(30)
# turtle.end_fill()
#
turtle.done()
