from tkinter import Tk, Label, Button, ttk, LEFT, RIGHT, Frame, WORD
import folium
import tkinter as tk
from pymongo import MongoClient
import tkinter.scrolledtext as tkst
from pandastable import Table
import pandas as pd
import locale

#https://python-textbok.readthedocs.io/en/1.0/Introduction_to_GUI_Programming.html 

class MyFirstGUI:
    def __init__(self, master):
        
        self.master = master
        master.title("TrafficApp")

        leftframe = Frame(master)
        leftframe.pack(side = LEFT)

        self.rightframe = Frame(master)
        self.rightframe.pack(side = RIGHT)

        #tree = ttk.Treeview(rightframe,)
        #self.textbox = tkst.ScrolledText( height=10, width = 40)
        #self.textbox.config
        #self.textbox.config(wrap=WORD)
        #self.textbox.pack(expand = 1, fill = 'both')
        self.textbox = tk.Text(self.rightframe,width=40,height=10,wrap="none")
        self.textvsb = tk.Scrollbar(self.rightframe, orient="vertical", command=self.textbox.yview)
        self.texthsb = tk.Scrollbar(self.rightframe, orient="horizontal", command=self.textbox.xview)
        self.textbox.configure(yscrollcommand=self.textvsb.set, xscrollcommand=self.texthsb.set)
        self.textbox.grid(row=0, column=0, sticky="nsew")
        self.textvsb.grid(row=0, column=1, sticky="ns")
        self.texthsb.grid(row=1, column=0, sticky="ew")

        self.rightframe.grid_rowconfigure(0, weight=1)
        self.rightframe.grid_columnconfigure(0, weight=1)
        self.rightframe.pack(side="top", fill="both", expand=True)
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


    #Reads corresponding collection based on combox selections
    def read(self):
        pd.set_option('display.max_rows',None,'display.max_columns',10)
        pd.options.display.width=None
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
                incidentdata2018 = [data for data in incidents2018.find({},{"_id": 0, "year":0,"id":0,"Longitude":0,"Latitude":0})]
                incidenttable2018 = pd.DataFrame(incidentdata2018)
                self.textbox.delete("1.0","end")
                self.textbox.insert(tk.END,str(incidenttable2018))
                self.textbox.insert(tk.END, '\n')
            elif(self.yearCombox.get() == "2017"):
                incidents2017 = trafficdb["TrafficIncidents2017"]
                incidentdata2017 = [data for data in incidents2017.find({},{"_id": 0, "year":0})]
                incidenttable2017 = pd.DataFrame(incidentdata2017)
                self.textbox.delete("1.0","end")
                self.textbox.insert(tk.END,str(incidenttable2017))
                self.textbox.insert(tk.END, '\n')
            elif(self.yearCombox.get() == "2016"):
                incidents2016 = trafficdb["TrafficIncidents2016"]
                incidentdata2016 = [data for data in incidents2016.find({},{"_id": 0, "year":0})]
                incidenttable2016 = pd.DataFrame(incidentdata2016)
                self.textbox.delete("1.0","end")
                self.textbox.insert(tk.END,str(incidenttable2016))
                self.textbox.insert(tk.END, '\n')

    
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