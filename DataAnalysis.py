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
                self.textbox.configure(state = 'disabled')
            elif(self.yearCombox.get() == "2017"):
                self.textbox.configure(state = 'normal')
                self.textbox.delete("1.0","end")
                flow2017= trafficdb["TrafficFlow2017"]
                flowdata2017 = [data for data in flow2017.find({},{"_id": 0, "year":0,"multilinestring":0})]
                flowtable2017 = pd.DataFrame(flowdata2017)
                self.textbox.insert(tk.END,str(flowtable2017))
                self.textbox.insert(tk.END, '\n')
                self.textbox.configure(state = 'disabled')
            elif(self.yearCombox.get() == "2016"):
                self.textbox.configure(state = 'normal')
                self.textbox.delete("1.0","end")
                flow2016= trafficdb["TrafficFlow2016"]
                flowdata2016 = [data for data in flow2016.find({},{"_id": 0, "year":0,"multilinestring":0})]
                flowtable2016 = pd.DataFrame(flowdata2016)
                self.textbox.insert(tk.END,str(flowtable2016))
                self.textbox.insert(tk.END, '\n')
                self.textbox.configure(state = 'disabled')
                
                    

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
            elif(self.yearCombox.get() == "2017"):
                incidents2017 = trafficdb["TrafficIncidents2017"]
                incidentdata2017 = [data for data in incidents2017.find({},{"_id": 0, "year":0})]
                incidenttable2017 = pd.DataFrame(incidentdata2017)
                self.textbox.configure(state = 'normal')
                self.textbox.delete("1.0","end")
                self.textbox.insert(tk.END,str(incidenttable2017))
                self.textbox.insert(tk.END, '\n')
                self.textbox.configure(state = 'disabled')
            elif(self.yearCombox.get() == "2016"):
                incidents2016 = trafficdb["TrafficIncidents2016"]
                incidentdata2016 = [data for data in incidents2016.find({},{"_id": 0, "year":0})]
                incidenttable2016 = pd.DataFrame(incidentdata2016)
                self.textbox.configure(state = 'normal')
                self.textbox.delete("1.0","end")
                self.textbox.insert(tk.END,str(incidenttable2016))
                self.textbox.insert(tk.END, '\n')
                self.textbox.configure(state = 'disabled')

    
    def sort(self):
        pd.set_option('display.max_rows',None)
        pd.set_option('display.max_colwidth',90)
        myclient = MongoClient("mongodb+srv://MylesBorthwick:8557mjb@trafficdatacluster.inrlg.mongodb.net/test?authSource=admin&replicaSet=atlas-86pvzi-shard-0&readPreference=primary&appname=MongoDB%20Compass%20Community&ssl=true")
        trafficdb = myclient.TrafficData
        
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
            elif(self.yearCombox.get() == "2017"):
                self.textbox.configure(state = 'normal')
                self.textbox.delete("1.0","end")
                flow2017= trafficdb["TrafficFlow2017"]
                flowdata2017 = [data for data in flow2017.find({},{"_id": 0, "year":0,"multilinestring":0}).sort("volume",-1)]
                flowtable2017 = pd.DataFrame(flowdata2017)
                self.textbox.insert(tk.END,str(flowtable2017))
                self.textbox.insert(tk.END, '\n')
                self.textbox.configure(state = 'disabled')
            elif(self.yearCombox.get() == "2016"):
                self.textbox.configure(state = 'normal')
                self.textbox.delete("1.0","end")
                flow2016= trafficdb["TrafficFlow2016"]
                flowdata2016 = [data for data in flow2016.find({},{"_id": 0, "year":0,"multilinestring":0}).sort("volume",-1)]
                flowtable2016 = pd.DataFrame(flowdata2016)
                self.textbox.insert(tk.END,str(flowtable2016))
                self.textbox.insert(tk.END, '\n')
                self.textbox.configure(state = 'disabled')
                
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
                
            elif(self.yearCombox.get() == "2017"):
                incidents = trafficdb["TrafficIncidents2017"]
                incidents = list(incidents.aggregate([
                    {"$group" : { "_id": "$INCIDENT INFO", "count": { "$sum": 1 } } }, 
                    {"$sort": {"count" : -1} },
                ]))
                incidents = [data for data in incidents]
                incidents = pd.DataFrame(incidents)
                self.textbox.configure(state = 'normal')
                self.textbox.delete("1.0","end")a   
                self.textbox.insert(tk.END,str(incidents))
                self.textbox.insert(tk.END, '\n')
                self.textbox.configure(state = 'disabled')
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