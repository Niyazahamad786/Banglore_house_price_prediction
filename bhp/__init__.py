from flask import Flask
app = Flask(__name__)
app.config['SECRET_KEY']='heelo therer'

from bhp  import routes