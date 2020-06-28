from flask import Flask,flash,render_template,url_for,session,request,redirect
from .forms import MainForm
from bhp import app
import json
import pickle
import numpy as np

@app.route('/predict',methods=['GET','POST'])
def predict():
    form=MainForm()
    cost=0
    if request.method=='POST':
        Total_sqft=float(form.Total_sqft.data)
        Bedroom=int(form.Bedroom.data)
        Bath=float(form.Bath.data)
        Balcony=int(form.Balcony.data)
        Area=form.Area.data.lower()
        data_column=None
        location=None
        model=None
        with open("bhp/columns.json", "r") as readit: 
            data_column = json.load(readit)['data_column']
        location=data_column[4:]
        if model is None:
            with open('banglore_home_prices_model.pickle','rb') as f:
                model=pickle.load(f)
        try:
            loc_index = data_column.index(Area.lower())
        except:
            loc_index = -1

        x = np.zeros(len(data_column))
        x[0] = Total_sqft
        x[3] = Bedroom
        x[2] = Balcony
        x[1] = Bath
        if loc_index>=0:
            x[loc_index] = 1

        cost=round(model.predict([x])[0],2)
        return render_template('HousePrice.html',form=form,cost=cost)

    return render_template('HousePrice.html',form=form,cost=cost)
