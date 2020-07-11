#Learned from cihan sönmez https://www.youtube.com/watch?v=B1U0gUhUeQs

import tkinter as tk
from math import*

# used to switch between units of rad, and deg
convert_constant = 1
inverse_convert_constant = 1
def fsin(arg):
    return sin(arg * convert_constant)
def fcos(arg):
    return cos(arg * convert_constant)
def ftan(arg):
    return tan(arg * convert_constant)
def arcsin(arg):
    return (inverse_convert_constant * (asin(arg)))
def arccos(arg):
    return (inverse_convert_constant * (acos(arg)))
def arctan(arg):
    return (inverse_convert_constant * (atan(arg)))

class Calculator:
    def __init__(self, master):
        # expression that will be displayed on screen
        self.expression = ""
        # be used to store data in memory
        self.recall = ""
        # self.answer
        self.sum_up = ""
        # create string for text input
        self.text_Input = tk.StringVar()
        # assign instance to master
        self.master = master
        # set frame showing inputs and title
        top_frame = tk.Frame(master, width=420, height=0, bd=4, relief='raised', bg='#000000')
        top_frame.pack(side=tk.TOP)
        # set frame showing all buttons==========================================================
        bottom_frame = tk.Frame(master, width=420, height=425, bd=4, relief='raised', bg='#2C3A47')
        bottom_frame.pack(side=tk.BOTTOM)
        # entry interface for inputs
        txtDisplay = tk.Entry(top_frame, font=('arial', 36), relief='flat', fg='#000000', bg='#ffffff', textvariable=self.text_Input, width=60, bd=4, justify='right')
        txtDisplay.pack()
        # row 0
        # changes trig function outputs to degrees
        self.btn_Deg = tk.Button(bottom_frame, padx=10, pady=1, bd=8, fg='white', bg='grey', font=('arial', 18),width=2, height=1, relief='raised', text="Deg", activebackground="#000000", foreground='white',activeforeground='orange', command=self.convert_deg)
        self.btn_Deg.grid(row=0, column=0)
        # changes trig function outputs to default back to radians
        self.btn_Rad = tk.Button(bottom_frame, padx=10, pady=1, bd=8, fg='white', bg='grey', font=('arial', 18),width=2, height=1, relief='raised', text="Rad", activebackground="#000000", foreground='orange', activeforeground='orange', command=self.convert_rad)
        self.btn_Rad.grid(row=0, column=1)
        # 'memory clear' button. Wipes self.recall to an empty string
        self.btn_MC = tk.Button(bottom_frame, padx=10, pady=1, bd=8, fg='white', bg='grey', font=('arial', 18),width=2, height=1,text="MC", relief='raised', activebackground="#000000",command=self.memory_clear)
        self.btn_MC.grid(row=0, column=2)
        # adds current self.expression to self.recall string
        self.btn_M_plus = tk.Button(bottom_frame, padx=10, pady=1, bd=8, fg='white', bg='grey', font=('arial', 18),width=2, height=1,text="M+", relief='raised', activebackground="#000000",command=self.memory_add)
        self.btn_M_plus.grid(row=0, column=3)
        # outputs what is in self.recall
        self.btn_MR = tk.Button(bottom_frame, padx=10, pady=1, bd=8, fg='white', bg='grey', font=('arial', 18),width=2, height=1,text="MR", relief='raised', activebackground="#000000",command=self.memory_recall)
        self.btn_MR.grid(row=0, column=4)   
        # row 1
        # square root
        self.btn_sqrt = tk.Button(bottom_frame, padx=10, pady=1, bd=8, fg='white', bg='grey', font=('arial', 18),width=2, height=1, relief='raised', text="√", activebackground="#000000",command=lambda: self.btnClick('sqrt('))
        self.btn_sqrt.grid(row=1, column=0)
        # square function
        self.btn_sqr = tk.Button(bottom_frame, padx=10, pady=1, bd=8, fg='white', bg='grey', font=('arial', 18),width=2, height=1,text=u"x\u00B2", relief='raised', activebackground="#000000",command=lambda: self.btnClick('**2'))
        self.btn_sqr.grid(row=1, column=1)
        # to the power of function
        self.btn_power = tk.Button(bottom_frame, padx=10, pady=1, bd=8, fg='white', bg='grey', font=('arial', 18),width=2, height=1,text="xʸ", relief='raised', activebackground="#000000",command=lambda: self.btnClick('**'))
        self.btn_power.grid(row=1, column=2)
        # log function
        self.btn_log = tk.Button(bottom_frame, padx=10, pady=1, bd=8, fg='white', bg='grey', font=('arial', 18),width=2, height=1,text="log", relief='raised', activebackground="#000000",command=lambda: self.btnClick('log('))
        self.btn_log.grid(row=1, column=3)
        # takes the natural log
        self.btn_ln = tk.Button(bottom_frame, padx=10, pady=1, bd=8, fg='white', bg='grey', font=('arial', 18),width=2, height=1,text="ln", relief='raised', activebackground="#000000",command=lambda: self.btnClick('log1p('))
        self.btn_ln.grid(row=1, column=4)
        # row 2
        # takes e to some exponent that you insert into the function
        self.btn_exp = tk.Button(bottom_frame, padx=10, pady=1, bd=8, fg='white', bg='grey', font=('arial', 18),width=2, height=1, relief='raised', text="EXP", activebackground="#000000",command=lambda: self.btnClick('exp('))
        self.btn_exp.grid(row=2, column=0)
        # takes the absolute value of an expression
        self.btn_abs = tk.Button(bottom_frame, padx=10, pady=1, bd=8, fg='white', bg='grey', font=('arial', 18),width=2, height=1, relief='raised', text="Abs", activebackground="#000000",command=lambda: self.btnClick('abs' + '('))
        self.btn_abs.grid(row=2, column=1)
        # sin function that returns value from -1 to 1 by default
        self.btn_sin = tk.Button(bottom_frame, padx=10, pady=1, bd=8, fg='white', bg='grey', font=('arial', 18),width=2, height=1,text="sin", relief='raised', activebackground="#000000",command=lambda: self.btnClick('fsin('))
        self.btn_sin.grid(row=2, column=2)
        # cos function that returns value from -1 to 1 by default
        self.btn_cos = tk.Button(bottom_frame, padx=10, pady=1, bd=8, fg='white', bg='grey', font=('arial', 18),width=2, height=1,text="cos", relief='raised', activebackground="#000000",command=lambda: self.btnClick('fcos('))
        self.btn_cos.grid(row=2, column=3)
        # tan function
        self.btn_tan = tk.Button(bottom_frame, padx=10, pady=1, bd=8, fg='white', bg='grey', font=('arial', 18),width=2, height=1, relief='raised', activebackground="#000000", text="tan",command=lambda: self.btnClick('ftan('))
        self.btn_tan.grid(row=2, column=4)
        # row 3
        # factorial function
        self.btn_fact = tk.Button(bottom_frame, padx=10, pady=1, bd=8, fg='white', bg='grey', font=('arial', 18),width=2, height=1,text="n!", relief='raised', activebackground="#000000",command=lambda: self.btnClick('factorial('))
        self.btn_fact.grid(row=3, column=0)
        # constant pi
        self.btn_pi = tk.Button(bottom_frame, padx=10, pady=1, bd=8, fg='white', bg='grey', font=('arial', 18),width=2, height=1, relief='raised', text="π", activebackground="#000000",command=lambda: self.btnClick('pi'))
        self.btn_pi.grid(row=3, column=1)
        # sin inverse function
        self.btn_sin_inverse = tk.Button(bottom_frame, padx=13, pady=7, bd=8, fg='white', bg='grey',font=('arial', 15), width=2, height=1,text="sin⁻¹", relief='raised', activebackground="#000000",command=lambda: self.btnClick('arcsin('))
        self.btn_sin_inverse.grid(row=3, column=2)
        # cos inverse function
        self.btn_cos_inverse = tk.Button(bottom_frame, padx=13, pady=7, bd=8, fg='white', bg='grey',font=('arial', 15), width=2, height=1,text="cos⁻¹", relief='raised', activebackground="#000000",command=lambda: self.btnClick('arccos('))
        self.btn_cos_inverse.grid(row=3, column=3)
        # tan inverse function
        self.btn_tan_inverse = tk.Button(bottom_frame, padx=13, pady=7, bd=8, fg='white', bg='grey',font=('arial', 15), width=2, height=1,text="tan⁻¹", relief='raised', activebackground="#000000",command=lambda: self.btnClick('arctan('))
        self.btn_tan_inverse.grid(row=3, column=4)
        # row 4
        # left bracket button
        self.btn_left_brack = tk.Button(bottom_frame, padx=10, pady=1, bd=8, fg='white', bg='#000000',font=('arial', 18), width=2, height=1, relief='raised', text="(", activebackground="#000000",command=lambda: self.btnClick('('))
        self.btn_left_brack.grid(row=4, column=0)
        # right bracket button
        self.btn_right_brack = tk.Button(bottom_frame, padx=10, pady=1, bd=8, fg='white', bg='#000000',font=('arial', 18),width=2, height=1, relief='raised', text=")", activebackground="#000000",command=lambda: self.btnClick(')'))
        self.btn_right_brack.grid(row=4, column=1)
        # comma to allow for more than one parameter!
        self.btn_comma = tk.Button(bottom_frame, padx=10, pady=1, bd=8, fg='white', bg='#000000', font=('arial', 18),width=2, height=1,text=",", relief='raised', activebackground="#000000",command=lambda: self.btnClick(','))
        self.btn_comma.grid(row=4, column=2)
        # clears self.expression
        self.btn_clear = tk.Button(bottom_frame, padx=10, pady=1, bd=8, fg='white', bg='#000000', font=('arial', 18),width=2, height=1, relief='raised', text="CLR", activebackground="#000000",command=self.btnClearAll)
        self.btn_clear.grid(row=4, column=3)
        # deletes last string input
        self.btn_del = tk.Button(bottom_frame, padx=10, pady=1, bd=8, fg='white', bg='#000000', font=('arial', 18),width=2, height=1, relief='raised', text="DEL", activebackground="#000000",command=self.btnClear1)
        self.btn_del.grid(row=4, column=4)
        # row 5
        # seven
        self.btn_7 = tk.Button(bottom_frame, padx=10, pady=1, bd=8, fg='white', bg='#2C3A47', font=('arial', 18),width=2, height=1,text="7", relief='raised', activebackground="#4d4d4d", command=lambda: self.btnClick(7))
        self.btn_7.grid(row=5, column=0)
        # eight
        self.btn_8 = tk.Button(bottom_frame, padx=10, pady=1, bd=8, fg='white', bg='#2C3A47', font=('arial', 18),width=2, height=1,text="8", relief='raised', activebackground="#4d4d4d", command=lambda: self.btnClick(8))
        self.btn_8.grid(row=5, column=1)
        # nine
        self.btn_9 = tk.Button(bottom_frame, padx=10, pady=1, bd=8, fg='white', bg='#2C3A47', font=('arial', 18),width=2, height=1,text="9", relief='raised', activebackground="#4d4d4d", command=lambda: self.btnClick(9))
        self.btn_9.grid(row=5, column=2)
        # inputs a negative sign to the next entry
        self.btn_change_sign = tk.Button(bottom_frame, padx=10, pady=1, bd=8, fg='white', bg='#000000',font=('arial', 18), width=2, height=1, relief='raised', text="+/-", activebackground="#000000", command=self.change_signs)
        self.btn_change_sign.grid(row=5, column=3)
        # cubed
        self.btn_cubed = tk.Button(bottom_frame, padx=10, pady=1, bd=8, fg='white', bg='#000000', font=('arial', 18),width=2, height=1, relief='raised', text="x³", activebackground="#000000", command=lambda: self.btnClick('**3'))
        self.btn_cubed.grid(row=5, column=4)
        # row 6
        # four
        self.btn4 = tk.Button(bottom_frame, padx=10, pady=1, bd=8, fg='white', bg='#2C3A47', font=('arial', 18),width=2, height=1,text="4", relief='raised', activebackground="#4d4d4d", command=lambda: self.btnClick(4))
        self.btn4.grid(row=6, column=0)
        # five
        self.btn5 = tk.Button(bottom_frame, padx=10, pady=1, bd=8, fg='white', bg='#2C3A47', font=('arial', 18),width=2, height=1,text="5", relief='raised', activebackground="#4d4d4d", command=lambda: self.btnClick(5))
        self.btn5.grid(row=6, column=1)
        # six
        self.btn6 = tk.Button(bottom_frame, padx=10, pady=1, bd=8, fg='white', bg='#2C3A47', font=('arial', 18),width=2, height=1,text="6", relief='raised', activebackground="#4d4d4d", command=lambda: self.btnClick(6))
        self.btn6.grid(row=6, column=2)
        # multiplication
        self.btn_mult = tk.Button(bottom_frame, padx=10, pady=1, bd=8, fg='white', bg='#000000', font=('arial', 18),width=2, height=1, relief='raised', text="×", activebackground="#000000",command=lambda: self.btnClick('*'))
        self.btn_mult.grid(row=6, column=3)
        # division
        self.btn_div = tk.Button(bottom_frame, padx=10, pady=1, bd=8, fg='white', bg='#000000', font=('arial', 18),width=2, height=1, relief='raised', text="÷", activebackground="#000000",command=lambda: self.btnClick('/'))
        self.btn_div.grid(row=6, column=4)
        # row 7
        # one
        self.btn1 = tk.Button(bottom_frame, padx=10, pady=1, bd=8, fg='white', bg='#2C3A47', font=('arial', 18),width=2, height=1,text="1", relief='raised', activebackground="#4d4d4d", command=lambda: self.btnClick(1))
        self.btn1.grid(row=7, column=0)
        # two
        self.btn2 = tk.Button(bottom_frame, padx=10, pady=1, bd=8, fg='white', bg='#2C3A47', font=('arial', 18),width=2, height=1,text="2", relief='raised', activebackground="#4d4d4d", command=lambda: self.btnClick(2))
        self.btn2.grid(row=7, column=1)
        # three
        self.btn3 = tk.Button(bottom_frame, padx=10, pady=1, bd=8, fg='white', bg='#2C3A47', font=('arial', 18),width=2, height=1,text="3", relief='raised', activebackground="#4d4d4d", command=lambda: self.btnClick(3))
        self.btn3.grid(row=7, column=2)
        # addition
        self.btn_add = tk.Button(bottom_frame, padx=10, pady=1, bd=8, fg='white', bg='#000000', font=('arial', 18),width=2, height=1,text="+", relief='raised', activebackground="#000000",command=lambda: self.btnClick('+'))
        self.btn_add.grid(row=7, column=3)
        # subtraction
        self.btnSub = tk.Button(bottom_frame, padx=10, pady=1, bd=8, fg='white', bg='#000000', font=('arial', 18),width=2, height=1,text="-", relief='raised', activebackground="#4d4d4d", command=lambda: self.btnClick('-'))
        self.btnSub.grid(row=7, column=4)
        # row 8
        # zero
        self.btn_0 = tk.Button(bottom_frame, padx=10, pady=1, bd=8, fg='white', bg='#2C3A47', font=('arial', 18),width=6, height=1,text="0", relief='raised', activebackground="#4d4d4d", command=lambda: self.btnClick(0))
        self.btn_0.grid(row=8, column=0, columnspan=2)
        # decimal to convert to float
        self.btn_dec = tk.Button(bottom_frame, padx=10, pady=1, bd=8, fg='white', bg='#2C3A47', font=('arial', 18),width=2, height=1,text=".", relief='raised', activebackground="#000000",command=lambda: self.btnClick('.'))
        self.btn_dec.grid(row=8, column=2)
        # stores previous expression as an answer value
        self.btn_ans = tk.Button(bottom_frame, padx=10, pady=1, bd=8, fg='white', bg='#000000', font=('arial', 18),width=2, height=1,text="Ans", relief='raised', activebackground="#000000", command=self.answer)
        self.btn_ans.grid(row=8, column=3)
        # equals button
        self.btn_eq = tk.Button(bottom_frame, padx=10, pady=1, bd=8, fg='white', bg='#FA7D0F', font=('arial', 18),width=2, height=1,text="=", relief='raised', activebackground="#000000", command=self.btnEqual)
        self.btn_eq.grid(row=8, column=4)

    # functions
    # allows button you click to be put into self.expression
    def btnClick(self, expression_val):
        self.expression = self.expression + str(expression_val)
        self.text_Input.set(self.expression)
    # clears last item in string
    def btnClear1(self):
        self.expression = self.expression[:-1]
        self.text_Input.set(self.expression)
    # adds in a negative sign
    def change_signs(self):
        self.expression = self.expression + '-'
        self.text_Input.set(self.expression)
    # clears memory_recall
    def memory_clear(self):
        self.recall = ""
    # adds whatever is on the screen to self.recall
    def memory_add(self):
        self.recall = self.recall + '+' + self.expression
    # uses whatever is stored in memory_recall
    def answer(self):
        self.answer = self.sum_up
        self.expression = self.expression + self.answer
        self.text_Input.set(self.expression)
    # uses whatever is stored in memory_recall
    def memory_recall(self):
        if self.expression == "":
            self.text_Input.set('0' + self.expression + self.recall)
        else:
            self.text_Input.set(self.expression + self.recall)
    # changes self.convert_constant to a string that allows degree conversion when button is clicked
    def convert_deg(self):
        global convert_constant
        global inverse_convert_constant
        convert_constant = pi / 180
        inverse_convert_constant = 180 / pi
        self.btn_Rad["foreground"] = 'black'
        self.btn_Deg["foreground"] = 'orange'
    def convert_rad(self):
        global convert_constant
        global inverse_convert_constant
        convert_constant = 1
        inverse_convert_constant = 1
        self.btn_Rad["foreground"] = 'orange'
        self.btn_Deg["foreground"] = 'black'
    # clears self.expression
    def btnClearAll(self):
        self.expression = ""
        self.text_Input.set("")
    # converts self.expression into a mathematical expression and evaluates it
    def btnEqual(self):
        self.sum_up = str(eval(self.expression))
        self.text_Input.set(self.sum_up)
        self.expression = ""

# tkinter layout
root = tk.Tk()
b = Calculator(root)
root.title("Scientific Calculator")
root.geometry("390x750+0+0")
root.resizable(False, False)
root.mainloop()
