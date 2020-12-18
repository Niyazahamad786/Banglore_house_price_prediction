from flask import Flask,flash,render_template,url_for,session,request,redirect
from .forms import MainForm
from bhp import app
import json
import pickle
import numpy as np

@app.route('/',methods=['GET','POST'])
def predict():
    form=MainForm()
    cost=0
    if request.method=='POST':
        Total_sqft=float(form.Total_sqft.data)
        Bedroom=int(form.Bedroom.data)
        Bath=float(form.Bath.data)
        Area=form.Area.data.lower()
        data_column=None
        model=None
        with open("Model/columns.json", "r") as readit: 
            data_column = json.load(readit)['data_columns']
        if model is None:
            with open('Model/banglore_home_prices_model.pickle','rb') as f:
                model=pickle.load(f)
        try:
            loc_index = data_column.index(Area.lower())
        except:
            loc_index = -1

        x = np.zeros(len(data_column))
        x[0] = Total_sqft
        x[1] = Bath
        x[2] = Bedroom
        if loc_index>=0:
            x[loc_index] = 1

        cost=round(model.predict([x])[0],2)
        return render_template('HousePrice.html',form=form,cost=cost)

    return render_template('HousePrice.html',form=form,cost=cost)
