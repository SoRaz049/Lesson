from fastapi import FastAPI, Path

app  = FastAPI()

inventory = {
        1:{
            "name": "milk",
            "price": 2.11,
            "brand": "regular"
        }
    }

@app.get("/get-item/{item_id}")

def get_item(item_id : int = Path(..., description="The ID of the item you like to view.")):
    return inventory[item_id]

@app.get("/get-by-name")

def get_item(name:str):
    for item_id in inventory:
        if inventory[item_id]["name"] == name:
            return inventory[item_id]
    
    return {"data": "not found."}


 