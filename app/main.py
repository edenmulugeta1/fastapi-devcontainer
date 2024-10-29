#!/usr/bin/env python3

from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import json
import os

api = FastAPI()

@api.get("/")  # zone apex
def zone_apex():
    return {"Hello": "Hello API"}

@api.get("/add/{a}/{b}")
def add(a: int, b: int):
    return {"sum": a + b}
@api.get("customer/{idx}"):
def customer (idx:int):
    #read the data into df 
    df = pd.read_csv("../cutomers.csv")
    customer = df.iloc[idx]
    return customer.to_dict()

@api.post("/get_body")
async def get_body(request: Request):
    return = await request.json()
    first_name = response["fname"]
    last_name = response["lname"]
    favorite_number = response["favnu]
    return {"first_name": first_name, "last_name": last_name, "favorite_number": favorite_name}

