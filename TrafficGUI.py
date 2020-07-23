from tkinter import Tk, Label, Button, ttk, LEFT, RIGHT, Frame, WORD
import folium
import tkinter as tk
from pymongo import MongoClient
import tkinter.scrolledtext as tkst
#from pandastable import Table
import pandas as pd
import locale
import Map as mappy
import DataAnalysis as dataA


#https://python-textbok.readthedocs.io/en/1.0/Introduction_to_GUI_Programming.html 

class TrafficGUI:
    def __init__(self, master):
        
        self.master = master
        master.title("TrafficApp")

        leftframe = Frame(master)
        leftframe.pack(side = LEFT)

        self.rightframe = Frame(master)
        self.rightframe.pack(side = RIGHT)


        self.textbox = tk.Text(self.rightframe,width=100,height=30,wrap="none")
        self.textvsb = tk.Scrollbar(self.rightframe, orient="vertical", command=self.textbox.yview)
        self.texthsb = tk.Scrollbar(self.rightframe, orient="horizontal", command=self.textbox.xview)
        self.textbox.configure(yscrollcommand=self.textvsb.set, xscrollcommand=self.texthsb.set)
        self.textbox.grid(row=0, column=0, sticky="nsew")
        self.textvsb.grid(row=0, column=1, sticky="ns")
        self.texthsb.grid(row=1, column=0, sticky="ew")
        self.rightframe.grid_rowconfigure(0, weight=1)
        self.rightframe.grid_columnconfigure(0, weight=1)
        self.rightframe.pack(side="top", fill="both", expand=True)


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

        self.read_button = Button(leftframe, text="Read", command=self.read)
        self.read_button.pack()

        self.sort_button = Button(leftframe, text="Sort", command=self.sort)
        self.sort_button.pack()

        self.analysis_button = Button(leftframe, text="Analysis",command = self.getMax)
        self.analysis_button.pack()

        self.map_button = Button(leftframe, text="Map", command = self.generate_map)
        self.map_button.pack()

        self.statustitle = Label(leftframe,text="Read Status")
        self.statustitle.pack()
        self.msg_box = tk.Text(leftframe,width=10,height=5,wrap="none")
        self.msg_box.pack()
 

    def generate_map(self):
        my_map = mappy.Map()
    
        myclient = MongoClient("mongodb+srv://MylesBorthwick:8557mjb@trafficdatacluster.inrlg.mongodb.net/test?authSource=admin&replicaSet=atlas-86pvzi-shard-0&readPreference=primary&appname=MongoDB%20Compass%20Community&ssl=true")
        trafficdb = myclient["TrafficData"] #all the databases are in here. 

        if(self.typeCombox.get() == "Traffic Volume"):
            if(self.yearCombox.get() == "2018"):
                flow = trafficdb["TrafficFlow2018"]
            elif(self.yearCombox.get() == "2017"):
                flow = trafficdb["TrafficFlow2017"]
            elif(self.yearCombox.get() == "2016"):
                flow = trafficdb["TrafficFlow2016"]
            for data in flow.find({},{"_id": 0, "year":0}):
                my_map.add_line_coordinates(data['multilinestring'],'section: '+ data['SECNAME'] +' volume: '+str(data['volume']),data['volume'])
       
        elif(self.typeCombox.get() == "Traffic Incidents"):
            if(self.yearCombox.get() == "2018"): 
                incidents = trafficdb["TrafficIncidents2018"] #grabbing a data collection
   
            elif(self.yearCombox.get() == "2017"):
                incidents = trafficdb["TrafficIncidents2017"] #grabbing a data collection
 
            elif(self.yearCombox.get() == "2016"):
                incidents = trafficdb["TrafficIncidents2016"] #grabbing a data collection

            for data in incidents.find({},{'Count':0,'location':0, 'QUADRANT':0,'MODIFIED_DT':0, "_id": 0, "year":0,"id":0,'START_DT':0}):
                my_map.add_marker(data['Latitude'],data['Longitude'],data['INCIDENT INFO']+': '+data['DESCRIPTION'])
            
        my_map.save_map()

 
    #Reads corresponding collection based on combox selections
    def read(self):
        pd.set_option('display.max_rows',None,'display.max_columns',10)
        pd.options.display.width=None
        myclient = MongoClient("mongodb+srv://MylesBorthwick:8557mjb@trafficdatacluster.inrlg.mongodb.net/test?authSource=admin&replicaSet=atlas-86pvzi-shard-0&readPreference=primary&appname=MongoDB%20Compass%20Community&ssl=true")
        trafficdb = myclient["TrafficData"] #all the databases are in here. 
        
        #handle volume selection
        if(self.typeCombox.get() == "Traffic Volume"):
            if(self.yearCombox.get() == "2018"):
                flow2018 = trafficdb["TrafficFlow2018"] #grabbing a data collection
                flowdata2018 = [data for data in flow2018.find({},{"_id": 0, "year":0,"multilinestring":0})] #pull data from collection
                flowtable2018 = pd.DataFrame(flowdata2018) #formats collection 
                self.textbox.delete("1.0","end")
                self.textbox.insert(tk.END,str(flowtable2018))
                self.textbox.insert(tk.END, '\n')
                self.textbox.configure(state = 'disabled')
                self.msg_box.delete("1.0","end")
                self.msg_box.insert(tk.END, "Read"+"\n"+"Succesful")
            elif(self.yearCombox.get() == "2017"):
                self.textbox.configure(state = 'normal')
                self.textbox.delete("1.0","end")
                flow2017= trafficdb["TrafficFlow2017"]
                flowdata2017 = [data for data in flow2017.find({},{"_id": 0, "year":0,"multilinestring":0})]
                flowtable2017 = pd.DataFrame(flowdata2017)
                self.textbox.insert(tk.END,str(flowtable2017))
                self.textbox.insert(tk.END, '\n')
                self.textbox.configure(state = 'disabled')
                self.msg_box.delete("1.0","end")
                self.msg_box.insert(tk.END, "Read"+"\n"+"Succesful")
            elif(self.yearCombox.get() == "2016"):
                self.textbox.configure(state = 'normal')
                self.textbox.delete("1.0","end")
                flow2016= trafficdb["TrafficFlow2016"]
                flowdata2016 = [data for data in flow2016.find({},{"_id": 0, "year":0,"multilinestring":0})]
                flowtable2016 = pd.DataFrame(flowdata2016)
                self.textbox.insert(tk.END,str(flowtable2016))
                self.textbox.insert(tk.END, '\n')
                self.textbox.configure(state = 'disabled')
                self.msg_box.delete("1.0","end")
                self.msg_box.insert(tk.END, "Read"+"\n"+"Succesful")
                
        #Handle Incident selection        
        elif (self.typeCombox.get() == "Traffic Incidents"):
            if(self.yearCombox.get() == "2018"):
                incidents2018 = trafficdb["TrafficIncidents2018"]
                incidentdata2018 = [data for data in incidents2018.find({},{"_id": 0, "year":0,"id":0,"Longitude":0,"Latitude":0})]
                incidenttable2018 = pd.DataFrame(incidentdata2018)
                self.textbox.configure(state = 'normal')
                self.textbox.delete("1.0","end")
                self.textbox.insert(tk.END,str(incidenttable2018))
                self.textbox.insert(tk.END, '\n')
                self.textbox.configure(state = 'disabled')
                self.msg_box.delete("1.0","end")
                self.msg_box.insert(tk.END, "Read"+"\n"+"Succesful")
            elif(self.yearCombox.get() == "2017"):
                incidents2017 = trafficdb["TrafficIncidents2017"]
                incidentdata2017 = [data for data in incidents2017.find({},{"_id": 0, "year":0})]
                incidenttable2017 = pd.DataFrame(incidentdata2017)
                self.textbox.configure(state = 'normal')
                self.textbox.delete("1.0","end")
                self.textbox.insert(tk.END,str(incidenttable2017))
                self.textbox.insert(tk.END, '\n')
                self.textbox.configure(state = 'disabled')
                self.msg_box.delete("1.0","end")
                self.msg_box.insert(tk.END, "Read"+"\n"+"Succesful")
            elif(self.yearCombox.get() == "2016"):
                incidents2016 = trafficdb["TrafficIncidents2016"]
                incidentdata2016 = [data for data in incidents2016.find({},{"_id": 0, "year":0})]
                incidenttable2016 = pd.DataFrame(incidentdata2016)
                self.textbox.configure(state = 'normal')
                self.textbox.delete("1.0","end")
                self.textbox.insert(tk.END,str(incidenttable2016))
                self.textbox.insert(tk.END, '\n')
                self.textbox.configure(state = 'disabled')
                self.msg_box.delete("1.0","end")
                self.msg_box.insert(tk.END, "Read"+"\n"+"Succesful")

    #Sorts selected dataset and appends the sorted list to textbox
    def sort(self):
        pd.set_option('display.max_rows',None)
        pd.set_option('display.max_colwidth',90)
        myclient = MongoClient("mongodb+srv://MylesBorthwick:8557mjb@trafficdatacluster.inrlg.mongodb.net/test?authSource=admin&replicaSet=atlas-86pvzi-shard-0&readPreference=primary&appname=MongoDB%20Compass%20Community&ssl=true")
        trafficdb = myclient.TrafficData
        #Handle volume selection based on year in combox
        if(self.typeCombox.get() == "Traffic Volume"):
            if(self.yearCombox.get() == "2018"):
                flow2018 = trafficdb["TrafficFlow2018"]
                flowdata2018 = [data for data in flow2018.find({},{"_id": 0, "year":0,"multilinestring":0}).sort("volume",-1)]
                flowtable2018 = pd.DataFrame(flowdata2018)
                self.textbox.configure(state = 'normal')
                self.textbox.delete("1.0","end")
                self.textbox.insert(tk.END,str(flowtable2018))
                self.textbox.insert(tk.END, '\n')
                self.textbox.configure(state = 'disabled')
                self.msg_box.delete("1.0","end")
                self.msg_box.insert(tk.END, "Sort"+"\n"+"Succesful")
            elif(self.yearCombox.get() == "2017"):
                self.textbox.configure(state = 'normal')
                self.textbox.delete("1.0","end")
                flow2017= trafficdb["TrafficFlow2017"]
                flowdata2017 = [data for data in flow2017.find({},{"_id": 0, "year":0,"multilinestring":0}).sort("volume",-1)]
                flowtable2017 = pd.DataFrame(flowdata2017)
                self.textbox.insert(tk.END,str(flowtable2017))
                self.textbox.insert(tk.END, '\n')
                self.textbox.configure(state = 'disabled')
                self.msg_box.delete("1.0","end")
                self.msg_box.insert(tk.END, "Sort"+"\n"+"Succesful")
                
            elif(self.yearCombox.get() == "2016"):
                self.textbox.configure(state = 'normal')
                self.textbox.delete("1.0","end")
                flow2016= trafficdb["TrafficFlow2016"]
                flowdata2016 = [data for data in flow2016.find({},{"_id": 0, "year":0,"multilinestring":0}).sort("volume",-1)]
                flowtable2016 = pd.DataFrame(flowdata2016)
                self.textbox.insert(tk.END,str(flowtable2016))
                self.textbox.insert(tk.END, '\n')
                self.textbox.configure(state = 'disabled')
                self.msg_box.delete("1.0","end")
                self.msg_box.insert(tk.END, "Sort"+"\n"+"Succesful")
        #Handle Incident selection        
        elif (self.typeCombox.get() == "Traffic Incidents"):
            if(self.yearCombox.get() == "2018"):
                incidents = trafficdb["TrafficIncidents2018"]
                incidents = list(incidents.aggregate([
                    {"$group" : { "_id": "$INCIDENT INFO", "count": { "$sum": 1 } } }, 
                    {"$sort": {"count" : -1} },
                ]))
                incidents = [data for data in incidents]
                incidents = pd.DataFrame(incidents)
                self.textbox.configure(state = 'normal')
                self.textbox.delete("1.0","end")
                self.textbox.insert(tk.END,str(incidents))
                self.textbox.insert(tk.END, '\n')
                self.textbox.configure(state = 'disabled')
                self.msg_box.delete("1.0","end")
                self.msg_box.insert(tk.END, "Sort"+"\n"+"Succesful")
                
            elif(self.yearCombox.get() == "2017"):
                incidents = trafficdb["TrafficIncidents2017"]
                incidents = list(incidents.aggregate([
                    {"$group" : { "_id": "$INCIDENT INFO", "count": { "$sum": 1 } } }, 
                    {"$sort": {"count" : -1} },
                ]))
                incidents = [data for data in incidents]
                incidents = pd.DataFrame(incidents)
                self.textbox.configure(state = 'normal')
                self.textbox.delete("1.0","end")
                self.textbox.insert(tk.END,str(incidents))
                self.textbox.insert(tk.END, '\n')
                self.textbox.configure(state = 'disabled')
                self.msg_box.delete("1.0","end")
                self.msg_box.insert(tk.END, "Sort"+"\n"+"Succesful")
            elif(self.yearCombox.get() == "2016"):
                incidents = trafficdb.TrafficIncidents2016
                incidents = list(incidents.aggregate([
                    {"$group" : { "_id": "$INCIDENT INFO", "count": { "$sum": 1 } } }, 
                    {"$sort": {"count" : -1} },
                ]))
                incidents = [data for data in incidents]
                incidents = pd.DataFrame(incidents)
                self.textbox.configure(state = 'normal')
                self.textbox.delete("1.0","end")
                self.textbox.insert(tk.END,str(incidents))
                self.textbox.insert(tk.END, '\n')
                self.textbox.configure(state = 'disabled')
                self.msg_box.delete("1.0","end")
                self.msg_box.insert(tk.END, "Sort"+"\n"+"Succesful")
    
    #Returns max value for dataset based on combox selections
    def getMax(self):
        myclient = MongoClient("mongodb+srv://MylesBorthwick:8557mjb@trafficdatacluster.inrlg.mongodb.net/test?authSource=admin&replicaSet=atlas-86pvzi-shard-0&readPreference=primary&appname=MongoDB%20Compass%20Community&ssl=true")
        trafficdb = myclient.TrafficData
        #Handle volume selection based on year
        if(self.typeCombox.get() == "Traffic Volume"):
            if(self.yearCombox.get() == "2018"):
                flow2018 = trafficdb["TrafficFlow2018"]
                maxflow = [data for data in flow2018.find({},{"_id": 0, "year":0,"multilinestring":0}).sort("volume",-1).limit(1)]
                maxflow = [document["volume"] for document in maxflow]
                plotValues = []
                plotValues.insert(0,maxflow[0])
                plotValues.insert(1, 2018)
                return plotValues
                

            elif(self.yearCombox.get() == "2017"):
                flow2017= trafficdb["TrafficFlow2017"]
                maxflow = [data for data in flow2017.find({},{"_id": 0, "year":0,"multilinestring":0}).sort("volume",-1).limit(1)]
                maxflow = [document["volume"] for document in maxflow]
                plotValues = []
                plotValues.insert(0,maxflow[0])
                plotValues.insert(1, 2017)
                return plotValues
                
                
            elif(self.yearCombox.get() == "2016"):
                
                flow2016= trafficdb["TrafficFlow2016"]
                maxflow = [data for data in flow2016.find({},{"_id": 0, "year":0,"multilinestring":0}).sort("volume",-1).limit(1)]
                maxflow = [document["volume"] for document in maxflow]
                plotValues = []
                plotValues.insert(0,maxflow[0])
                plotValues.insert(1, 2016)
                return plotValues
                
        #Handle Incident selection based on year     
        elif (self.typeCombox.get() == "Traffic Incidents"):
            if(self.yearCombox.get() == "2018"):
                incidents = trafficdb["TrafficIncidents2018"]
                incidents = list(incidents.aggregate([
                    {"$group" : { "_id": "$INCIDENT INFO", "count": { "$sum": 1 } } }, 
                    {"$sort": {"count" : -1} },
                ]))
                incidentmax = [data for data in incidents]
                incidentmax = [document["count"] for document in incidentmax]
                plotValues = []
                plotValues.insert(0,incidentmax[0])
                plotValues.insert(1, 2018)
                return plotValues
                
               
                
            elif(self.yearCombox.get() == "2017"):
                incidents = trafficdb["TrafficIncidents2017"]
                incidents = list(incidents.aggregate([
                    {"$group" : { "_id": "$INCIDENT INFO", "count": { "$sum": 1 } } }, 
                    {"$sort": {"count" : -1} },
                ]))
                incidentmax = [data for data in incidents]
                incidentmax = [document["count"] for document in incidentmax]
                plotValues = []
                plotValues.insert(0,incidentmax[0])
                plotValues.insert(1, 2017)
                return plotValues
                
               
                
            elif(self.yearCombox.get() == "2016"):
                incidents = trafficdb.TrafficIncidents2016
                incidents = list(incidents.aggregate([
                    {"$group" : { "_id": "$INCIDENT INFO", "count": { "$sum": 1 } } }, 
                    {"$sort": {"count" : -1} },
                ]))
                incidentmax = [data for data in incidents]
                incidentmax = [document["count"] for document in incidentmax]
                plotValues = []
                plotValues.insert(0,incidentmax[0])
                plotValues.insert(1, 2016)
                return plotValues
               
   #             
   #     
root =Tk()
my_gui = TrafficGUI(root)
root.mainloop()