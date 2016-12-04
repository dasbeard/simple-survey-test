from flask import Flask, render_template, request, redirect, session, flash

app = Flask(__name__)
app.secret_key = "My secret key"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/getInfo', methods=['POST'])
def getInfo():
    # print "Got Info"
    session['local'] = request.form['dojoLocation']
    session['lang'] = request.form['favLanguage']
    if len(request.form['name'])<1:
        flash("Name cannot be blank!")
        return redirect('/')
    else:
        session['name'] = request.form['name']

    if len(request.form['comment'])<1:
        session['comment'] = "Hi there!!"
    elif len(request.form['comment'])>121:
        flash("Comments can only be 120 characters")
        return redirect('/')
    elif len(request.form['comment'])>1 and len(request.form['comment'])<121:
        session['comment'] = request.form['comment']


    return redirect('/results')

@app.route('/results')
def results():
    return render_template('results.html')




app.run(debug=True)
