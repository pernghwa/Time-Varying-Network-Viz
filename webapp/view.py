import os, sys, json, pickle
from flask import render_template, request, jsonify
from webapp import app

@app.route('/')
def index():
	return render_template("network.html")