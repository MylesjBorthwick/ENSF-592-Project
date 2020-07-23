class DataAnalysis:
    def read(self):
        pd.set_option('display.max_rows',None,'display.max_columns',10)
        pd.options.display.width=None
        myclient = MongoClient("mongodb+srv://MylesBorthwick:8557mjb@trafficdatacluster.inrlg.mongodb.net/test?authSource=admin&replicaSet=atlas-86pvzi-shard-0&readPreference=primary&appname=MongoDB%20Compass%20Community&ssl=true")
        trafficdb = myclient["TrafficData"] #all the databases are in here. 
        
        #handle volume selection
        if(TrafficGUI.typeCombox.get() == "Traffic Volume"):
            if(TrafficGUI.yearCombox.get() == "2018"):
                flow2018 = trafficdb["TrafficFlow2018"] #grabbing a data collection
                flowdata2018 = [data for data in flow2018.find({},{"_id": 0, "year":0,"multilinestring":0})] #pull data from collection
                flowtable2018 = pd.DataFrame(flowdata2018) #formats collection 
                TrafficGUI.textbox.delete("1.0","end")
                TrafficGUI.textbox.insert(tk.END,str(flowtable2018))
                TrafficGUI.textbox.insert(tk.END, '\n')
                TrafficGUI.textbox.configure(state = 'disabled')
                TrafficGUI.msg_box.delete("1.0","end")
                TrafficGUI.msg_box.insert(tk.END, "Read"+"\n"+"Succesful")
            elif(TrafficGUI.yearCombox.get() == "2017"):
                TrafficGUI.textbox.configure(state = 'normal')
                TrafficGUI.textbox.delete("1.0","end")
                flow2017= trafficdb["TrafficFlow2017"]
                flowdata2017 = [data for data in flow2017.find({},{"_id": 0, "year":0,"multilinestring":0})]
                flowtable2017 = pd.DataFrame(flowdata2017)
                TrafficGUI.textbox.insert(tk.END,str(flowtable2017))
                TrafficGUI.textbox.insert(tk.END, '\n')
                TrafficGUI.textbox.configure(state = 'disabled')
                TrafficGUI.msg_box.delete("1.0","end")
                TrafficGUI.msg_box.insert(tk.END, "Read"+"\n"+"Succesful")
            elif(TrafficGUI.yearCombox.get() == "2016"):
                TrafficGUI.textbox.configure(state = 'normal')
                TrafficGUI.textbox.delete("1.0","end")
                flow2016= trafficdb["TrafficFlow2016"]
                flowdata2016 = [data for data in flow2016.find({},{"_id": 0, "year":0,"multilinestring":0})]
                flowtable2016 = pd.DataFrame(flowdata2016)
                TrafficGUI.textbox.insert(tk.END,str(flowtable2016))
                TrafficGUI.textbox.insert(tk.END, '\n')
                TrafficGUI.textbox.configure(state = 'disabled')
                TrafficGUI.msg_box.delete("1.0","end")
                TrafficGUI.msg_box.insert(tk.END, "Read"+"\n"+"Succesful")
                
        #Handle Incident selection        
        elif (TrafficGUI.typeCombox.get() == "Traffic Incidents"):
            if(TrafficGUI.yearCombox.get() == "2018"):
                incidents2018 = trafficdb["TrafficIncidents2018"]
                incidentdata2018 = [data for data in incidents2018.find({},{"_id": 0, "year":0,"id":0,"Longitude":0,"Latitude":0})]
                incidenttable2018 = pd.DataFrame(incidentdata2018)
                TrafficGUI.textbox.configure(state = 'normal')
                TrafficGUI.textbox.delete("1.0","end")
                TrafficGUI.textbox.insert(tk.END,str(incidenttable2018))
                TrafficGUI.textbox.insert(tk.END, '\n')
                TrafficGUI.textbox.configure(state = 'disabled')
                TrafficGUI.msg_box.delete("1.0","end")
                TrafficGUI.msg_box.insert(tk.END, "Read"+"\n"+"Succesful")
            elif(TrafficGUI.yearCombox.get() == "2017"):
                incidents2017 = trafficdb["TrafficIncidents2017"]
                incidentdata2017 = [data for data in incidents2017.find({},{"_id": 0, "year":0})]
                incidenttable2017 = pd.DataFrame(incidentdata2017)
                TrafficGUI.textbox.configure(state = 'normal')
                TrafficGUI.textbox.delete("1.0","end")
                TrafficGUI.textbox.insert(tk.END,str(incidenttable2017))
                TrafficGUI.textbox.insert(tk.END, '\n')
                TrafficGUI.textbox.configure(state = 'disabled')
                TrafficGUI.msg_box.delete("1.0","end")
                TrafficGUI.msg_box.insert(tk.END, "Read"+"\n"+"Succesful")
            elif(TrafficGUI.yearCombox.get() == "2016"):
                incidents2016 = trafficdb["TrafficIncidents2016"]
                incidentdata2016 = [data for data in incidents2016.find({},{"_id": 0, "year":0})]
                incidenttable2016 = pd.DataFrame(incidentdata2016)
                TrafficGUI.textbox.configure(state = 'normal')
                TrafficGUI.textbox.delete("1.0","end")
                TrafficGUI.textbox.insert(tk.END,str(incidenttable2016))
                TrafficGUI.textbox.insert(tk.END, '\n')
                TrafficGUI.textbox.configure(state = 'disabled')
                TrafficGUI.msg_box.delete("1.0","end")
                TrafficGUI.msg_box.insert(tk.END, "Read"+"\n"+"Succesful")

    #Sorts selected dataset and appends the sorted list to textbox
    def sort(self):
        pd.set_option('display.max_rows',None)
        pd.set_option('display.max_colwidth',90)
        myclient = MongoClient("mongodb+srv://MylesBorthwick:8557mjb@trafficdatacluster.inrlg.mongodb.net/test?authSource=admin&replicaSet=atlas-86pvzi-shard-0&readPreference=primary&appname=MongoDB%20Compass%20Community&ssl=true")
        trafficdb = myclient.TrafficData
        #Handle volume selection based on year in combox
        if(TrafficGUI.typeCombox.get() == "Traffic Volume"):
            if(TrafficGUI.yearCombox.get() == "2018"):
                flow2018 = trafficdb["TrafficFlow2018"]
                flowdata2018 = [data for data in flow2018.find({},{"_id": 0, "year":0,"multilinestring":0}).sort("volume",-1)]
                flowtable2018 = pd.DataFrame(flowdata2018)
                TrafficGUI.textbox.configure(state = 'normal')
                TrafficGUI.textbox.delete("1.0","end")
                TrafficGUI.textbox.insert(tk.END,str(flowtable2018))
                TrafficGUI.textbox.insert(tk.END, '\n')
                TrafficGUI.textbox.configure(state = 'disabled')
                TrafficGUI.msg_box.delete("1.0","end")
                TrafficGUI.msg_box.insert(tk.END, "Sort"+"\n"+"Succesful")
            elif(TrafficGUI.yearCombox.get() == "2017"):
                TrafficGUI.textbox.configure(state = 'normal')
                TrafficGUI.textbox.delete("1.0","end")
                flow2017= trafficdb["TrafficFlow2017"]
                flowdata2017 = [data for data in flow2017.find({},{"_id": 0, "year":0,"multilinestring":0}).sort("volume",-1)]
                flowtable2017 = pd.DataFrame(flowdata2017)
                TrafficGUI.textbox.insert(tk.END,str(flowtable2017))
                TrafficGUI.textbox.insert(tk.END, '\n')
                TrafficGUI.textbox.configure(state = 'disabled')
                TrafficGUI.msg_box.delete("1.0","end")
                TrafficGUI.msg_box.insert(tk.END, "Sort"+"\n"+"Succesful")
                
            elif(TrafficGUI.yearCombox.get() == "2016"):
                TrafficGUI.textbox.configure(state = 'normal')
                TrafficGUI.textbox.delete("1.0","end")
                flow2016= trafficdb["TrafficFlow2016"]
                flowdata2016 = [data for data in flow2016.find({},{"_id": 0, "year":0,"multilinestring":0}).sort("volume",-1)]
                flowtable2016 = pd.DataFrame(flowdata2016)
                TrafficGUI.textbox.insert(tk.END,str(flowtable2016))
                TrafficGUI.textbox.insert(tk.END, '\n')
                TrafficGUI.textbox.configure(state = 'disabled')
                TrafficGUI.msg_box.delete("1.0","end")
                TrafficGUI.msg_box.insert(tk.END, "Sort"+"\n"+"Succesful")
        #Handle Incident selection        
        elif (TrafficGUI.typeCombox.get() == "Traffic Incidents"):
            if(TrafficGUI.yearCombox.get() == "2018"):
                incidents = trafficdb["TrafficIncidents2018"]
                incidents = list(incidents.aggregate([
                    {"$group" : { "_id": "$INCIDENT INFO", "count": { "$sum": 1 } } }, 
                    {"$sort": {"count" : -1} },
                ]))
                incidents = [data for data in incidents]
                incidents = pd.DataFrame(incidents)
                TrafficGUI.textbox.configure(state = 'normal')
                TrafficGUI.textbox.delete("1.0","end")
                TrafficGUI.textbox.insert(tk.END,str(incidents))
                TrafficGUI.textbox.insert(tk.END, '\n')
                TrafficGUI.textbox.configure(state = 'disabled')
                TrafficGUI.msg_box.delete("1.0","end")
                TrafficGUI.msg_box.insert(tk.END, "Sort"+"\n"+"Succesful")
                
            elif(TrafficGUI.yearCombox.get() == "2017"):
                incidents = trafficdb["TrafficIncidents2017"]
                incidents = list(incidents.aggregate([
                    {"$group" : { "_id": "$INCIDENT INFO", "count": { "$sum": 1 } } }, 
                    {"$sort": {"count" : -1} },
                ]))
                incidents = [data for data in incidents]
                incidents = pd.DataFrame(incidents)
                TrafficGUI.textbox.configure(state = 'normal')
                TrafficGUI.textbox.delete("1.0","end")
                TrafficGUI.textbox.insert(tk.END,str(incidents))
                TrafficGUI.textbox.insert(tk.END, '\n')
                TrafficGUI.textbox.configure(state = 'disabled')
                TrafficGUI.msg_box.delete("1.0","end")
                TrafficGUI.msg_box.insert(tk.END, "Sort"+"\n"+"Succesful")
            elif(TrafficGUI.yearCombox.get() == "2016"):
                incidents = trafficdb.TrafficIncidents2016
                incidents = list(incidents.aggregate([
                    {"$group" : { "_id": "$INCIDENT INFO", "count": { "$sum": 1 } } }, 
                    {"$sort": {"count" : -1} },
                ]))
                incidents = [data for data in incidents]
                incidents = pd.DataFrame(incidents)
                TrafficGUI.textbox.configure(state = 'normal')
                TrafficGUI.textbox.delete("1.0","end")
                TrafficGUI.textbox.insert(tk.END,str(incidents))
                TrafficGUI.textbox.insert(tk.END, '\n')
                TrafficGUI.textbox.configure(state = 'disabled')
                TrafficGUI.msg_box.delete("1.0","end")
                TrafficGUI.msg_box.insert(tk.END, "Sort"+"\n"+"Succesful")
    
    #Returns max value for dataset based on combox selections
    def getMax(self):
        myclient = MongoClient("mongodb+srv://MylesBorthwick:8557mjb@trafficdatacluster.inrlg.mongodb.net/test?authSource=admin&replicaSet=atlas-86pvzi-shard-0&readPreference=primary&appname=MongoDB%20Compass%20Community&ssl=true")
        trafficdb = myclient.TrafficData
        #Handle volume selection based on year
        if(TrafficGUI.typeCombox.get() == "Traffic Volume"):
            if(TrafficGUI.yearCombox.get() == "2018"):
                flow2018 = trafficdb["TrafficFlow2018"]
                maxflow = [data for data in flow2018.find({},{"_id": 0, "year":0,"multilinestring":0}).sort("volume",-1).limit(1)]
                maxflow = [document["volume"] for document in maxflow]
                return maxflow([0])
                

            elif(TrafficGUI.yearCombox.get() == "2017"):
                flow2017= trafficdb["TrafficFlow2017"]
                maxflow = [data for data in flow2017.find({},{"_id": 0, "year":0,"multilinestring":0}).sort("volume",-1).limit(1)]
                maxflow = [document["volume"] for document in maxflow]
                return maxflow([0])
                
                
            elif(TrafficGUI.yearCombox.get() == "2016"):
                
                flow2016= trafficdb["TrafficFlow2016"]
                maxflow = [data for data in flow2016.find({},{"_id": 0, "year":0,"multilinestring":0}).sort("volume",-1).limit(1)]
                maxflow = [document["volume"] for document in maxflow]
                return maxflow([0])
                
        #Handle Incident selection based on year     
        elif (TrafficGUI.typeCombox.get() == "Traffic Incidents"):
            if(TrafficGUI.yearCombox.get() == "2018"):
                incidents = trafficdb["TrafficIncidents2018"]
                incidents = list(incidents.aggregate([
                    {"$group" : { "_id": "$INCIDENT INFO", "count": { "$sum": 1 } } }, 
                    {"$sort": {"count" : -1} },
                ]))
                incidentmax = [data for data in incidents]
                incidentmax = [document["count"] for document in incidentmax]
                return incidentmax[0]
                
               
                
            elif(TrafficGUI.yearCombox.get() == "2017"):
                incidents = trafficdb["TrafficIncidents2017"]
                incidents = list(incidents.aggregate([
                    {"$group" : { "_id": "$INCIDENT INFO", "count": { "$sum": 1 } } }, 
                    {"$sort": {"count" : -1} },
                ]))
                incidentmax = [data for data in incidents]
                incidentmax = [document["count"] for document in incidentmax]
                return incidentmax[0]
                
               
                
            elif(TrafficGUI.yearCombox.get() == "2016"):
                incidents = trafficdb.TrafficIncidents2016
                incidents = list(incidents.aggregate([
                    {"$group" : { "_id": "$INCIDENT INFO", "count": { "$sum": 1 } } }, 
                    {"$sort": {"count" : -1} },
                ]))
                incidentmax = [data for data in incidents]
                incidentmax = [document["count"] for document in incidentmax]
                return incidentmax[0]