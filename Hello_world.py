from flask import Flask

app=Flask(__name__)

@app.route('/')
def home():
    return ('Hey Rajinikanth!')


@app.route('/Login')
def login():
    return('Welcome! please login')

@app.route('/ContactUs')
def contactus():
    return('Please create an INC to reach us')


app.run(debug=True)