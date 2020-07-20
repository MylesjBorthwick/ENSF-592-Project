
from pymongo import MongoClient


myclient = MongoClient("mongodb+srv://MylesBorthwick:8557mjb@trafficdatacluster.inrlg.mongodb.net/test?authSource=admin&replicaSet=atlas-86pvzi-shard-0&readPreference=primary&appname=MongoDB%20Compass%20Community&ssl=true")

trafficdb = myclient["TrafficData"]
flow = trafficdb["TrafficFlow"]
incidents = trafficdb["TrafficIncidents"]



#Sort volume data     
sortlistVolume = flow.find({},{"_id": 0,"volume":1}).sort("volume", -1)


for x in sortlistVolume[0:30]:
    print(x)

#for x in incidents.find({},{ "_id": 0, "location":1, "Count": 1}):
#  print(x)
##print(trafficdb.list_collection_names())
#for x in flow.find({},{ "_id": 0, "year":1,"YEAR":1,"year_vol":1, "Count": 1}):
#  print(x)



#TODO Sort collections by volume or incidents