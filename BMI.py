'''
Blake Neu
BMI_Blake_Neu.py
objective: create BMI Calculator
date: 4/19/2015
'''

from Tkinter import *

class App():
    def __init__(self):
        self.root = Tk()
        self.root.geometry('380x335+500+300')
        self.root.title('BMI Calculator')

        #Intro
        top = Label(self.root, text="Welcome to the BMI Calculator!", font=('Helvetica',12), fg='#191818', padx=10, pady=10).grid(row=0, column=2)

        # labels
        lbl_1 = Label(self.root, text="Feet:", font=('Helvetica',12), fg='#191818', padx=10, pady=10)
        lbl_2 = Label(self.root, text="Inches:", font=('Helvetica',12), fg='#191818', padx=10, pady=10)
        lbl_3 = Label(self.root, text="Weight:", font=('Helvetica',12), fg='#191818', padx=10, pady=10)

        # entry 1 - Feet
        self.var = StringVar()
        self.entr_1 = Entry(self.root, font=('Helvetica',14) , fg='#191818', textvariable=self.var)

        # entry 2 - Inches
        self.var2 = StringVar()
        self.entr_2 = Entry(self.root, font=('Helvetica',14) , fg='#191818', textvariable=self.var2)

        # entry 3 - Weight
        self.var3 = StringVar()
        self.entr_3 = Entry(self.root, font=('Helvetica',14) , fg='#191818', textvariable=self.var3)

        #label grid layotut
        lbl_1.grid(row=1, column=1, sticky=E)
        lbl_2.grid(row=2, column=1, sticky=E)
        lbl_3.grid(row=3, column=1, sticky=E)

        #entry grid layout
        self.entr_1.grid(row=1, column=2)
        self.entr_2.grid(row=2, column=2)
        self.entr_3.grid(row=3, column=2)

        # Calculate Button
        self.La = StringVar()
        Button(self.root, text="Calculate", bg='#383838', fg='white', font=('Helvetica', 13), width=23,pady=5, padx=5, command=self.Calculate).grid(pady=10, row=4, column=2)

        # Tk Loop
        self.root.mainloop()

        # Calculate Function
    def Calculate(self, *all):
        Entry_1 = self.entr_1.get()
        Entry_2 = self.entr_2.get()
        Entry_3 = self.entr_3.get()

        Feet = int(Entry_1)
        Inches = int(Entry_2)
        Height = Feet*12+Inches

        Weight = getdouble(Entry_3)

        Ans = Weight * 703 /  Height**2
        RoundTo = round(Ans, 2)
        self.La.set(RoundTo)

        # Output Labels
        Label(self.root, text="BMI: ", font=('Helvetica',14), fg='#191818').grid(row=5, column=1)
        Label(self.root, text="Status: ", font=('Helvetica',12), fg='#191818').grid(row=6, column=1)
        Label(self.root, text="Range: ", font=('Helvetica',12), fg='#191818').grid(row=7, column=1)
        Label(self.root, textvariable=self.La, font=('Helvetica',14), fg='#191818').grid(row=5, column=2)

        # Conditions for BMI
        if(RoundTo < getdouble(18.65)):
            Label(self.root, text='   You are underweight   ', font=('Helvetica',12)).grid(row=6, column=2)
            Label(self.root, text="                             ", bg='#c9c23e', font=('Helvetica',14)).grid(row=7, column=2)

        elif(RoundTo >= getdouble(18.65) and RoundTo < getdouble(25.11)):
            Label(self.root, text='                You are normal              ', font=('Helvetica',12)).grid(row=6, column=2)
            Label(self.root, text="                             ", bg='#47a83d', font=('Helvetica',14)).grid(row=7, column=2)

        elif(RoundTo >= getdouble(25.11) and RoundTo < getdouble(29.84)):
            Label(self.root, text='       You are overweight (Level 1)       ', font=('Helvetica',12)).grid(row=6, column=2)
            Label(self.root, text="                             ", bg='#d3962e', font=('Helvetica',14)).grid(row=7, column=2)

        elif(RoundTo >= getdouble(29.84) and RoundTo < (30.13)):
            Label(self.root, text='    You are overweight (Level 2)    ', font=('Helvetica',12)).grid(row=6, column=2)
            Label(self.root, text="                             ", bg='#d32929', font=('Helvetica',14)).grid(row=7, column=2)

        elif(RoundTo >= getdouble(30.13)):
            Label(self.root, text='                 You are obese               ', font=('Helvetica',12)).grid(row=6, column=2)
            Label(self.root, text="                             ", bg='#383838', font=('Helvetica',14)).grid(row=7, column=2)

App()
