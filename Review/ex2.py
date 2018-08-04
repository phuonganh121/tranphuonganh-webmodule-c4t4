from mongoengine import * 
import mlab

class Data(Document):
    name = StringField()
    age = StringField()
    address = StringField()
    ref = StringField()
    meta = {"collection": "customers"}

mlab.connect()
data_list = Data.objects(ref__icontains = "Event")

print (len(data_list))


for data in data_list: 
    print (data.name)
