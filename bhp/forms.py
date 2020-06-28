from flask_wtf import FlaskForm
#from flask_wtf.file import FileField,FileAllowed
from wtforms import  SubmitField,SelectField,FloatField
from wtforms.validators import DataRequired,Length



class MainForm(FlaskForm):
    
    
    lis=[]
    import json
    with open("bhp/columns.json", "r") as readit: 
        x = json.load(readit)['data_column'][4:]
        
        for i in  x:
            i=i.upper()
            lis.append((i,i))
    
    Total_sqft=FloatField('Total Sqft*',validators=[DataRequired(), Length(min=2, max=6)])
    Bedroom=SelectField('Bedroom*',validators=[DataRequired()], choices=[('0','None'),('1','1'),('2','2'),('3','3'),('4','4'),('5','5'),('6','6'),('7','7'),('8','8')])
    Bath=SelectField('Bath*',validators=[DataRequired()], choices=[('0','None'),('1','1'),('2','2'),('3','3'),('4','4'),('5','5'),('6','6'),('7','7'),('8','8'),('9','9'),('10','10')])
    Balcony=SelectField('Balcony*',validators=[DataRequired()], choices=[('0','None'),('1','1'),('2','2'),('3','3'),('4','4')])
    Area=SelectField('Area*',validators=[DataRequired()], choices=lis)
    Submit = SubmitField('Predict')
