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
    
    return {"Hello": "World"}


@app.get("/product/{product_name}")
def read_item(item_id: int, q: Optional[str] = None):

    return {"item_id": item_id, "q": q}


if __name__== "__main__":

    uvicorn.run(host="0.0.0.0", debug = True, port=8500)