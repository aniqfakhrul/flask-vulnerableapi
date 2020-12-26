#!/usr/bin/env python3
from flask import Flask,request
import jwt
import os
import subprocess

from jwt import InvalidSignatureError

app = Flask(__name__)

@app.route('/')
def index():
    return """
    <h1>Monitoring API is still in development</h1>
    <!-- nick please fix the code in the backend -->
    """

@app.route('/monitoring')
def main():
    secret = "Thank you for attempting this challenge" # make sure to exclude this in the commits
    auth_header = request.headers.get('Authorization')
    if auth_header:
        try:
            token = auth_header.split(" ")[1]
            arg = jwt.decode(token,secret,algorithms='HS256')['cmd']
            response = ParseLog(arg)
        except InvalidSignatureError:
            response = {
                'status': 'fail',
                'message': 'Bearer token malformed.'
            }
    else:
        response = {
            'status':'Error',
            'message':'No token provided'
        }
    return response

# coding skiils needed to be more
def ParseLog(arg):
    if ' ' in arg:
        response = 'Go away hacker!'
    else:
        response = subprocess.Popen(['sh','-c',arg],stdout=subprocess.PIPE).communicate()[0]
        if not response:
            response = "No Results"
    return response

if __name__=="__main__":
    app.run(debug=False)