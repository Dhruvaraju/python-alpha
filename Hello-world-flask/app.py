from flask import Flask, render_template 

app = Flask(__name__)

@app.route('/fp')
def hello_world():
    return render_template('first_page.html')

@app.route('/sp')
def greet_user():
    return render_template('second_page.html')
    
@app.route('/jinja2')
def jinja2():
    return render_template('jinja2.html',username='dexter', framework='flask')

userInfo ={
    "username": "dexter",
    "framework": "flask",
    "apple_count": 10,
    "orange_count": 20,
    "series01": "dexter",
    "series02": "flash",
}

@app.route('/express/')
def express():
    return render_template('expressions.html', **userInfo)