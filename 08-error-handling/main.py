from fastapi import FastAPI, HTTPException

app = FastAPI(title="FastAPI Basics - Lesson 08")

@app.get("/items/{item_id}")
def get_item(item_id: int):
    if item_id != 1:
        raise HTTPException(status_code=404, detail=f"Item {item_id} was not found")
    return {"id": 1, "name": "Keyboard"}
