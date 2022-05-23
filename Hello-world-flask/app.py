from flask import Flask 

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/greet')
def greet_user():
    return """
    <html>
    <h2> Hello User!</h2
    <p> Welcome to the website </p>
    </html>
    """