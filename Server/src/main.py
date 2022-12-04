from fastapi import FastAPI
import json
from operations import getAllimmdieateChildren

# initiating the app
app = FastAPI()

# loading the directory from Json File
crumbsData = json.load(open('../src/directory.json'))

@app.get("/")
def root():
    children = getAllimmdieateChildren(crumbsData)
    return children
