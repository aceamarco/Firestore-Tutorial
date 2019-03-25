# #Austin's all powerful module manager
import module_manager
module_manager.review()

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from google.cloud.firestore_v1beta1 import ArrayRemove, ArrayUnion
import datetime
import time

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
