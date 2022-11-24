# Import flask module
from typing import List, Dict
from flask import Flask
from flask import jsonify
import mysql.connector
import json
from flask import Flask, flash, request, redirect, url_for, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return test_table()

@app.route('/display')
def display_video():
	#print('display_video filename: ' + filename)
	return "<video autoplay=\"autoplay\" controls=\"controls\" preload=\"preload\"> <source src=\"" + url_for('display_video', filename="Vid.mp4")+"\" type=\"video/mp4\"></source>\</video>"

def test_table() -> List[Dict]:
    config = {
        'user': 'root',
        'password': 'Pass',
        'host': 'mysql',
        'port': '3306',
        'database': 'SQLDB'
    }
          
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM SQLTABLE')
    results = ""
    for (name, color) in cursor:
        results = results + "<img src=\"" + str(color) + "\"></img>"
    results = results +"<iframe src=\"https://www.youtube.com/embed/POda_-GV0QA\" width=\"853\" height=\"480\" frameborder=\"0\" allow=\"accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture\"></iframe>"

    cursor.close()
    connection.close()
    return results
    

# main driver function
if __name__ == "__main__":
    #app.run(ssl_context=("cert.pem", "key.pem"))
    app.run(host='0.0.0.0',ssl_context='adhoc')
