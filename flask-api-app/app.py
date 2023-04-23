from flask import Flask

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