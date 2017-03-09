from flask import Flask , render_template, request, redirect, session, flash
import random

app=Flask(__name__)
app.secret_key='secret'

@app.route('/')
def index():
    if 'message' not in session:
        session["message"]=""
    if 'number' not in session:
        session['number']=random.randrange(1,101)
    return render_template("index.html", message=session['message'] )

@app.route('/guess', methods=['POST'])
def guess():

    guess=int(request.form['number'])
    if guess== session['number']:
        session['message']= "you win!"
    if guess > session['number']:
        session['message']= 'Too high guess lower'
    elif guess< session['number']:
        session['message']= 'Too low guess higer'
    return redirect('/')
@app.route('/reset')
def reset():
    session['number']
    session.pop("number")
    session.pop("message")
    return redirect('/')
app.run(debug=True)
