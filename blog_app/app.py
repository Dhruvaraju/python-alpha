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

@app.route('/dashboard', methods=['GET','POST'])
def dashboard():
    if request.method == 'POST':
        if(request.form is not None):
            return redirect('/')
        return render_template('dashboard.html',username=username)
    return render_template('dashboard.html', username=username)