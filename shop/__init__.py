from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = '6ad8fdbb56094336ac8ad611016d4b6d315d85ccd61b3059'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://c1847641:x516xx@csmysql.cs.cf.ac.uk:3306/c1847641'

db = SQLAlchemy(app)
db.init_app(app)

from shop import routes
from shop.models import User, Record, Cart
