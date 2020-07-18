from pymongo import MongoClient


myclient = MongoClient("mongodb+srv://MylesBorthwick:8557mjb@trafficdatacluster.inrlg.mongodb.net/test?authSource=admin&replicaSet=atlas-86pvzi-shard-0&readPreference=primary&appname=MongoDB%20Compass%20Community&ssl=true")

mydb = myclient["TrafficData"]
flow = mydb["TrafficFlow"]
incidents = mydb["TrafficIncidents"]


x = incidents.find_one()

print(x)