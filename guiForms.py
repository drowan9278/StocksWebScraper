from tkinter import *
class Startup:
    def __init__(self , master):
        print("Starting startup form")
        self.master = master
        master.title("StockReviewer")
        master.iconbitmap(self,"logo.ico")
        self.label = Label(master, text="Welcome To StockReviews")
        self.label.grid(column =0,row=0,sticky =W)
        self.greet_button = Button(master,text="Update Selection", command=self.greet)
        self.greet_button.grid(row=1,column = 0)

        self.close_button = Button(master, text="Exit", command=master.quit)
        self.close_button.grid(row=4,column=0)
        self.companyOption = Scrollbar(master)
        self.companyList = Listbox(master,yscrollcommand = self.companyOption.set)
        data = self.grabData()
        for i in data:
            self.companyList.insert(END,i)
        self.companyList.grid(row=1,column=1,rowspan= 10,columnspan = 10)
        self.companyOption.config(command=self.companyList.yview())
        self.companyOption.grid(row=2,column=1)
        companycur = StringVar()
        self.companySelect = Label(self.master, text = " No Selection!")
        self.companySelect.grid(row=2, column=0)


    def stockgraph(self):
        return
    def greet(self):
        print("Updated")
        self.companySelect.config(text = "Current Selection: " +self.companyList.get('active'))
        self.showStockGraph = Button(self.master, text="Show Current Stock Graph", command =  self.stockgraph())
        self.showStockGraph.grid(row=3,column = 0)
    def grabData(self):
        data = []
        with open("companies.txt") as file:
            data = file.readlines()
        return data
root = Tk()
my_gui = Startup(root )
root.mainloop()


