from fastapi import FastAPI, Path, Query, HTTPException, status
from typing import Optional
from pydantic import BaseModel


app  = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    brand: Optional[str] = None

class UpdateItem(BaseModel):
    name: Optional[str] = None
    price: Optional[float] = None
    brand: Optional[str] = None
inventory = {}

@app.get("/get-item/{item_id}")

def get_item(item_id : int = Path(..., description="The ID of the item you like to view.")):
    
    if item_id in inventory:
        return inventory[item_id]
    
    raise HTTPException(status_code= 404, detail= "Item Id not found.")

@app.get("/get-by-name")

def get_item(name:str):
    for item_id in inventory:
        if inventory[item_id].name == name:
            return inventory[item_id]
    
    return {"data": "not found."}


@app.post("/create-item/{item_id}")

def create_item(item_id: int, item: Item):
    if item_id in inventory:
         return {"Error": "Item exist"}
 
    inventory[item_id] = item
    
    return inventory[item_id]
    
    
@app.put("/update-item/{item_id}")

def update_item(item_id: int, item: UpdateItem):
    if item_id not in inventory:
        return {"Error": "Item does not exist"}
    
    # Update the item's fields if they are not None
    if item.price is not None:
        inventory[item_id].price = item.price
    if item.name is not None:
        inventory[item_id].name = item.name
    if item.brand is not None:
        inventory[item_id].brand = item.brand
    
    return inventory[item_id]


@app.delete("/delte-item")

def delte_item(item_id: int = Query(..., description= "The ID of the item to delete the item.")):
    if item_id not in inventory:
        return {"Error": "ID doesnot exist."}
    
    del inventory[item_id]
    return {"Success": "Item deleted."}