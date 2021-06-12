import random
from flask import Flask, render_template, redirect, request, session
app=Flask(__name__)

app.secret_key="shhhhhh, don't tell anyone"

@app.route('/')
def index():
    if 'gold' not in session:
        session['gold']=0
        session['message']=[]
    return render_template('index.html')


@app.route('/process_money', methods=['POST'])
def process_money():
    building=request.form['building']
    value=0
    if building=='farm':
        value=random.randint(10,20)
    elif building=='cave':
        value=random.randint(5,10)
    elif building=='house':
        value=random.randint(2,5)
    elif building=='casino':
        value=random.randint(-50,50)
    print(value)
    session['gold']+=value
    if value>=0:
        message='Earned '+str(value)+' gold from the '+building
        session['message']=[(1,message)]+session['message']
    else:
        message='Lost '+str(value)+' gold from the '+building
        session['message']=[(0,message)]+session['message']
    return redirect('/')

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')


if __name__=='__main__':
    app.run(debug=True)