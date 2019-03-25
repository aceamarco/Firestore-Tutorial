#This file is meant to just set up the database, you're free to 
#start working with it however you like!

# #Austin's all powerful module manager
import module_manager
module_manager.review()
#Firestore modules
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from google.cloud.firestore_v1beta1 import ArrayRemove, ArrayUnion
#Python Modules
import datetime
import time


#From the Google Cloud Documentation
#First create a service account, generate a new private key and save the JSON file to this folder.
#If you're going to change the name of the file, change the file name on line 20
#Use this link: https://console.cloud.google.com/iam-admin/serviceaccounts
# Use a service account
cred = credentials.Certificate('serviceAccount.json')
firebase_admin.initialize_app(cred)

db = firestore.client()

####Begin Writing your own code here#####
