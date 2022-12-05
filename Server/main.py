from fastapi import FastAPI, APIRouter, Request
import re
import json
from operations import getAllimmdieateChildren

# initiating the app
app = FastAPI()

# creating my router
my_router = APIRouter(prefix="/path")

# loading the directory from Json File
crumbsData = json.load(open('./directory.json'))

@app.api_route("/{path_name:path}", methods=["GET"])
async def catch_all(path_name: str):
    return getAllimmdieateChildren(crumbsData, path_name)

# @app.get("/path/{route_path}")
# async def get_path(route_path :str):
     
#     return getAllimmdieateChildren(crumbsData, pathString = route_path)