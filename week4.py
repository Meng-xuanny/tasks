import turtle

# NUM_CIRCLE=36
# RADIUS=100
# ANGLE=10
#
# for x in range(NUM_CIRCLE):
#     turtle.circle(RADIUS)
#     turtle.left(ANGLE)


# START_X=-200
# START_Y=0
# NUM_LINES=36
# LINE_LENGTH=400
# ANGLE=170
#
# turtle.hideturtle()
# turtle.penup()
# turtle.goto(START_X,START_Y)
# turtle.pendown()
#
# for x in range(NUM_LINES):
#     turtle.forward(LINE_LENGTH)
#     turtle.left(ANGLE)


number_students = int(input("Enter the number of students: "))
while number_students < 0 :
    print("The number of students can't be negative")

number_tests = int (input("Enter the number of tests: "))
while number_tests < 0 :
    print("The number of tests can't be negative")

for student in range(number_students):
    print(f"Student number {student + 1}")
    print('------')

    total = 0

    for test in range(number_tests):
        score = float(input(f'Enter the score for test {test + 1}: '))

        while score < 0:
            print("The score can't be negative.")

        total += score

    average = total / number_tests
    print(f"The average score for student {student + 1} is {average: .1f} ")
    print()

#1
# x=100
#
# if x > 100:
#     y=20
#     z=40
#
#
# #2
# a=100
#
# if a==100:
#     b=10
#     c=50


#3
# a=2
#
# if a < 10:
#     b=0
# else:
#     b=99
#
# print(b)

#4
# score=60
# A_score=85
# B_score=75
# C_score=65
# D_score=55
#
# if score >= A_score: print('Your grade is A.')
#
# elif score >= B_score: print('Your grade is B.')
#
# elif score >= C_score: print('Your grade is C.')
#
# elif score >= D_score: print('Your grade is D.')
# else:
#     print('Your grade is F.')


#5
# amount1=50
# amount2=10
# if (amount1 > 10) and (amount2 < 100):
#     if (amount1 > amount2):
#         print(amount1)
#     else:
#         print(amount2)


#6
# speed=40
#
# if speed >= 24 and speed <= 56:
#     print('your speed is normal')
# else:
#     print('your speed is abnormal')


#7
# points=3
#
# if points < 9 or points > 51:
#     print('invalid points')
# else:
#     print('valid points')

