from flask import Flask, render_template, request , flash , Markup , send_file
import flask
import os
import shutil
import csv
from fpdf import FPDF
import datetime
from datetime import datetime
from datetime import date
import backend_data_1
import help
app = Flask(__name__)

@app.route('/')
def get():
    z=1
    if z==1:
        z=1
    return render_template('index.html')

app.secret_key= b'Prasanth@77777'

@app.route("/all" , methods=["POST","GET"])
def generate_all():
    if flask.request.method=='POST':
        backend_data_1.storer_1()

    backend_data_1.function_2()
    return render_template("index.html")



@app.route("/Range" ,methods=['POST' , "GET"])
def generating_marksheet():
    return help.function_1()






@app.route("/data" , methods=["POST", "GET"])
def backend_data():
    backend_data_1.storer()
    if flask.request.method == 'POST':
        return backend_data_1.function()





if __name__ == '__main__':
    app.run(debug=True)



