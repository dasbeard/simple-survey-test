from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "My secret key"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/getInfo', methods=['POST'])
def getInfo():
    print "Got Info"
    session['name'] = request.form['name']
    session['local'] = request.form['dojoLocation']
    session['lang'] = request.form['favLanguage']
    session['comment'] = request.form['comment']

    return redirect('/results')

@app.route('/results')
def results():
    return redirect('/')




app.run(debug=True)
