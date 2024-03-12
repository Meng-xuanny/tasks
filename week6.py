#1
# def show_value(quantity):
#     print(quantity)
#
# show_value(12)
import random

#3
# def main():
#     x = 1
#     y = 3.4
#     print(x, y)
#     change_us(x, y)
#     print(x, y)
#
# def change_us(a, b):
#     a = 0
#     b = 0
#     print(a, b)
#
# main()

#4
# rand = random.randint(1,100)
# print(rand)

#5
# def half(value):
#     return value / 2
# number = 6
# result=half(number)
# print(result)

#6
# def cube(num):
#     return num * num * num
#
# result=cube(4)
# print(result)

#7
# def times_ten(value):
#     return value * 10

#8
# mystring=input('enter a string: ')
# def count_white_space(str):
#     count=0
#     for x in str:
#         if x == ' ':
#            count += 1
#     print(f'The number of white space in the string is {count}')
#
# count_white_space(mystring)
#
# #9
# def count_char(str):
#     count = 0
#     for a in str:
#         if a.isalnum():
#             count+=1
#     print(f'The number of alphanumeric characters in the string is {count}')
#
# count_char(mystring)
#
# #10
# def count_lower(str):
#     count = 0
#     for a in str:
#         if a.islower():
#             count+=1
#     print(f'The number of alphanumeric characters in the string is {count}')
#
# count_lower(mystring)
#
# 11
# def ifAU(str):
#     lower_str=str.lower()
#     if 'au' in lower_str:
#         return True
#     else:
#         return False
#
# print(ifAU('luluart'))

#12
# def reverse_string(str):
#     result=''
#     index=len(str)
#     while index >0:
#         index -= 1
#         result += str[index]
#     print(result)
#
# reverse_string('helloworld')

#13
# def capitalizer(input):
#     result=''
#     str_list = input.split('. ')
#     for str in str_list:
#         capitalized_str = str.capitalize()
#         #print(capitalized_str)
#         result+=capitalized_str + '. '
#     print(result)
#
# input_str = input('enter a string: ')
# capitalizer(input_str)

#14
# def word_seperator(str):
#     result = ''
#     for x in str:
#         if x.islower():
#             result += x
#         else:
#             result += f' {x}'
#     lower_result=result.lower().strip() #this line gets rifd of the white space in the begining and turns it to lower case
#     print(lower_result.capitalize())
#
# word_seperator('StopAndSmellTheRoses.')

#15
# def pig_latin_translator(str):
#     pig_latin = ''
#     words=str.split(' ')
#     for word in words:
#         if len(word) <= 1:
#             pig_latin += word + 'ay '
#         else:
#             first_letter = word[0]
#             pig_latin += word[1:] + first_letter + 'ay '
#
#     print(pig_latin.upper())
#
# pig_latin_translator('The quzk brown fox jumped over the lazy dog')





'''
import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog

class SalesTrackerGUI:
    def __init__(self):

        # Create the main window.
        self.main_window = tkinter.Tk()
        self.main_window.title("Sales Tracker Report")

        # Create two frames to group widgets.
        self.top_frame = tkinter.Frame()
        self.bottom_frame = tkinter.Frame()
        self.result_frame = tkinter.Frame()

        # Create the widgets for the top frame.
        self.prompt_label = tkinter.Label(self.top_frame,
                    text='Enter number of Sales staff in the report:')
        self.Sales_entry = tkinter.Entry(self.top_frame, width=10)

        # Pack the top frame's widgets.
        self.prompt_label.pack(side='left')
        self.Sales_entry.pack(side='left')

        # Create the button widgets for the bottom frame.
        self.Sales_read_button = tkinter.Button(self.bottom_frame,
                                          text='Read Sales Amount',
                                          command=self.Sales_read)
        self.quit_button = tkinter.Button(self.bottom_frame,
                                          text='Quit',
                                          command=self.main_window.destroy)

        # Pack the buttons.
        self.Sales_read_button.pack(side='left')
        self.quit_button.pack(side='left')

        self.result_ta = tkinter.Text(self.result_frame, bg ='light blue', height=20, width=40)
        self.result_ta.pack()

        # Pack the frames.
        self.top_frame.pack()
        self.bottom_frame.pack()
        self.result_frame.pack()

        # Enter the tkinter main loop.
        tkinter.mainloop()

    # The Sales_read method is a callback function for
    # the Calculate button.

    def Sales_read(self):
            self.result_ta.delete('1.0', 'end')
            sum_of_sales = 0
            max_sales = 0
            min_sales = 0
            sum_of_sales =0
            avg_sales = 0
            result_string = ""
            # Get the value entered by the user into the # Sales_entry widget.
            staff_num = int(self.Sales_entry.get())
            while staff_num <= 0:
                messagebox.showinfo('alart','the number of staff must be positive!')
                return
            i = 0
            while i< staff_num:
                    sales_done = (simpledialog.askstring(title = "Sales done by staff # "+str(i+1),
                                                           prompt="Enter Sales amount: "))
                    sales_done = float(sales_done)
                    if i==0:
                            max_sales = sales_done
                            min_sales = sales_done
                    if sales_done > max_sales:
                            max_sales = sales_done
                    if sales_done < min_sales:
                            min_sales = sales_done
                    i+=1
                    sum_of_sales += sales_done

            avg_sales = sum_of_sales / staff_num

            result_string += ("=====Sales Tracker Report=====")
            result_string += ("\nTotal Sales:"+ str(f'{sum_of_sales:.2f}'))
            result_string += ("\nHighest Sales:"+ str(f'{max_sales:.2f}'))
            result_string += ("\nLowest Sales:"+ str(f'{min_sales:.2f}'))
            result_string += ("\nAverage Sales:"+ str(f'{avg_sales:.2f}'))
            self.result_ta.insert('1.0', result_string)

my_Sales_Tracker = SalesTrackerGUI()

'''

