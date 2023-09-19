#!/usr/bin/env python3

from flask import Flask

app = Flask(name)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<parameter>')
def print_parameter(parameter):
    print(parameter)
    return parameter

@app.route('/count/<int:parameter>')
def count_parameter(parameter):
    count_list = [str(i) for i in range(parameter)]
    return '\n'.join(count_list) + '\n'  

@app.route('/math/<int:num1>/<operation>/<int:num2>')
def math_operations(num1, operation, num2):
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        result = num1 / num2
    elif operation == '%':
        result = num1 % num2
    else:
        return 'Invalid operation'
    return str(result)

if name == 'main':
    app.run(port=5555, debug=True)