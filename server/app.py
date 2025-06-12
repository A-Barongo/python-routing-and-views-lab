#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<parameter>')
def print_text(parameter):
    print(parameter)
    return (f'{parameter}')


@app.route('/count/<parameter>')
def count(parameter):
    try:
        num = int(parameter)
        result = ''
        for n in range(num):
            result += f'{n}\n'
        return result
    except ValueError:
        result = ''
        for char in parameter:
            result += f'{char}\n'
        return result

    
@app.route('/math/<int:num1>/<op>/<int:num2>')
def math(num1,num2,op):
    
    if op=="+":
        result=num1+num2
    elif op=="-":
        result=num1-num2
    elif op=="*":
        result=num1*num2
    elif op=="div":
        result=num1/num2
    elif op == '%':
        result = num1 % num2
    else:
        return "Enter either +,-,* or div as your operations"
    return str(result)
if __name__ == '__main__':
    app.run(port=5555, debug=True)
