import flask
from flask import Flask, redirect, request, jsonify, render_template_string
from flask_cors import CORS

app = Flask(__name__)

CORS(app)

@app.route("/")
def Home():

    return """If you see this Message the API Server is Working! Check for the /api/links for more  Test
    Links
    """



    