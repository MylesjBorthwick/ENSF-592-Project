
from pymongo import MongoClient


myclient = MongoClient("mongodb+srv://MylesBorthwick:8557mjb@trafficdatacluster.inrlg.mongodb.net/test?authSource=admin&replicaSet=atlas-86pvzi-shard-0&readPreference=primary&appname=MongoDB%20Compass%20Community&ssl=true")

trafficdb = myclient["TrafficData"]

flow2018 = trafficdb["TrafficFlow2018"]
flow2017= trafficdb["TrafficFlow2017"]
flow2016= trafficdb["TrafficFlow2016"]


incidents2018 = trafficdb["TrafficIncidents2018"]
incidents2017 = trafficdb["TrafficIncidents2017"]
incidents2016 = trafficdb["TrafficIncidents2016"]



#Sort volume data     
sortedFlow2018 = flow2018.find({},{"_id": 0,"volume":1}).sort("volume", -1)
sortedFlow2017 = flow2017.find({},{"_id": 0,"volume":1}).sort("volume", -1)
sortedFlow2016 = flow2016.find({},{"_id": 0,"volume":1}).sort("volume", -1)


#Print top 30 volumes
totalVolume2018 = sum(sortedFlow2018)
totalVolume2017 = sum([row[0] for row in sortedFlow2017.fetchall()])
totalVolume2016 = sum([row[0] for row in sortedFlow2016.fetchall()])



print(totalVolume2018)



#TODO Sort collections by volume or incidents