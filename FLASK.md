### What is flask?

- Flask is a light weight WSGI application framework.
- A framework is a code library that allows us to write application code a bit more easily.
- Flask helps us build reliable, scalable, and maintainable web applications.
- Flask is known as a micro framework because it doesn't do much.
- It allows us to receive user data and send data back as per user requests.
- To install Flask run the below command

```
pip install flask
```

### Writing first flask app

- Generally a flask app is written in a file called app.py
- We need to import flask
- Pass the `__name__` an input parameter for flask app.
- Define app endpoints are routes.
- Then write a function to return information for the routes defined.

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'
```

- To run the app we need to set the FLASK_APP variable

```
export FLASK_APP=app.py #In a mac or linux based system
$env:FLASK_APP ="app.py" #In power shell
set FLASK_APP=app.py #In cmd.exe or windows machine command prompt
```

- We have to set flask environment also as

```
set FLASK_ENV=development
```

- To run a flask app we use

```
flask run
```

- It will start the app on `http://127.0.0.1:5000`
- Now we can access our routs by appending them towards the end.