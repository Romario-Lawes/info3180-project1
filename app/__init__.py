from flask import Flask
from flask_sqlalchemy import SQLAlchemy

UPLOAD_FOLDER = './app/static/uploads'

app = Flask(__name__)
app.config['SECRET_KEY'] = "$3KRET"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://project1:project1@localhost/project1"
# app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://mwneuvcncwhzor:2990fb67f2ac8546943008e253a025c0f5acbcc2929977ac912dd653b1a84011@ec2-54-235-146-51.compute-1.amazonaws.com:5432/d9cvq1m78bnaor"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True 

db = SQLAlchemy(app)

app.config.from_object(__name__)
from app import views
