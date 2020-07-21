from tkinter import Tk, Label, Button, ttk, LEFT, RIGHT, Frame, WORD
import folium
import tkinter as tk
from pymongo import MongoClient
import tkinter.scrolledtext as tkst
from pandastable import Table
import pandas as pd
#https://python-textbok.readthedocs.io/en/1.0/Introduction_to_GUI_Programming.html 

class MyFirstGUI:
    def __init__(self, master):
        
        self.master = master
        master.title("TrafficApp")

        leftframe = Frame(master)
        leftframe.pack(side = LEFT)

        rightframe = Frame(master)
        rightframe.pack(side = RIGHT)

        #tree = ttk.Treeview(rightframe,)
        self.textbox = tkst.ScrolledText( height=10, width = 40)
        self.textbox.config(wrap=WORD)
        self.textbox.pack(expand = 1, fill = 'both')
        #self.table=Table(rightframe)
        #self.table.show()

        self.label = Label(leftframe, text="Type")
        self.label.pack()

        Type = tk.StringVar()
        Year = tk.StringVar()
        self.typeCombox = ttk.Combobox(leftframe, width=14, textvariable=Type)
        
        self.typeCombox['values']=("Traffic Volume", "Traffic Incidents")
        self.typeCombox.pack()

        self.label2 = Label(leftframe, text="Year")
        self.label2.pack()

        self.yearCombox = ttk.Combobox(leftframe, width=14, textvariable=Year)
        self.yearCombox['values']=("2018", "2017", "2016")
        self.yearCombox.pack()

        self.greet_button = Button(leftframe, text="Read", command=self.read)
        self.greet_button.pack()

        self.sort_button = Button(leftframe, text="Sort", command=self.sort)
        self.sort_button.pack()

        self.greet_button = Button(leftframe, text="Analysis")
        self.greet_button.pack()

        self.close_button = Button(leftframe, text="Map")
        self.close_button.pack()

        self.close_button = Button(leftframe, text="Close", command=master.quit)
        self.close_button.pack()

    def greet(self):
        print("Greetings!")

    #Reads corresponding collection based on combox selections
    def read(self):
        pd.set_option('display.max_rows',None)
        myclient = MongoClient("mongodb+srv://MylesBorthwick:8557mjb@trafficdatacluster.inrlg.mongodb.net/test?authSource=admin&replicaSet=atlas-86pvzi-shard-0&readPreference=primary&appname=MongoDB%20Compass%20Community&ssl=true")
        trafficdb = myclient["TrafficData"]
        
        if(self.typeCombox.get() == "Traffic Volume"):
            if(self.yearCombox.get() == "2018"):
                flow2018 = trafficdb["TrafficFlow2018"]
                flowdata2018 = [data for data in flow2018.find({},{"_id": 0, "year":0,"multilinestring":0})]
                flowtable2018 = pd.DataFrame(flowdata2018)
                self.textbox.delete("1.0","end")
                self.textbox.insert(tk.END,str(flowtable2018))
                self.textbox.insert(tk.END, '\n')
            elif(self.yearCombox.get() == "2017"):
                self.textbox.delete("1.0","end")
                flow2017= trafficdb["TrafficFlow2017"]
                flowdata2017 = [data for data in flow2017.find({},{"_id": 0, "year":0,"multilinestring":0})]
                flowtable2017 = pd.DataFrame(flowdata2017)
                self.textbox.insert(tk.END,str(flowtable2017))
                self.textbox.insert(tk.END, '\n')
            elif(self.yearCombox.get() == "2016"):
                self.textbox.delete("1.0","end")
                flow2016= trafficdb["TrafficFlow2016"]
                flowdata2016 = [data for data in flow2016.find({},{"_id": 0, "year":0,"multilinestring":0})]
                flowtable2016 = pd.DataFrame(flowdata2016)
                self.textbox.insert(tk.END,str(flowtable2016))
                self.textbox.insert(tk.END, '\n')
                
                    

        elif (self.typeCombox.get() == "Traffic Incidents"):
            if(self.yearCombox.get() == "2018"):
                incidents2018 = trafficdb["TrafficIncidents2018"]
            elif(self.yearCombox.get() == "2017"):
                incidents2017 = trafficdb["TrafficIncidents2017"]
            elif(self.yearCombox.get() == "2016"):
                incidents2016 = trafficdb["TrafficIncidents2016"]

    
    def sort(self):
        pd.set_option('display.max_rows',None)
        myclient = MongoClient("mongodb+srv://MylesBorthwick:8557mjb@trafficdatacluster.inrlg.mongodb.net/test?authSource=admin&replicaSet=atlas-86pvzi-shard-0&readPreference=primary&appname=MongoDB%20Compass%20Community&ssl=true")
        trafficdb = myclient["TrafficData"]
        
        if(self.typeCombox.get() == "Traffic Volume"):
            if(self.yearCombox.get() == "2018"):
                flow2018 = trafficdb["TrafficFlow2018"]
                flowdata2018 = [data for data in flow2018.find({},{"_id": 0, "year":0,"multilinestring":0}).sort("volume",-1)]
                flowtable2018 = pd.DataFrame(flowdata2018)
                self.textbox.delete("1.0","end")
                self.textbox.insert(tk.END,str(flowtable2018))
                self.textbox.insert(tk.END, '\n')
            elif(self.yearCombox.get() == "2017"):
                self.textbox.delete("1.0","end")
                flow2017= trafficdb["TrafficFlow2017"]
                flowdata2017 = [data for data in flow2017.find({},{"_id": 0, "year":0,"multilinestring":0}).sort("volume",-1)]
                flowtable2017 = pd.DataFrame(flowdata2017)
                self.textbox.insert(tk.END,str(flowtable2017))
                self.textbox.insert(tk.END, '\n')
            elif(self.yearCombox.get() == "2016"):
                self.textbox.delete("1.0","end")
                flow2016= trafficdb["TrafficFlow2016"]
                flowdata2016 = [data for data in flow2016.find({},{"_id": 0, "year":0,"multilinestring":0}).sort("volume",-1)]
                flowtable2016 = pd.DataFrame(flowdata2016)
                self.textbox.insert(tk.END,str(flowtable2016))
                self.textbox.insert(tk.END, '\n')
                
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