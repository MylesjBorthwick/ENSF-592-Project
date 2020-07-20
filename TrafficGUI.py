from tkinter import Tk, Label, Button, ttk
import folium
import tkinter as tk
from pymongo import MongoClient

#https://python-textbok.readthedocs.io/en/1.0/Introduction_to_GUI_Programming.html 

class MyFirstGUI:
    def __init__(self, master):
        
        self.master = master
        master.title("TrafficApp")

        self.label = Label(master, text="Type")
        self.label.pack()

        Type = tk.StringVar()
        Year = tk.StringVar()
        self.typeCombox = ttk.Combobox(master, width=12, textvariable=Type)
        
        self.typeCombox['values']=("Traffic Volume", "Traffic Incidents")
        self.typeCombox.pack()

        self.label2 = Label(master, text="Year")
        self.label2.pack()

        self.yearCombox = ttk.Combobox(master, width=12, textvariable=Year)
        self.yearCombox['values']=("2018", "2017", "2016")
        self.yearCombox.pack()

        self.greet_button = Button(master, text="Read", command=self.read)
        self.greet_button.pack()

        self.close_button = Button(master, text="Sort")
        self.close_button.pack()

        self.greet_button = Button(master, text="Analysis")
        self.greet_button.pack()

        self.close_button = Button(master, text="Map")
        self.close_button.pack()

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()

    def greet(self):
        print("Greetings!")

    #Reads corresponding collection based on combox selections
    def read(self):
        myclient = MongoClient("mongodb+srv://MylesBorthwick:8557mjb@trafficdatacluster.inrlg.mongodb.net/test?authSource=admin&replicaSet=atlas-86pvzi-shard-0&readPreference=primary&appname=MongoDB%20Compass%20Community&ssl=true")
        trafficdb = myclient["TrafficData"]

        
        if(self.typeCombox.get() == "Traffic Volume"):
            if(self.yearCombox.get() == "2018"):
                flow2018 = trafficdb["TrafficFlow2018"]
            elif(self.yearCombox.get() == "2017"):
                flow2017= trafficdb["TrafficFlow2017"]
            elif(self.yearCombox.get() == "2016"):
                flow2016= trafficdb["TrafficFlow2016"]

        elif (self.typeCombox.get() == "Traffic Incidents"):
            if(self.yearCombox.get() == "2018"):
                incidents2018 = trafficdb["TrafficIncidents2018"]
            elif(self.yearCombox.get() == "2017"):
                incidents2017 = trafficdb["TrafficIncidents2017"]
            elif(self.yearCombox.get() == "2016"):
                incidents2016 = trafficdb["TrafficIncidents2016"]
        
        
        


root =Tk()
my_gui = MyFirstGUI(root)
root.mainloop()