import turtle

ANIMATION_SPEED = 0
BASE_X = 0
BASE_Y = -200
BASE_RADIUS = 100
MID_X = 0
MID_Y = 0
MID_RADIUS = 60

RIGHT_ARM_X1 = 60
RIGHT_ARM_Y1 = 60
RIGHT_ARM_X2 = 108
RIGHT_ARM_Y2 = 75
RIGHT_ARM_X3 = 118
RIGHT_ARM_Y3 = 75
RIGHT_ARM_X4 = 118
RIGHT_ARM_Y4 = 85

LEFT_ARM_X1 = -60
LEFT_ARM_Y1 = 60
LEFT_ARM_X2 = -105
LEFT_ARM_Y2 = 70
LEFT_ARM_X3 = -120
LEFT_ARM_Y3 = 110
LEFT_ARM_X4 = -130
LEFT_ARM_Y4 = 115
LEFT_ARM_X5 = -120
LEFT_ARM_Y5 = 125

HEAD_X = 0
HEAD_Y = 120
HEAD_RADIUS = 40

LEFT_EYE_X = -20
LEFT_EYE_Y = 170
RIGHT_EYE_X = 20
RIGHT_EYE_Y = 170
EYE_RADIUS = 5

MOUTH_START_X = -25
MOUTH_START_Y = 140
MOUTH_END_X = 25
MOUTH_END_Y = 140

HAT_X1 = -50
HAT_Y1 = 180
HAT_X2 = 50
HAT_Y2 = 180
HAT_X3 = 50
HAT_Y3 = 205
HAT_X4 = -50
HAT_Y4 = 205
HAT_X5 = -30
HAT_Y5 = 205
HAT_X6 = 30
HAT_Y6 = 205
HAT_X7 = 30
HAT_Y7 = 245
HAT_X8 = -30
HAT_Y8 = 245

def drawBase():
    turtle.penup()
    turtle.goto(BASE_X, BASE_Y)
    turtle.pendown()
    turtle.circle(BASE_RADIUS)

def drawMidSection():
    turtle.penup()
    turtle.goto(MID_X, MID_Y)
    turtle.pendown()
    turtle.circle(MID_RADIUS)

def drawArms():
    # Draw the right arm
    turtle.penup()
    turtle.goto(RIGHT_ARM_X1, RIGHT_ARM_Y1)
    turtle.pendown()
    turtle.goto(RIGHT_ARM_X2, RIGHT_ARM_Y2)
    turtle.goto(RIGHT_ARM_X3, RIGHT_ARM_Y3)
    turtle.penup()
    turtle.goto(RIGHT_ARM_X2, RIGHT_ARM_Y2)
    turtle.pendown()
    turtle.goto(RIGHT_ARM_X4, RIGHT_ARM_Y4)

    # Draw the left arm
    turtle.speed(1)
    turtle.penup()
    turtle.goto(LEFT_ARM_X1, LEFT_ARM_Y1)
    turtle.pendown()
    turtle.goto(LEFT_ARM_X2, LEFT_ARM_Y2)
    turtle.goto(LEFT_ARM_X3, LEFT_ARM_Y3)
    turtle.goto(LEFT_ARM_X4, LEFT_ARM_Y4)
    turtle.penup()
    turtle.goto(LEFT_ARM_X3, LEFT_ARM_Y3)
    turtle.pendown()
    turtle.goto(LEFT_ARM_X5, LEFT_ARM_Y5)

def drawHead():
    # Draw the head
    turtle.penup()
    turtle.goto(HEAD_X, HEAD_Y)
    turtle.pendown()
    turtle.circle(HEAD_RADIUS)

    # Draw the left eye
    turtle.penup()
    turtle.goto(LEFT_EYE_X, LEFT_EYE_Y)
    turtle.pendown()
    turtle.circle(EYE_RADIUS)

    # Draw the right eye
    turtle.penup()
    turtle.goto(RIGHT_EYE_X, RIGHT_EYE_Y)
    turtle.pendown()
    turtle.circle(EYE_RADIUS)

    # Draw the mouth
    turtle.penup()
    turtle.goto(MOUTH_START_X, MOUTH_START_Y)
    turtle.pendown()
    turtle.goto(MOUTH_END_X, MOUTH_END_Y)


def drawHat():
    # Draw the bottom part of the hat
    turtle.penup()
    turtle.goto(HAT_X1, HAT_Y1)
    turtle.fillcolor('black')
    turtle.pendown()
    turtle.begin_fill()
    turtle.goto(HAT_X2, HAT_Y2)
    turtle.goto(HAT_X3, HAT_Y3)
    turtle.goto(HAT_X4, HAT_Y4)
    turtle.end_fill()

    # Draw the top part of the hat
    turtle.penup()
    turtle.goto(HAT_X5, HAT_Y5)
    turtle.pendown()
    turtle.begin_fill()
    turtle.goto(HAT_X6, HAT_Y6)
    turtle.goto(HAT_X7, HAT_Y7)
    turtle.goto(HAT_X8, HAT_Y8)
    turtle.end_fill()


def main():
    turtle.speed(ANIMATION_SPEED)
    turtle.hideturtle()
    drawBase()
    drawMidSection()
    drawArms()
    drawHead()
    drawHat()
    turtle.done()

main()


