#1
# myfile = open('numbers.txt','w')
# myfile.write('22\n')
# myfile.write('14\n')
# myfile.write('-99\n')
#
# myfile.close()



#2
# def file_displayer():
#     file_name=input('Enter the file name: ')
#     file = open(file_name, 'r')
#     line_count = 0
#     line=file.readline()
#     while line != '' and line_count <5:
#         line=line.rstrip('\n')
#         print(line)
#         line = file.readline()
#         line_count+=1
#
#     file.close()
#
# file_displayer()

#3
# def number_reader_calculator(filepath):
#
#         total = 0.0
#         count = 0
#         try:
#             file = open(filepath,'r+')
#             for line in file:
#                 number = float(line)
#                 total += number
#                 count += 1
#             average = total / count
#             print(f'The total is {total}, and average is {average}')
#         except ValueError:
#             print(f'cannot convert {line} to integer')
#         except IOError:
#             print('there is an error reading the file, check the file path')
#         except:
#             print('An error occured.')
#
# number_reader_calculator('numbers.txt')

# def number_reader_2(filepath):
#     total=0.0
#     average=0.0
#     try:
#         file=open(filepath,'r')
#         numbers_str= file.read().strip()
#         numbers_str_list = numbers_str.split('\n')
#         count = len(numbers_str_list)
#
#         for number_str in numbers_str_list:
#             number = int(number_str)
#             total += number
#         average=total/count
#         print(f'The total is {total}, and average is {average}')
#     except ValueError:
#         print(f'cannot convert {number_str} to integer')
#     except IOError:
#         print('there is an error opening the file, check the file path')
#     except:
#         print('An error occured.')
#
# number_reader_2('numbers.txt')

#exercise
def file_write():
    print("===Sales Report===")
    file=open('sales.txt','w')
    num_staff = int(input('enter the number of staff: '))
    for staff in range(num_staff):
        sale_per_staff = input(f'enter the sales amount done by staff {staff + 1}: ')
        file.write(sale_per_staff + '\n')
    file.close()

def file_read(filepath):
    file=open(filepath,'r')
    total = 0

    for line in file:
        sale = float(line)
        total += sale
        print(f'sales: {sale}')
    print(f'total sales: {total}')
    file.close()

file_write()
file_read('sales.txt')


import tkinter
from tkinter import messagebox
from tkinter import simpledialog
from tkinter import filedialog

class SalesTracker:
    def __init__(self):
        self.window=tkinter.Tk()
        self.window.title('Daily Sales Tracker')

        self.top_frame = tkinter.Frame()
        self.bottom_frame = tkinter.Frame()
        self.top_frame.pack()
        self.bottom_frame.pack()

        self.sales_label = tkinter.Label(self.top_frame, text='Enter number of Sales staff in the report: ')
        self.sales_entry = tkinter.Entry(self.top_frame,width=10)
        self.sales_label.pack(side='left')
        self.sales_entry.pack(side='left')

        self.write_button = tkinter.Button(self.bottom_frame, text='Create Sales Report',command=self.sales_write)
        self.read_button = tkinter.Button(self.bottom_frame,text='Display Sales Report', command=self.sales_read)
        self.quit_button = tkinter.Button(self.bottom_frame,text='Quit', command=self.window.destroy)
        self.write_button.pack()
        self.read_button.pack(side='left')
        self.quit_button.pack(side='left')

        tkinter.mainloop()

    def sales_write(self):
        num_staff = int(self.sales_entry.get())
        file = open('sales.txt','w')
        messagebox.showinfo("showinfo", "'Enter the sales done by each sales team member.'")
        for n in range(1, num_staff + 1):
            sales = simpledialog.askstring(title=f'Team member {n} sales amount', prompt='enter sales amount: ')
            file.write(sales + '\n')

        file.close()

    def sales_read(self):
        result = ''
        try:
            file = open('sales.txt','r')
            total = 0.0
            count = 0
            for line in file:
                sales = float(line)
                count += 1
                result +=  "\nTeam Member #"+ str(count)+ ":" +str(sales)+" dollars"
                total += sales
            result += "\nTotal sales for the Team: "+str(total)+" dollars"
            file.close()
            messagebox.showinfo('showinfo',result)
        except IOError:
            messagebox.showinfo('error','could not open file')

salesTracker = SalesTracker()
