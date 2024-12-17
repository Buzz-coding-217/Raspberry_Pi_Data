from tinydb import TinyDB, Query
db = TinyDB('db.json')
import pyrebase                                                                                 #import the pyrebase module which allows us to communicate with the firebase servers.
from time import sleep

config = {                                                             #define a dictionary named config with several key-value pairs that configure the connection to the database.
  "apiKey": "AIzaSyAEs6ayyqojMgfiNl-p4OqdwfIS2ztGKaE",
  "authDomain": "test-e8b6a.firebaseapp.com",
  "databaseURL": "https://test-e8b6a-default-rtdb.firebaseio.com",
  "storageBucket": "test-e8b6a.appspot.com"
}

firebase = pyrebase.initialize_app(config)
user = Query()

trolley = "A"
items = ["milk","butter"]

for item in items:
    database = firebase.database()                                        #take an instance from the firebase database which is pointing to the root directory of your database.
    crate = database.child(trolley)                        #get the child "RGBControl" path in your database and store it inside the "RGBControlBucket" variable.
    quantity_ = crate.child(item).get().val()
    result = db.get(Query()['item'] == item)
    leftover = int(result.get('quantity'))
    leftover = leftover - quantity_
    db.update({'quantity': leftover}, user.item == item)

print(db.all())