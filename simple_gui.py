#! /usr/bin/python3.8

"""
This is simple program written for study pools answer program
written in Tkinter

Change the extension .py install python and run with
>>linux chmod +x simplu_gui.py && ./simple_gui.py
>>windows >> install python and run the file
"""

from tkinter import*

class calculator_window:
    def __init__(self, window):
        self.mainframe=Frame(window, highlightbackground="black", highlightthickness=2)
        self.mainframe.config(bg="black")
        self.mainframe.pack(fill=BOTH)

        """container frames"""
        self.rightframe = Frame(self.mainframe, width=400, height=400, highlightthickness=2)
        self.rightframe.pack(side=RIGHT,fill=BOTH,expand=True)
        self.eo1 = Entry(self.rightframe)
        #self.insert(0, 'value1')
        self.eo1.pack()
        self.eo2 = Entry(self.rightframe)
        #self.insert(0, 'value2')
        self.eo2.pack()
        self.eo3 = Entry(self.rightframe)
        #self.eo3.insert(0, 'value3')
        self.eo3.pack()
        self.eo4 = Entry(self.rightframe)
        #self.eo4.insert(0, 'value4')
        self.eo4.pack()
        """answer frame"""
        self.leftframe = Frame(self.mainframe,width=400,height=400,highlightthickness=2, bg="yellow")
        self.leftframe.pack(side=LEFT,fill=BOTH,expand=True)

        self.label = Label(self.leftframe, text="Sum will appear hear")
        self.label.pack()
        self.label2 = Label(self.leftframe, text="Product will appear hear")
        self.label2.pack()
        self.label3 = Label(self.leftframe, text="Smallest value will appear hear")
        self.label3.pack()
        self.label4 = Label(self.leftframe, text="Largest vallue will appear hear")
        self.label4.pack()
        def calculate():
            v1 = self.eo1.get()
            v2 = self.eo2.get()
            v3 = self.eo3.get()
            v4 = self.eo4.get()
            v5 = int(v1) + int(v2) +int(v3) +int(v4)
            v6 = int(v1) * int(v2) *int(v3) *int(v4)
            #v7 = int(v1) + int(v2) +int(v3) +int(v4)
            
            self.label.config(text= "Sum : " + str(v5))
            self.label2.config(text= "Product: " + str(v6))

            lis = []
            lis.append(int(v1))
            lis.append(int(v2))
            lis.append(int(v3))
            lis.append(int(v4))
            lis.sort()

            self.label3.config(text="Smallest no: " +str(lis[0]))
            self.label4.config(text="Largest no: " +str(lis[3]))
            

            
        self.button =Button(self.mainframe, text="Calculate", command=calculate)
        self.button.pack()
        self.exit =Button(self.mainframe, text="exit")
        self.exit.pack()

       

root = Tk()
root.title("Simple calculator App")
root.minsize(550,200)
d = calculator_window(root)
root.mainloop()
