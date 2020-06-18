from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, String, Text, Binary, Column
import os

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'planets.db')


db = SQLAlchemy(app)

@app.route('/')
def hello_world():
    return jsonify('Buyaka wwwwoi') 


@app.route('/super_simple')
def super_simple():
    return jsonify(message='Hello from the planetary API'), 200

@app.route('/not_found')
def not_found():
    return jsonify(message='That resource does not exist'), 404


@app.route('/parameters')
def parameters():
    name = request.args.get('name')
    age = int(request.args.get('age'))
    if age < 18:
        return jsonify(message="Sorry " + name + ", You are not old enough."), 401
    else:
        return jsonify(message="Welcome " + name + ", to planetary.")


@app.route('/url_variables/<string:name>/<int:age>')
def url_variables(name: str, age:int):
    if age < 18:
        return jsonify(message="Sorry " + name + ", You are not old enough."), 401
    else:
        return jsonify(message="Welcome " + name + ", to planetary.")



# Data Models
class User(db.Model):
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column()


if __name__ == '__main__':
    app.run()