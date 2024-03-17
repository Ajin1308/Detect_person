from flask import Flask, render_template, request, redirect, url_for, Response, jsonify
import mysql.connector
import cv2
import os
import base64
# import sys
# sys.path.append(r'C:\Users\AJIN\Detect_person')

from utils.utils import *

app = Flask(__name__)


@app.route('/')
def main():
    return render_template('index.html')

@app.route('/upload', methods =['GET','POST'])
def upload():
    if request.method == 'POST':
        name = request.form['name'] 
        address = request.form['address']
        phone = request.form['phone']
        image = request.files['image'].read()
        
        db = mysql_connect()
        cursor = db.cursor()
        sql = "INSERT INTO persons (name, address, phone, image) VALUES (%s, %s, %s, %s)"
        cursor.execute(sql, (name, address, phone, image))
        db.commit()
        cursor.close()

        image_data = base64.b64encode(image).decode('utf-8')

        details = {'name': name, 'address': address, 'phone': phone, 'image': image_data}
        return render_template('upload.html', details=details)

    return render_template('upload.html')


@app.route('/face', methods = ['GET','POST'])
def face():
    return render_template('face.html')

@app.route('/start_camera')
def start_camera():
    return Response(run_all(), mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/admin')
def admin():
    db = mysql_connect()
    cursor = db.cursor()
    cursor.execute("SELECT id, name, address, phone, image FROM persons")
    results = cursor.fetchall()
    cursor.close()

    return render_template('admin.html', results=results)



if __name__ == '__main__':
    app.run(debug=True)