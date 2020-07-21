import pandas as pd
from pymongo import MongoClient



class DataAnalysis:
     
    def read():
       pd.set_option('display.max_rows',None)
       myclient = MongoClient("mongodb+srv://MylesBorthwick:8557mjb@trafficdatacluster.inrlg.mongodb.net/test?authSource=admin&replicaSet=atlas-86pvzi-shard-0&readPreference=primary&appname=MongoDB%20Compass%20Community&ssl=true")
       trafficdb = myclient["TrafficData"]
       
       if(MyFirstGUI.typeCombox.get() == "Traffic Volume"):
           if(MyFirstGUI.yearCombox.get() == "2018"):
               flow2018 = trafficdb["TrafficFlow2018"]
               flowdata2018 = [data for data in flow2018.find({},{"_id": 0, "year":0,"multilinestring":0})]
               flowtable2018 = pd.DataFrame(flowdata2018)
               MyFirstGUI.textbox.delete("1.0","end")
               MyFirstGUI.textbox.insert(tk.END,str(flowtable2018))
               MyFirstGUI.textbox.insert(tk.END, '\n')
           elif(MyFirstGUI.yearCombox.get() == "2017"):
               MyFirstGUI.textbox.delete("1.0","end")
               flow2017= trafficdb["TrafficFlow2017"]
               flowdata2017 = [data for data in flow2017.find({},{"_id": 0, "year":0,"multilinestring":0})]
               flowtable2017 = pd.DataFrame(flowdata2017)
               MyFirstGUI.textbox.insert(tk.END,str(flowtable2017))
               MyFirstGUI.textbox.insert(tk.END, '\n')
           elif(MyFirstGUI.yearCombox.get() == "2016"):
               MyFirstGUI.textbox.delete("1.0","end")
               flow2016= trafficdb["TrafficFlow2016"]
               flowdata2016 = [data for data in flow2016.find({},{"_id": 0, "year":0,"multilinestring":0})]
               flowtable2016 = pd.DataFrame(flowdata2016)
               MyFirstGUI.textbox.insert(tk.END,str(flowtable2016))
               MyFirstGUI.textbox.insert(tk.END, '\n')
               
                   
       elif (MyFirstGUI.typeCombox.get() == "Traffic Incidents"):
           if(MyFirstGUI.yearCombox.get() == "2018"):
               incidents2018 = trafficdb["TrafficIncidents2018"]
           elif(MyFirstGUI.yearCombox.get() == "2017"):
               incidents2017 = trafficdb["TrafficIncidents2017"]
           elif(MyFirstGUI.yearCombox.get() == "2016"):
               incidents2016 = trafficdb["TrafficIncidents2016"]
    
    def sort():
        pd.set_option('display.max_rows',None)
        myclient = MongoClient("mongodb+srv://MylesBorthwick:8557mjb@trafficdatacluster.inrlg.mongodb.net/test?authSource=admin&replicaSet=atlas-86pvzi-shard-0&readPreference=primary&appname=MongoDB%20Compass%20Community&ssl=true")
        trafficdb = myclient["TrafficData"]
        
        if(MyFirstGUI.typeCombox.get() == "Traffic Volume"):
            if(MyFirstGUI.yearCombox.get() == "2018"):
                flow2018 = trafficdb["TrafficFlow2018"]
                flowdata2018 = [data for data in flow2018.find({},{"_id": 0, "year":0,"multilinestring":0}).sort("volume",-1)]
                flowtable2018 = pd.DataFrame(flowdata2018)
                MyFirstGUI.textbox.delete("1.0","end")
                MyFirstGUI.textbox.insert(tk.END,str(flowtable2018))
                MyFirstGUI.textbox.insert(tk.END, '\n')
            elif(MyFirstGUI.yearCombox.get() == "2017"):
                MyFirstGUI.textbox.delete("1.0","end")
                flow2017= trafficdb["TrafficFlow2017"]
                flowdata2017 = [data for data in flow2017.find({},{"_id": 0, "year":0,"multilinestring":0}).sort("volume",-1)]
                flowtable2017 = pd.DataFrame(flowdata2017)
                MyFirstGUI.textbox.insert(tk.END,str(flowtable2017))
                MyFirstGUI.textbox.insert(tk.END, '\n')
            elif(MyFirstGUI.yearCombox.get() == "2016"):
                MyFirstGUI.textbox.delete("1.0","end")
                flow2016= trafficdb["TrafficFlow2016"]
                flowdata2016 = [data for data in flow2016.find({},{"_id": 0, "year":0,"multilinestring":0}).sort("volume",-1)]
                flowtable2016 = pd.DataFrame(flowdata2016)
                MyFirstGUI.textbox.insert(tk.END,str(flowtable2016))
                MyFirstGUI.textbox.insert(tk.END, '\n')
                
        elif (MyFirstGUI.typeCombox.get() == "Traffic Incidents"):
            if(MyFirstGUI.yearCombox.get() == "2018"):
                incidents2018 = trafficdb["TrafficIncidents2018"]
            elif(MyFirstGUI.yearCombox.get() == "2017"):
                incidents2017 = trafficdb["TrafficIncidents2017"]
            elif(MyFirstGUI.yearCombox.get() == "2016"):
                incidents2016 = trafficdb["TrafficIncidents2016"]