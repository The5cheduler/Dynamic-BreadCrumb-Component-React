from fastapi import FastAPI, APIRouter
import re
import json
from operations import getAllimmdieateChildren

# initiating the app
app = FastAPI()

# creating my router
my_router = APIRouter()

# loading the directory from Json File
crumbsData = json.load(open('./directory.json'))

def generate_route_signature(route_path : str) :
    args 


@app.get("/path/{route_path}")
async def get_path(route_path :str):
    if route_path:
        return getAllimmdieateChildren(crumbsData)
    else :
        print(path)
        childrens = getAllimmdieateChildren(crumbsData, pathString = route_path)
        return childrens