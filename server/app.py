#!/usr/bin/env python3

# from flask import Flask

# app = Flask(__name__)

# @app.route('/')
# def index():
#     return'<h1>Welcome</h1>'


# if __name__ == '__main__':
#     app.run(port=5555, debug=True)

from flask import Flask

app = Flask(__name__)

# Route for the index page
@app.route('/')
def index():
    return "<h1>Python Operations with Flask Routing and Views</h1>"

# Route for the print_string view
# @app.route('/print/<string:str_param>')
# def print_string(str_param):
#     print(str_param)
#     return f"<p>Printed: {str_param}</p>"
@app.route('/print/<string:str_param>')
def print_string(str_param):
    print(str_param)
    return str_param  # Return only the string

# Route for the count view
@app.route('/count/<int:num_param>')
def count(num_param):
    numbers = "\n".join(map(str, range(num_param)))
    return numbers  # Return numbers as plain text


# Route for the math view
@app.route('/math/<float:num1>/<operation>/<float:num2>')
def math(num1, operation, num2):
    result = None
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        if num2 != 0:
            result = num1 / num2
        else:
            return "Division by zero is not allowed"

    if result is not None:
        return str(result)  # Return the result as a string
    else:
        return "Invalid operation"


if __name__ == '__main__':
    app.run(port=5555, debug=True)