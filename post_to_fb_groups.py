#-*- coding: utf-8 -*-
import time
from facepy import GraphAPI


#Author: T Shrinivasan <tshrinivasan@gmail.com>


# get api from here  https://developers.facebook.com/tools/explorer


api = ""


graph = GraphAPI(api)

message = '''


בדיקה 1 2 3




'''


# Find the ids of your desired groups from http://lookup-id.com/  
# and add this in this array groups

groups = ['']


for group_id in groups:
    graph.post(path=str(group_id) + "/feed", message=message)
    time.sleep(10)
print("Done")
