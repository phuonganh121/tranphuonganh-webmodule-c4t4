# mongodb://<dbuser>:<dbpassword>@ds145881.mlab.com:45881/c4t4

import mongoengine

host = "ds145881.mlab.com"
port = 45881
db_name = "c4t4"
user_name = "admin"
password = "phuonganh1201"


def connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)

def list2json(l):
    import json
    return [json.loads(item.to_json()) for item in l]

def item2json(item):
    import json
    return json.loads(item.to_json())