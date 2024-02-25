import tkinter
import tkinter.messagebox


class MYGUI:
    def __init__(self):
        self.window = tkinter.Tk()
        self.window.title("Loan Qualifier")

        # frame
        self.top_frame = tkinter.Frame(pady=10)
        self.top_frame.pack()
        self.mid_frame = tkinter.Frame()
        self.mid_frame.pack()
        self.button_frame = tkinter.Frame(pady=20)
        self.button_frame.pack()
        self.text_frame = tkinter.Frame(pady=30)
        self.text_frame.pack(side='bottom')

        # question label and entry
        self.label_salary = tkinter.Label(self.top_frame, text='Your salary: ')
        self.label_salary.pack(side='left')

        self.entry_salary = tkinter.Entry(self.top_frame, bg='light grey', width=10)
        self.entry_salary.pack(side='left')

        self.label_year = tkinter.Label(self.mid_frame, text='Years on job: ')
        self.label_year.pack(side='left')

        self.entry_year = tkinter.Entry(self.mid_frame, bg='light grey', width=10)
        self.entry_year.pack(side='left')

        # button
        self.button_calc = tkinter.Button(self.button_frame, text='Calculate', command=self.calculate_loan)
        self.button_calc.pack(side='left')

        self.button_quit = tkinter.Button(self.button_frame, text='Quit', command=self.window.destroy)
        self.button_quit.pack(side='left')

        # label as output
        self.message = tkinter.StringVar()
        self.text_label = tkinter.Label(self.text_frame, textvariable=self.message)
        self.text_label.pack()

        # text area as output
        self.result_ta = tkinter.Text(self.text_frame, bg='light blue', height=20, width=60)
        self.result_ta.pack()

        tkinter.mainloop()

    def calculate_loan(self):
        result = ''
        MIN_SALARY = 30000
        MIN_YEAR = 2

        self.result_ta.delete('1.0', tkinter.END)

        salary = float(self.entry_salary.get())
        years_on_job = int(self.entry_year.get())

        if salary >= MIN_SALARY:
            if years_on_job >= MIN_YEAR:
                result += 'You are qualified for the loan.'
            else:
                result += f"You must be employed for more than {MIN_YEAR} years."
        else:
            result += f'Your annual salary has to be at least {MIN_SALARY:,.2f}.'

        # tkinter.messagebox.showinfo('loaninfo',result)

        # self.message.set(result)

        self.result_ta.insert('1.0', result)


my_gui = MYGUI()
