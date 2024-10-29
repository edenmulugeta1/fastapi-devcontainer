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
    
