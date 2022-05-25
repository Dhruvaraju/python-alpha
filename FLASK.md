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

### render_template

- For rendering larger html files we use render template
- import `render_template` from flask
- create a new folder under root of project named as `template`
- create all your html files in templates folder, as flask by default checks templates folder for html files.
- in the function now we can return render_template with html file name, example below

```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/fp')
def hello_world():
    return render_template('first_page.html')

@app.route('/sp')
def greet_user():
    return render_template('second_page.html')

```

### Jinja2

- A template language which is used to replace variables in string with syntactic sugar `{{ var_name }}`
- Jinja2 comes with flask by default.
- we need to place template variables in html and replace them in the functions

**html example**

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Jinja example</title>
  </head>
  <body>
    <h2>Hi {{ username }} !</h2>
    <p>This is an example for {{ framework }}</p>
  </body>
</html>
```

**jinja template replacement**

```python
@app.route('/jinja2')
def jinja2():
    return render_template('jinja2.html',username='dexter', framework='flask')
```

### Expressions in jinja2
- We can use interpolation for string replacement.
- Arithmetic operations on numbers can be done.
- String concatenation can be performed.
- When we have multiple variables that need to be replaced, we add them as a dictionary and replace them.
  
```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Expressions</title>
  </head>
  <body style="background-color: beige">
    <div style="border: 2px; border-style: solid">
      <h2>Hi {{ username }} !</h2>
      <p>This is an example for {{ framework }}</p>
    </div>
    <div style="border: 2px; border-style: solid">
      <p>We have {{ apple_count }} apples and {{ orange_count }} oranges</p>
      <p>We have a total of {{ apple_count + orange_count }} fruit.</p>
    </div>
    <div style="border: 2px; border-style: solid">
      <p>Serials to watch are {{ series01 + ' ' + series02}}</p>
    </div>
  </body>
</html>

```

```python
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
```