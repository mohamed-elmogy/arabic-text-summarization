from flask import Flask
from flask_bcrypt import Bcrypt


app = Flask(__name__)
app.config['SECRET_KEY'] = '0b1e67116979247ac1decb41e93a5c8c'
bcrypt = Bcrypt(app)

from app import routes
