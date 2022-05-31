- [What is flask?](#what-is-flask)
- [Writing first flask app](#writing-first-flask-app)
- [render_template](#render_template)
- [Jinja2](#jinja2)
- [Expressions in jinja2](#expressions-in-jinja2)
- [Data Structures in jinja 2](#data-structures-in-jinja-2)
- [If conditional in jinja](#if-conditional-in-jinja)
- [For loop in jinja 2](#for-loop-in-jinja-2)
- [Receiving data from html](#receiving-data-from-html)

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

### Data Structures in jinja 2

- We can pass the following as info to jinja2
  - tuple
  - list
  - dictionary
  - class

To render_template we can pass every variable as a separate value or as a object

**Eg html template**

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Data Structures in Jinja2</title>
</head>
<body>
    <div style="border: 2px; border-style: solid">
    <h2>Lists and tuples</h2>
    <p>From List</p>
    DC Characters are:
    <ul>
        <li>{{ list_example[0] }}</li>
        <li>{{ list_example[1] }}</li>
        <li>{{ list_example[2] }}</li>
    </ul>
    <p>From Tuple</p>
    Marvel Characters
    <ul>
        <li>{{ tuple_example[0] }}</li>
        <li>{{ tuple_example[1] }}</li>
        <li>{{ tuple_example[2] }}</li>
    </ul>
    </div>
    <div style="border: 2px; border-style: solid">
        Below are the details about superman
    <p>
        <ul>
            <li>city he lives in {{ dictionary_example["city"] }}</li>
            <li>His nemesis is {{ dictionary_example["Villain"] }}</li>
            <li>Works as {{ dictionary_example["job"] }}</li>
            <li>For news-paper {{ dictionary_example["new-paper"] }}</li>
        </ul>
    </p>
    </div>
    <div style="border: 2px; border-style: solid">
    <h4>Info on book from a class</h4>
    <p>
        <ul>
            <li>Title: {{ bookInfo.name }}</li>
            <li>Author: {{ bookInfo.author }}</li>
            <li>Version: {{ bookInfo.version }}</li>
        </ul>
    </div>

</body>
</html>
```

**Eg flask code**

```python
class appInfo:
    def __init__(self, name, version, author):
        self.name=name
        self.version=version
        self.author=author

list_example = [
"Superman",
"Flash",
"Arrow"
]

tuple_example = (
"Iron-man",
"Loki",
"Thor"
)

dictionary_example = {"city":"Metropolis", "Villain":"Lex","job": "reporter", "new-paper": "Daily-planet"}

bookInfo = appInfo("trojan horse", "1.0", "mark russanovich")

allInfoAsObject = {
    "list_example": list_example,
    "tuple_example": tuple_example,
    "dictionary_example": dictionary_example,
    "bookInfo": bookInfo
}

@app.route('/data')
def parsingDataStructures():
    return render_template('datastructures.html', **allInfoAsObject)
```

### If conditional in jinja

- We can parse if in jinja using the following syntax

```html
{% if state== 'AP' %}
<h1>Andhra Pradesh</h1>
{% elif state== 'TN' %}
<h1>Tamil Nadu</h1>
{% else %}
<h1>Unknown</h1>
{% endif %}
```

### For loop in jinja 2

- Used to iterate through list, tuple, set, dictionary

```html
Displaying list of dc characters from list: {% for character in dcCharacters %}
<li>{{ character }}</li>
{% endfor %} Displaying from dictionary: {% for key, value in
supermanData.items() %}
<li>{{ key }}: {{ value }}</li>
{% endfor %}
```

### Receiving data from html

- We make use of forms to get data back from html
- `action` attribute is added to form tag to specify the uri to which the form should return data
- `method` attribute is used to specify http method.
- `name` attribute should be mentioned for each field in form and value should be unique for it.
- data will be returned to python file, as a json where name of filed will be the key and value of the filed as its value.
- The json can be fetched by using the `request.form` attribute on python file.

Eg HTML:

```html
<form class="p-4 p-md-5 border rounded-3 bg-light" action="/" method="POST">
  <div class="form-floating mb-3">
    <input
      type="text"
      class="form-control"
      id="floatingInput"
      name="username"
      placeholder="Enter user name"
    />
    <label for="floatingInput">Username</label>
  </div>
  <div class="form-floating mb-3">
    <input
      type="password"
      class="form-control"
      name="password"
      id="floatingPassword"
      placeholder="Password"
    />
    <label for="floatingPassword">Password</label>
  </div>
  <button class="w-100 btn btn-lg btn-primary" type="submit">Sign up</button>
  <hr class="my-4" />
  <small class="text-muted"
    >By clicking Sign up, you agree to the terms of use.</small
  >
</form>
```

eg flask code:

```python
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)

username = ""

@app.route('/', methods=['GET','POST'])
def homePage():
    if request.method == 'POST':
        username = request.form['username']
        cred =  request.form['password']
        if (username == 'alpha' and cred == 'alpha'):
            return redirect('/dashboard')
        else:
            return render_template('home.html')
    else:
        return render_template('home.html')
```
