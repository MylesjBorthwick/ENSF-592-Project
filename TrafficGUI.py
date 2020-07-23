from tkinter import Tk, Label, Button, ttk, LEFT, RIGHT, Frame, WORD
import folium
import tkinter as tk
from pymongo import MongoClient
import pandas as pd
import locale
import Map as mappy
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
#https://python-textbok.readthedocs.io/en/1.0/Introduction_to_GUI_Programming.html 

#Traffic GUI class creates interface and maps commands to GUI elements
class TrafficApp:
    def __init__(self, master):
        
        self.master = master
        master.title("TrafficApp")
        self.matplot_active = False
        #Create window title
        self.master = master
        master.title("TrafficApp")

        #Create left Frame in GUI window
        leftframe = Frame(master)
        leftframe.pack(side = LEFT)

        #Create right Frame in GUI Window
        self.rightframe = Frame(master)
        self.rightframe.pack(side = RIGHT)

        #Create text field used to display read and sort data
        self.textbox = tk.Text(self.rightframe,width=150,height=40,wrap="none")
        #Create scrollbars for text window for data navigation
        self.textvsb = tk.Scrollbar(self.rightframe, orient="vertical", command=self.textbox.yview)
        self.texthsb = tk.Scrollbar(self.rightframe, orient="horizontal", command=self.textbox.xview)
        #Add scrollbars to textbox and pack into rightframe
        self.textbox.configure(yscrollcommand=self.textvsb.set, xscrollcommand=self.texthsb.set)
        self.textbox.grid(row=0, column=0, sticky="nsew")
        self.textvsb.grid(row=0, column=1, sticky="ns")
        self.texthsb.grid(row=1, column=0, sticky="ew")
        self.rightframe.grid_rowconfigure(0, weight=1)
        self.rightframe.grid_columnconfigure(0, weight=1)
        self.rightframe.pack(side="top", fill="both", expand=True)

        #Create combobox header Type
        self.label = Label(leftframe, text="Type")
        self.label.pack()

        Type = tk.StringVar()
        Year = tk.StringVar()
        self.typeCombox = ttk.Combobox(leftframe, width=14, textvariable=Type)

        #Create combobox for type
        self.typeCombox['values']=("Traffic Volume", "Traffic Incidents")
        self.typeCombox.pack()

        #Create combobox header year
        self.label2 = Label(leftframe, text="Year")
        self.label2.pack()
        
        #Create combobox for year
        self.yearCombox = ttk.Combobox(leftframe, width=14, textvariable=Year)
        self.yearCombox['values']=("2018", "2017", "2016")
        self.yearCombox.pack()

        #create button for read functionality
        self.read_button = Button(leftframe, text="Read", command=self.read)
        self.read_button.pack()

        #create button for sort functionality
        self.sort_button = Button(leftframe, text="Sort", command=self.sort)
        self.sort_button.pack()
 
        self.analysis_button = Button(leftframe, text="Analysis", command=self.generate_plot)
        self.analysis_button.pack()

        #Create button for map
        self.map_button = Button(leftframe, text="Map", command = self.generate_map)
        self.map_button.pack()

        #Create status box
        self.statustitle = Label(leftframe,text="Read Status")
        self.statustitle.pack()
        self.msg_box = tk.Text(leftframe,width=10,height=5,wrap="none")
        self.msg_box.pack()

        

    def generate_plot(self):
        self.check_active_plot()
        self.rightframe.pack_forget()
        self.matplot_active = True
        values = self.getMax()
        if(values == [-1,-1,-1]):
            self.matplot_active = False
            self.rightframe.pack()
        else:
            f = plt.figure(figsize=(8,6))

            # linear
            plt.subplot(111)
            plt.plot(['2016','2017','2018'],values)
            plt.yscale('linear')
            
            
            plt.xlabel('Year')
            if(self.typeCombox.get() == "Traffic Incidents"):
                plt.ylabel('Traffic Incidents')
                plt.title('Incident plot')
            else:
                plt.ylabel('Flow Volume')
                plt.title('Flow plot')   
            plt.grid(True)
            
            #a = f.add_subplot(111)
            #a.plot([2016,2017,2018],values)
            self.rightframe.canvas = FigureCanvasTkAgg(f, master=root)  # A tk.DrawingArea.
            self.rightframe.canvas.draw ()
            self.rightframe.canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
            self.rightframe.canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
            self.msg_box.delete("1.0","end")
            self.msg_box.insert(tk.END, "Analysis"+"\n"+"Successful")
        
        



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
            self.msg_box.delete("1.0","end")
            self.msg_box.insert(tk.END, "Mapping"+"\n"+"Successful")
            
        elif(self.typeCombox.get() == "Traffic Incidents"):
            if(self.yearCombox.get() == "2018"): 
                incidents = trafficdb["TrafficIncidents2018"] #grabbing a data collection
   
            elif(self.yearCombox.get() == "2017"):
                incidents = trafficdb["TrafficIncidents2017"] #grabbing a data collection
 
            elif(self.yearCombox.get() == "2016"):
                incidents = trafficdb["TrafficIncidents2016"] #grabbing a data collection

            for data in incidents.find({},{'Count':0,'location':0, 'QUADRANT':0,'MODIFIED_DT':0, "_id": 0, "year":0,"id":0,'START_DT':0}):
                my_map.add_marker(data['Latitude'],data['Longitude'],data['INCIDENT INFO']+': '+data['DESCRIPTION'])
            
            self.msg_box.delete("1.0","end")
            self.msg_box.insert(tk.END, "Mapping"+"\n"+"Successful")

        else:
            self.msg_box.delete("1.0","end")
            self.msg_box.insert(tk.END, "Error:"+"\n"+ "Insufficient"+"\n"+ "information,"+"\n"+ "displaying"+"\n"+ "empty"+"\n"+ "map.")
            
        my_map.save_map()

 

    def check_active_plot(self):
        if(self.matplot_active):
            self.rightframe.canvas.get_tk_widget().destroy()
            self.matplot_active = False
            self.rightframe.pack()





    #Reads corresponding collection based on combox selections
    def read(self):
        self.check_active_plot()
        pd.set_option('display.max_rows',None)
        pd.set_option('display.max_columns',None)
        pd.options.display.width=None
        #Connect to mongodb client
        myclient = MongoClient("mongodb+srv://MylesBorthwick:8557mjb@trafficdatacluster.inrlg.mongodb.net/test?authSource=admin&replicaSet=atlas-86pvzi-shard-0&readPreference=primary&appname=MongoDB%20Compass%20Community&ssl=true")
        #Grab database
        trafficdb = myclient["TrafficData"] 

        #Handle volume combobox selection
        if(self.typeCombox.get() == "Traffic Volume"):
            #Handle year combobox selection
            if(self.yearCombox.get() == "2018"):
                #Grab collection from TrafficData database
                flow2018 = trafficdb["TrafficFlow2018"] 
                #pull data from collection
                flowdata2018 = [data for data in flow2018.find({},{"_id": 0, "year":0})] 
                #formats collection 
                flowtable2018 = pd.DataFrame(flowdata2018)
                #Clear textbox
                self.textbox.configure(state = 'normal')
                self.textbox.delete("1.0","end")
                #Update textbox
                self.textbox.insert(tk.END,str(flowtable2018))
                self.textbox.insert(tk.END, '\n')
                #Make textbox readonly
                self.textbox.configure(state = 'disabled')
                #Update status bar
                self.msg_box.delete("1.0","end")
                self.msg_box.insert(tk.END, "Read"+"\n"+"Successful")
            elif(self.yearCombox.get() == "2017"):
                flow2017= trafficdb["TrafficFlow2017"]
                flowdata2017 = [data for data in flow2017.find({},{"_id": 0, "year":0})]
                flowtable2017 = pd.DataFrame(flowdata2017)
                self.textbox.configure(state = 'normal')
                self.textbox.delete("1.0","end")
                self.textbox.insert(tk.END,str(flowtable2017))
                self.textbox.insert(tk.END, '\n')
                self.textbox.configure(state = 'disabled')
                self.msg_box.delete("1.0","end")
                self.msg_box.insert(tk.END, "Read"+"\n"+"Successful")
            elif(self.yearCombox.get() == "2016"):
                
                flow2016= trafficdb["TrafficFlow2016"]
                flowdata2016 = [data for data in flow2016.find({},{"_id": 0, "year_vol":0})]
                flowtable2016 = pd.DataFrame(flowdata2016)
                self.textbox.configure(state = 'normal')
                self.textbox.delete("1.0","end")
                self.textbox.insert(tk.END,str(flowtable2016))
                self.textbox.insert(tk.END, '\n')
                self.textbox.configure(state = 'disabled')
                self.msg_box.delete("1.0","end")
                self.msg_box.insert(tk.END, "Read"+"\n"+"Successful")
            else:
                self.msg_box.delete("1.0","end")
                self.msg_box.insert(tk.END, "Error:"+"\n"+"Please"+"\n"+"select a"+"\n"+"year")
                
        #Repeat for incident selection        
        elif (self.typeCombox.get() == "Traffic Incidents"):
            if(self.yearCombox.get() == "2018"):
                incidents2018 = trafficdb["TrafficIncidents2018"]
                incidentdata2018 = [data for data in incidents2018.find({},{"_id": 0, "year":0,"id":0})]
                incidenttable2018 = pd.DataFrame(incidentdata2018)
                self.textbox.configure(state = 'normal')
                self.textbox.delete("1.0","end")
                self.textbox.insert(tk.END,str(incidenttable2018))
                self.textbox.insert(tk.END, '\n')
                self.textbox.configure(state = 'disabled')
                self.msg_box.delete("1.0","end")
                self.msg_box.insert(tk.END, "Read"+"\n"+"Successful")
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
                self.msg_box.insert(tk.END, "Read"+"\n"+"Successful")
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
                self.msg_box.insert(tk.END, "Read"+"\n"+"Successful")
            else:
                self.msg_box.delete("1.0","end")
                self.msg_box.insert(tk.END, "Error:"+"\n"+"Please"+"\n"+"select a"+"\n"+"year")

        else:
            self.msg_box.delete("1.0","end")
            self.msg_box.insert(tk.END, "Error:"+"\n"+"Please"+"\n"+"select a"+"\n"+"Traffic"+"\n"+"Statistic")

    #Sorts selected dataset and appends the sorted list to textbox
    def sort(self):
        self.check_active_plot()
        pd.set_option('display.max_rows',None)
        pd.set_option('display.max_colwidth',90)
        myclient = MongoClient("mongodb+srv://MylesBorthwick:8557mjb@trafficdatacluster.inrlg.mongodb.net/test?authSource=admin&replicaSet=atlas-86pvzi-shard-0&readPreference=primary&appname=MongoDB%20Compass%20Community&ssl=true")
        trafficdb = myclient.TrafficData
        #Handle volume selection based on year in combox
        if(self.typeCombox.get() == "Traffic Volume"):
            if(self.yearCombox.get() == "2018"):
                flow2018 = trafficdb["TrafficFlow2018"]
                #Sort collection based on volume in decending order (ie max on top)
                flowdata2018 = [data for data in flow2018.find({},{"_id": 0, "year":0,"multilinestring":0}).sort("volume",-1)]
                flowtable2018 = pd.DataFrame(flowdata2018)
                self.textbox.configure(state = 'normal')
                self.textbox.delete("1.0","end")
                self.textbox.insert(tk.END,str(flowtable2018))
                self.textbox.insert(tk.END, '\n')
                self.textbox.configure(state = 'disabled')
                self.msg_box.delete("1.0","end")
                self.msg_box.insert(tk.END, "Sort"+"\n"+"Successful")
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
                self.msg_box.insert(tk.END, "Sort"+"\n"+"Successful")
                
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
                self.msg_box.insert(tk.END, "Sort"+"\n"+"Successful")
            else:
                self.msg_box.delete("1.0","end")
                self.msg_box.insert(tk.END, "Error:"+"\n"+"Please"+"\n"+"select a"+"\n"+"year")
        #Handle Incident selection        
        elif (self.typeCombox.get() == "Traffic Incidents"):
            if(self.yearCombox.get() == "2018"):
                incidents = trafficdb["TrafficIncidents2018"]
                #Create list of total incidents at each "INFO LOCATION" 
                incidents = list(incidents.aggregate([
                    #group data by Incident info and get the the sum of each group
                    {"$group" : { "_id": "$INCIDENT INFO", "count": { "$sum": 1 } } }, 
                    #Sort by decending number of incidents
                    {"$sort": {"count" : -1} },
                ]))
                #Update textbox and status bar
                incidents = [data for data in incidents]
                incidents = pd.DataFrame(incidents)
                self.textbox.configure(state = 'normal')
                self.textbox.delete("1.0","end")
                self.textbox.insert(tk.END,str(incidents))
                self.textbox.insert(tk.END, '\n')
                self.textbox.configure(state = 'disabled')
                self.msg_box.delete("1.0","end")
                self.msg_box.insert(tk.END, "Sort"+"\n"+"Successful")
                
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
                self.msg_box.insert(tk.END, "Sort"+"\n"+"Successful")
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
                self.msg_box.insert(tk.END, "Sort"+"\n"+"Successful")
            else:
                self.msg_box.delete("1.0","end")
                self.msg_box.insert(tk.END, "Error:"+"\n"+"Please"+"\n"+"select a"+"\n"+"year")
        else:
            self.msg_box.delete("1.0","end")
            self.msg_box.insert(tk.END, "Error:"+"\n"+"Please"+"\n"+"select a"+"\n"+"Traffic"+"\n"+"Statistic")
    
    #Returns list of max value from sorted tables and corresponding year
    def getMax(self):
        myclient = MongoClient("mongodb+srv://MylesBorthwick:8557mjb@trafficdatacluster.inrlg.mongodb.net/test?authSource=admin&replicaSet=atlas-86pvzi-shard-0&readPreference=primary&appname=MongoDB%20Compass%20Community&ssl=true")
        trafficdb = myclient.TrafficData
        #Handle volume selection based on year
        if(self.typeCombox.get() == "Traffic Volume"):
                max_values =  []
                flow2016= trafficdb["TrafficFlow2016"]
                maxflow = [data for data in flow2016.find({},{"_id": 0, "year":0,"multilinestring":0}).sort("volume",-1).limit(1)]
                maxflow = [document["volume"] for document in maxflow]
                max_values.append(maxflow[0])
            
                

                flow2017= trafficdb["TrafficFlow2017"]
                maxflow = [data for data in flow2017.find({},{"_id": 0, "year":0,"multilinestring":0}).sort("volume",-1).limit(1)]
                maxflow = [document["volume"] for document in maxflow]
                max_values.append(maxflow[0])
                
                flow2018 = trafficdb["TrafficFlow2018"]
                maxflow = [data for data in flow2018.find({},{"_id": 0, "year":0,"multilinestring":0}).sort("volume",-1).limit(1)]
                maxflow = [document["volume"] for document in maxflow]
                max_values.append(maxflow[0])
                return max_values

                
                
        #Handle Incident selection based on year     
        elif (self.typeCombox.get() == "Traffic Incidents"):
                max_values =  []
  
                incidents2016 = trafficdb.TrafficIncidents2016
                incidents2016 = list(incidents2016.aggregate([
                    {"$group" : { "_id": "$INCIDENT INFO", "count": { "$sum": 1 } } }, 
                    {"$sort": {"count" : -1} },
                ]))
                incidentmax = [data for data in incidents2016]
                incidentmax = [document["count"] for document in incidentmax]
                max_values.append(incidentmax[0])
                
                incidents2017 = trafficdb["TrafficIncidents2017"]
                incidents2017 = list(incidents2017.aggregate([
                    {"$group" : { "_id": "$INCIDENT INFO", "count": { "$sum": 1 } } }, 
                    {"$sort": {"count" : -1} },
                ]))
                incidentmax = [data for data in incidents2017]
                incidentmax = [document["count"] for document in incidentmax]
                max_values.append(incidentmax[0])
                
                incidents2018 = trafficdb["TrafficIncidents2018"]
                incidents2018 = list(incidents2018.aggregate([
                    {"$group" : { "_id": "$INCIDENT INFO", "count": { "$sum": 1 } } }, 
                    {"$sort": {"count" : -1} },
                ]))
                incidentmax = [data for data in incidents2018]
                incidentmax = [document["count"] for document in incidentmax]
                max_values.append(incidentmax[0])
                
                return max_values

        else:
            self.msg_box.delete("1.0","end")
            self.msg_box.insert(tk.END, "Error:"+"\n"+"Please"+"\n"+"select"+"\n"+"a"+"\n"+"Traffic"+"\n"+"Statistic")
            return [-1,-1,-1]
            
                
        
root =Tk()
my_gui = TrafficApp(root)
root.mainloop()