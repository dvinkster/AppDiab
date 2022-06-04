# from cgitb import html
# from crypt import methods
# from urllib import request
# from unittest import result
from flask import Flask, render_template, request
import joblib

app=Flask(__name__)
load_model=joblib.load('modelDiabetic.pkl')

@app.route('/')
def default():
    return render_template('homepage.html')

@app.route('/homepage')
def home():
    return render_template('homepage.html')

@app.route('/predict', methods=['POST'])
def predict():
    # return render_template('homepage.html')#('default')
    preg = int(request.form.get('preg'))
    plas = int(request.form.get('plas'))
    pres = int(request.form.get('pres'))
    skin = int(request.form.get('skin'))
    test = int(request.form.get('test'))
    mass = int(request.form.get('mass'))
    pedi = int(request.form.get('pedi'))
    age = int(request.form.get('age'))

    print(preg)
    prediction=load_model.predict([[preg,plas,pres,skin,test,mass,pedi,age]])
    # prediction=load_model.predict([[0,0,30,50,7,60,7,8]])

    if prediction[0]==1:
        print('Diabetic')
        result='Diabetic'
    else:
        print('Not Diabetic')
        result='Not Diabetic'

    return render_template('result.html', value=result)

if __name__=='__main__':
    app.run(debug=True)