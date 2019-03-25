# #Austin's all powerful module manager
import module_manager
module_manager.review()

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import datetime

###################################################################
#Uncomment the chuncks of code as you proceed through the document#
###################################################################


#From the Google Cloud Documentation
#First create a service account, generate a new private key and save the JSON file to this folder.
#If you're going to change the name of the file, change the file name on line 20
#Use this link: https://console.cloud.google.com/iam-admin/serviceaccounts
# Use a service account
cred = credentials.Certificate('serviceAccount.json')
firebase_admin.initialize_app(cred)

db = firestore.client()

'''
#Add Info
doc_ref = db.collection(u'users').document(u'alovelace')
doc_ref.set({
    u'first': u'Ada',
    u'last': u'Lovelace',
    u'born': 1815
})
#Add another(different) document
doc_ref = db.collection(u'users').document(u'aturing')
doc_ref.set({
    u'first': u'Alan',
    u'middle': u'Mathison',
    u'last': u'Turing',
    u'born': 1912
})
'''

'''
#To read data you can see it online or by using the following code
users_ref = db.collection(u'users')
docs = users_ref.get()
#doc.id is the name of the document, doc.to_dict returns all of its attributes
for doc in docs:
    print(u'{} => {}'.format(doc.id, doc.to_dict()))

data = {
    u'name': u'Los Angeles',
    u'state': u'CA',
    u'country': u'USA'
}
'''

'''
# Add a new doc in collection 'cities' with ID 'LA'
db.collection(u'cities').document(u'LA').set(data)

#Set merge = True in case you don't know if a document exists
city_ref = db.collection(u'cities').document(u'BJ')
city_ref.set({
    'capital': True
},merge = True)
'''

'''
#Here are all the types of data you can store in Firestore
data = {
    u'stringExample': u'Hello, World!',
    u'booleanExample': True,
    u'numberExample': 3.14159265,
    u'dateExample': datetime.datetime.now(),
    u'arrayExample': [5, True, u'hello'],
    u'nullExample': None,
    u'objectExample': {
        u'a': 5,
        u'b': True
    }
}

db.collection(u'data').document(u'one').set(data)
'''

'''
#Example of how to create objects and then add them to the database
class Person(object):

    def __init__(self,age):
        self.age = age

    #Call this method when you want to add this object to the database
    def to_dict(self):
        return {u'age':self.age}

    #We'll use this later to create a City object from a document in the database
    def from_dict(self,document):
        return City(document[u'age'])

#You can set the dictionary containing the objects attributes to the database
me = Person(age = 21)
db.collection(u'users').document(u'Marco').set(me.to_dict())
'''

'''
#To Update information
ref = db.collection(u'users').document(u'Marco')
ref.update({u'age':19})
'''

'''
#To update dictionaries (From the Google Documentation)
# Create an initial document to update
frank_ref = db.collection(u'users').document(u'frank')
frank_ref.set({
    u'name': u'Frank',
    u'favorites': {
        u'food': u'Pizza',
        u'color': u'Blue',
        u'subject': u'Recess'
    },
    u'age': 12
})
'''

'''
# Update age and favorite color
frank_ref.update({
    u'age': 13,
    u'favorites.color': u'Red'
})
'''

'''
#To Update Arrays
city_ref = db.collection(u'cities').document(u'DC')

# Automatically add a new region to the 'regions' array field.
city_ref.update({u'regions': ArrayUnion([u'greater_virginia'])})

# // Automatically remove a region from the 'regions' array field.
city_ref.update({u'regions': ArrayRemove([u'east_coast'])})
'''

'''
#To delete attributes from a document use .DELETE_FIELD
city_ref = db.collection(u'cities').document(u'BJ')
city_ref.update({
    u'capital': firestore.DELETE_FIELD
})
'''

'''
#This is how you create a Python object from the values in the database
doc_ref = db.collection(u'users').document(u'Marco')
doc = doc_ref.get()
city = Person.from_dict(doc.to_dict())
print(city)
'''

'''
#This is how you query, or filter through a collection for specific documents
#.where() can also use u'<', u'>', u'==', u'<=', u'>=', and u'array_contains'
user_collection = db.collection(u'users')
query = user_collection.where(u'age', u'==', 21)
'''
