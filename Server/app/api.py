from fastapi import FastAPI, APIRouter, Request
from starlette.middleware import Middleware
from starlette.middleware.cors import CORSMiddleware
import re
import json
from .operations import getfirstchild, findkeys, pathIsPath

middleware = [
    Middleware(
        CORSMiddleware,
        allow_origins=['*'],
        allow_credentials=True,
        allow_methods=['*'],
        allow_headers=['*']
    )
]

# initiating the app
app = FastAPI(middleware=middleware)

# creating my router
my_router = APIRouter(prefix="/path")

# loading the directory from Json File
crumbsData = json.load(open('../Server/directory.json'))

origins = [
    "http://localhost:3000",
    "localhost:3000"
]

@app.api_route("/{path_name:path}", methods=["GET"])
async def catch_all(path_name: str):
    
    if "path" == path_name:
        return pathIsPath(crumbsData)
    
    path_values = list()
    
    if path_name and '/' in path_name and "path" in path_name:
        if path_name[-1] == '/':
            return pathIsPath(crumbsData) 
        else: 
            path_values = path_name.split("/")[1:]
        # path_values = path_name.split("/")[1:]
        result = {}
        immediate_child = []    
        current_node = path_values[-1]
        result["currentNode"] = current_node
        result["previousNodes"] = path_values if len(path_values) > 1 else list()

        for value in findkeys(crumbsData,current_node):
            result["currentNodeType"] = value["type"]
            for child_key, child_value in value.items():
                if child_key == "children":
                    immediate_child.extend(child_value.keys())
        result["childrenNodes"] = immediate_child
        return result
    
    return {"message" :  "There is no Directory to look!", "statusCode" : 404}