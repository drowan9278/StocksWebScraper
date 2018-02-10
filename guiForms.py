from tkinter import *
class Startup:
    def __init__(self , master):
        print("Starting startup form")
        self.master = master
        master.title("A simple GUI")
        self.label = Label(master, text="Welcome To StockReviews")
        self.label.pack()

        self.greet_button = Button(master,text="Welcome", command=self.greet)
        self.greet_button.pack()
        choices =[

            "Microsft",
            "AMD",
            "Nvidia"
        ]
        tkvar = StringVar(root)
        tkvar.set(choices[0])
        self.dropDown = OptionMenu(master,tkvar,*choices)
        self.dropDown.pack()




        self.close_button = Button(master, text="Exit", command = master.quit)
        self.close_button.pack()
    def greet(self):
        print("Welcome!")

root = Tk()
my_gui = Startup(root )
root.mainloop()


