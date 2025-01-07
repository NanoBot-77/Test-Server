import flask
from flask import Flask, redirect, request, jsonify, render_template_string
from flask_cors import CORS
import random


app = Flask(__name__)

CORS(app)

@app.route("/")
def Home():

    return """If you see this Message the API Server is Working! Check for the /api/links for more  Test
    Links
    """


@app.route('/api/links')
def links():
    return jsonify({'links':{'about':'/api/about', "TestJson":"/api/TestJson"}})

@app.route('/api/about')
def About():
    return "This is a test Server  created on python Flask for Testing Nginx and duckdns"

@app.route('/api/TestJson')
def TestJson():
    R = random.randint(10, 200)
    return jsonify({'R_Data':R})
