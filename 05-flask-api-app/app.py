from flask import Flask, request
from db import epic, user_stories
import uuid
from flask_smorest import abort

app = Flask(__name__)

@app.get("/epic")
def get_stores():
    return epic, 200


@app.post("/epic")
def add_new_epic():
    request_date = request.get_json()
    epic_id = uuid.uuid4().hex
    new_epic = {**request_date, "id": epic_id}
    epic[epic_id]=new_epic
    return new_epic, 201

@app.get("/epic/<string:epic_id>")
def get_specific_epic(epic_id):
    try:
        return epic[epic_id]
    except KeyError:
        # Flask smorest internally calls the flask abort method
        abort(404, message="Epic Not Found!!")

@app.get("/user_stories")
def get_user_stories():
    return user_stories, 200

@app.post("/user_stories")
def create_new_user_story():
    request_data = request.get_json()
    new_user_story = {}
    user_story_id = uuid.uuid4.hex
    if "epic_id" in request_data:
        new_user_story = {**request_data, "id": user_story_id}
        user_stories[user_story_id]= new_user_story
        return new_user_story
    else:
        abort(404, message="Choose a valid Epic.")