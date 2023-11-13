#!/usr/bin/env python3

from flask import Flask,jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route("/print/<parameter>")
def printroute(parameter):
    print(parameter)
    return parameter

@app.route('/count/<parameter>')
def count(parameter):
    c = ""
    for x in range(int(parameter)):
        c += f'{x}\n'
    return c

@app.route('/math/<num1>/<operation>/<num2>')
def math(num1,operation,num2):
    n1 = int(num1)
    n2 = int(num2)
    if(operation == "+"):
        return str(n1 + n2)
    elif operation == "-":
        return str(n1-n2)
    elif operation == "*":
        return str(n1*n2)
    elif operation == "div":
        return str(n1/n2)
    elif operation == "%":
        return str(n1 % n2)
    return 404

if __name__ == '__main__':
    app.run(port=5555, debug=True)
