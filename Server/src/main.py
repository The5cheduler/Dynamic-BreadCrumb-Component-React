from fastapi import FastAPI
import json

# initiating the app
app = FastAPI()

# loading the directory from Json File
crumbsData = json.load(open('../src/directory.json'))

@app.get("/")
def root():
    return crumbsData
