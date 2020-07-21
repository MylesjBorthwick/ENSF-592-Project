from pymongo import MongoClient
from tkinter import Tk, Label, Button, ttk, LEFT, RIGHT, Frame, WORD, END
import tkinter as tk
from pprint import pprint
import pandas as pd




myclient = MongoClient("mongodb+srv://MylesBorthwick:8557mjb@trafficdatacluster.inrlg.mongodb.net/test?authSource=admin&replicaSet=atlas-86pvzi-shard-0&readPreference=primary&appname=MongoDB%20Compass%20Community&ssl=true")
trafficdb = myclient["TrafficData"]
flow2018 = trafficdb["TrafficFlow2018"]

    
tabledata = [data for data in flow2018.find()]
formattable = pd.DataFrame(tabledata)
print(formattable)