# from flask import Flask, render_template, request, flash, redirect, url_for
# import requests
# import os
# app = Flask(__name__)
# app.secret_key = 'thisisjustarandomstring'
# def add(n1, n2):
#     return n1+n2
# def minus(n1, n2):
#     return n1-n2
# def multiply(n1, n2):
#     return n1*n2
# def divide(n1, n2):
#     if n2 == 0:
#         return "Undefined"
#     return n1/n2
# def fixVal(n):
#     try:
#         n = float(n)
#     except ValueError:
#     except (ValueError, TypeError):
#         n = 0
#     return n

# @app.route('/', methods=['POST', 'GET'])
# def index():
#     number_1 = fixVal(request.form.get("first"))
#     number_2 = fixVal(request.form.get('second'))
#     operation = request.form.get('operation')
#     result = 0
#     if operation == 'add':
#         result = add(number_1, number_2)
#     elif operation == 'minus':
#         result =  minus(number_1, number_2)
#     elif operation == 'multiply':
#         result = multiply(number_1, number_2)
#     elif operation == 'divide':
#         result = divide(number_1, number_2)
#     flash(f'The result of operation {operation} on {number_1} and {number_2} is {result}')
#     return render_template('index.html')
# if __name__ == '__main__':
#     app.run(
#         debug=True,
#         port=5050,
#         host="0.0.0.0"
#     )


from flask import Flask, render_template, request, flash, redirect, url_for

import requests
import os

app = Flask(__name__)
app.secret_key = 'thisisjustarandomstring'


def fixVal(n):
    try:
        n = float(n)
    except (ValueError, TypeError):
        n = 0.0
    return n

def call(port,x,y):
    req = requests.get(f'http://{request.remote_addr}:{port}/{abs(x)}/{abs(y)}/{int(x<0)}/{int(y<0)}').text.strip()
    return req

@app.route('/', methods=['POST', 'GET'])
def index():
    number_1 = fixVal(request.form.get("first"))
    number_2 = fixVal(request.form.get('second'))
    operation = request.form.get('operation')
    result = 0
    if operation == 'add':
        result = call(5051,number_1,number_2)
    elif operation == 'minus':
        result =  call(5052,number_1,number_2)
    elif operation == 'multiply':
        result = call(5053,number_1,number_2)
    elif operation == 'divide':
        result = call(5054,number_1,number_2)
    elif operation == 'equal':
        result = call(5055,number_1,number_2)
    elif operation == 'greater_than':
        result = call(5056,number_1,number_2)
    elif operation == 'less_than':
        result = call(5057,number_1,number_2)
    elif operation == 'modulus':
        result = call(5058,number_1,number_2)
    elif operation == 'exponent':
        result = call(5059,number_1,number_2)
    elif operation == 'GCD':
        result = call(5060,number_1,number_2)
    elif operation == 'LCM':
        result = call(5061,number_1,number_2)
    elif operation == 'AND':
        result = call(5062,number_1,number_2)
    elif operation == 'OR':
        result = call(5063,number_1,number_2)
    elif operation == 'XOR':
        result = call(5064,number_1,number_2)

    flash(f'The result of operation {operation} on {number_1} and {number_2} is {result}')

    return render_template('index.html')

if __name__ == '__main__':
    app.run(
        debug=True,
        port=5050,
        host="0.0.0.0"
    )
