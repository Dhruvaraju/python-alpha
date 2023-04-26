from flask import Flask, request

app = Flask(__name__)

stores = [
    {
    "name": "my_store",
    "items": [
     {
    "name": "chair",
    "price": 27
     }
    ]
    }
]

@app.get("/store")
def get_stores():
    return {"stores": stores}

@app.post("/store")
def add_new_store():
    request_date = request.get_json()
    new_store = {"name": request_date["name"]}
    stores.append(new_store)
    return new_store, 201