from flask import Flask, jsonify, request
import requests 

app = Flask(__name__)

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


@app.route('/url_variables')
def url_variables():
    return jsonify(message='That resource does not exist'), 404


if __name__ == '__main__':
    app.run()