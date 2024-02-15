import tkinter


'''
# week1 exercise1
print("===Welcome Program===")
print("Welcome to python")
print("Welcome to computer science")
print("Programming is fun", end="\n\n\n")


class Exercise1:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.title("exercise 1")

        self.label1 = tkinter.Label(self.main_window, text="===Welcome Program===")
        self.label2 = tkinter.Label(self.main_window, text="Welcome to python")
        self.label3 = tkinter.Label(self.main_window, text="Welcome to computer science")
        self.label4 = tkinter.Label(self.main_window, text="Programming is fun")

        self.label1.pack()
        self.label2.pack()
        self.label3.pack()
        self.label4.pack()

        tkinter.mainloop()


if __name__ == '__main__':
    exercise1 = Exercise1()

'''



# exercise2
# print((9.5 * 4.5 - 2.5 * 3) / (45.5 - 3.5))
# print()
# print()
#
#
#
# class Exercise2:
#     def __init__(self):
#         self.main_window = tkinter.Tk()
#         self.main_window.title("exercise 2")
#
#         result=round((9.5 * 4.5 - 2.5 * 3) / (45.5 - 3.5))
#
#         self.label1 = tkinter.Label(self.main_window, text=f"The result of (9.5 * 4.5 - 2.5 * 3) / (45.5 - 3.5) is: {result}")
#
#         self.label1.pack()
#
#
#         tkinter.mainloop()
#
#
# if __name__ == '__main__':
#     exercise2 = Exercise2()



# erercise3
# a = 3
# b = 4
# c = 5
# result = b * b - 4 * a * c
# print(f"the discriminate for this equation is {result}\n\n")



class Exercise3:

    def get_result(self,string_variable):
        a = int(self.entry_a.get())
        b = int(self.entry_b.get())
        c = int(self.entry_c.get())
        result = b * b - 4 * a * c
        string_variable.set(result)
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.title("exercise 3")
        self.button_frame=tkinter.Frame(self.main_window)
        self.button_frame.pack(side='bottom')

        self.label1 = tkinter.Label(self.main_window, pady=50, text="Please enter the values for a, b and c")
        self.label_x_square = tkinter.Label(self.main_window, text='X^2 + ')
        self.label_plus = tkinter.Label(self.main_window, text='+')
        self.label_x = tkinter.Label(self.main_window, text='X')
        self.label_equal = tkinter.Label(self.main_window,text='= 0')
        self.label4=tkinter.Label(self.button_frame,text='The X of this equation is: ')
        string_variable = tkinter.StringVar(self.main_window)
        self.label5 = tkinter.Label(self.button_frame, textvariable=string_variable)
        self.button=tkinter.Button(self.button_frame,text='Compute',command=lambda: self.get_result(string_variable))

        self.entry_a = tkinter.Entry(self.main_window)
        self.entry_b = tkinter.Entry(self.main_window)
        self.entry_c = tkinter.Entry(self.main_window)


        self.label1.pack(side='top')
        self.entry_a.pack(side='left')
        self.label_x_square.pack(side='left')
        self.entry_b.pack(side='left')
        self.label_x.pack(side='left')
        self.label_plus.pack(side='left')
        self.entry_c.pack(side='left')
        self.label_equal.pack(side='left')
        self.button.pack(pady=50)
        self.label4.pack()
        self.label5.pack(side='bottom')


        tkinter.mainloop()


if __name__ == '__main__':
    exercise3 = Exercise3()



#exercise4
# v0 = 5.6
# v1 = 10.5
# t = 0.5
# a = (v1 - v0) / t
# print(f"the average velocity is {a}")




# class Exercise4:
#     def on_change(self,string_variable):
#         v0 = float(self.entry1.get())
#         v1 = float(self.entry2.get())
#         t = float(self.entry3.get())
#         a = (v1 - v0) / t
#         string_variable.set(a)
#     def __init__(self):
#         self.window=tkinter.Tk()
#         self.window.title('exercise 4')
#         self.bottom_frame=tkinter.Frame(self.window)
#         self.bottom_frame.pack(side='bottom')
#
#         self.label1=tkinter.Label(self.window,text="Please input the values for calculation:")
#         self.label1.pack(side='top')
#
#         self.label2=tkinter.Label(self.window,text='v0(starting velocity m/s): ', pady=10)
#         self.label2.pack(side='left')
#         self.entry1=tkinter.Entry(self.window,width=15)
#         self.entry1.pack(side='left')
#
#         self.label3 = tkinter.Label(self.window, text='v1(ending velocity m/s): ', pady=10)
#         self.label3.pack(side='left')
#         self.entry2 = tkinter.Entry(self.window, width=15)
#         self.entry2.pack(side='left')
#
#         self.label4 = tkinter.Label(self.window, text='t(time in seconds): ', pady=10)
#         self.label4.pack(side='left')
#         self.entry3=tkinter.Entry(self.window,width=15)
#         self.entry3.pack(side='left')
#
#
#         string_variable = tkinter.StringVar()
#
#         self.label_result=tkinter.Label(self.bottom_frame,textvariable=string_variable)
#         self.label_result.pack(side='bottom')
#
#         self.button=tkinter.Button(self.bottom_frame,text='Calculate',command=lambda :self.on_change(string_variable))
#         self.button.pack()
#
#
#
#         tkinter.mainloop()
#
#
# if __name__ == "__main__":
#     exercise4=Exercise4()
