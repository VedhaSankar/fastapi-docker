'''
Created on 

Course work: 

@author: vedha

Source:
    
'''

# Import necessary modules

from typing import Optional
from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/")
def read_root():
    
    return {"Content": "Marketing Content Validator"}


@app.get("/product/{product_name}")
def read_item(product_name: str):

    category = "household"

    confidence_rate = 0.9

    result = {

        "product name"      : product_name,
        "category"          : category,
        "confidence rate"   : confidence_rate
    }


    return result


if __name__== "__main__":

    uvicorn.run(host="0.0.0.0", debug = True, port = 8500)