from tkinter import *
class Startup:
    def __init__(self , master):
        print("Starting startup form")
        self.master = master
        master.title("StockReviewer")
        master.iconbitmap(self,"logo.ico")
        master.geometry('400x330')

        self.label = Label(master, text="Welcome To StockReviews")
        self.label.grid(column =0,row=0,sticky =W)
        self.greet_button = Button(master,text="Update Selection", command=self.greet)
        self.greet_button.grid(row=1,column = 0)

        self.close_button = Button(master, text="Exit", command=master.quit)
        self.close_button.grid(row=8,column=0)
        self.companyOption = Scrollbar(master)
        self.companyList = Listbox(master,yscrollcommand = self.companyOption.set)
        data = self.grabData()
        for i in data:
            self.companyList.insert(END,i)
        self.companyList.grid(row=1,column=1,rowspan= 2,columnspan = 4)
        self.companyOption.config(command=self.companyList.yview())
        self.companyOption.grid(row=2,column=1)
        companycur = StringVar()
        self.companySelect = Label(self.master, text = " No Selection!")
        self.companySelect.grid(row=2, column=0)
        dateoptions = [
            "Q1",
            "Q2",
            "Q3",
            "Q4",
            "Custom Date Range"
        ]
        dateVar = StringVar()
        self.dateSelect = OptionMenu(master,dateVar,*dateoptions,command = self.dateselect)
        self.dateSelect.grid(row=4,column=1)
        self.dateSelectLabel = Label(master,text="Select Date: ")
        self.dateSelectLabel.grid(row=4,column=0)
    def dateselect(self,value):

        if value == "Custom Date Range":
            self.dateRange1 = Entry(self.master)
            self.dateRange2 = Entry(self.master)
            self.dateRange1Label = Label(self.master,text="Start Date: ")
            self.dateRange2Label = Label(self.master,text="End Date: ")
            self.dateRange1Label.grid(row=5,column=0)
            self.dateRange2Label.grid(row=6,column=0)
            self.dateRange1.grid(row=5,column=1)
            self.dateRange2.grid(row=6,column=1)
        else:
            self.dateRange1.grid_forget()
            self.dateRange2.grid_forget()
            self.dateRange2Label.grid_forget()
            self.dateRange1Label.grid_forget()

    def stockgraph(self):
        return
    def greet(self):
        print("Updated")
        self.companySelect.config(text = "Current Selection: " +self.companyList.get('active'))
        self.showStockGraph = Button(self.master, text="Show Current Stock Graph", command =  self.stockgraph())
        self.showStockGraph.grid(row=7,column = 0)
    def grabData(self):
        data = []
        with open("companies.txt") as file:
            data = file.readlines()
        return data
root = Tk()
my_gui = Startup(root )
root.mainloop()


