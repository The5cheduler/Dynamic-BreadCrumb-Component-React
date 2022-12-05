from fastapi import FastAPI, APIRouter, Request
import re
import json
from operations import getfirstchild, findkeys

# initiating the app
app = FastAPI()

# creating my router
my_router = APIRouter(prefix="/path")

# loading the directory from Json File
crumbsData = json.load(open('./directory.json'))

@app.api_route("/{path_name:path}", methods=["GET"])
async def catch_all(path_name: str):
    result = {}
    if not path_name:
        return {"details" :  "Not Found"}
    
    if "path" == path_name:
        return getfirstchild(data=crumbsData)
    
    path_values = list()
    

    if path_name and '/' in path_name:
        path_values = path_name.split("/")[1:]
    else: 
        path_values = ["home"]
    
    immediate_child = []    
    last_node = path_values[-1]

    for value in findkeys(crumbsData,last_node):
        result["type"] = value["type"]
        for child_key, child_value in value.items():
            if child_key == "children":
                immediate_child.extend(child_value.keys())
    result["children"] = immediate_child
    return result
