from flask import Flask, render_template 

class appInfo:
    def __init__(self, name, version, author):
        self.name=name
        self.version=version
        self.author=author

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

@app.route('/if')
def ifUsage():
    return render_template('if.html', state="TN")

@app.route('/for')
def forUsage():
    return render_template('for.html', dcCharacters=list_example, supermanData = dictionary_example)

