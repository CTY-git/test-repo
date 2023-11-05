from werkzeug.security import check_password_hash

from flask import request, jsonify
import html


import os
from pathlib import Path




import json



from flask import request, render_template_string
import os, logging


import shlex


from html import escape


from django.utils.html import escape

from django.shortcuts import render
from django.http import JsonResponse

from flask import escape

from flask import render_template

from sqlalchemy import text
from flask import jsonify
import logging

from sqlalchemy import create_engine, text


from flask import Flask,jsonify,render_template_string,request,Response,render_template
import subprocess
from werkzeug.datastructures import Headers
from werkzeug.utils import secure_filename
import sqlite3


app = Flask(__name__)
app.config['UPLOAD_FOLDER']="/home/kali/Desktop/upload"
app.config['MAX_CONTENT_LENGTH'] = 16 * 1000 * 1000

@app.route("/")
def main_page():
    return "REST API"

@app.route("/user/<string:name>")
def search_user(name):
    engine = create_engine('sqlite:///test.db')
    with engine.connect() as connection:
        result = connection.execute(text("SELECT * FROM test WHERE username = :username"), {'username': name})
        data = result.fetchall()

    logging.basicConfig(filename="restapi.log", filemode='w', level=logging.DEBUG)
    logging.debug(str(data))

    return render_template('data.html', data=data)










@app.route("/welcome/<string:name>")
from django.shortcuts import render
from django.http import JsonResponse

def welcome(request, name):
    context = {"name": escape(name)}
    return render(request, 'welcome.html', context)

from django.utils.html import escape
from django.http import JsonResponse

def welcome_json(request, name):
    safe_name = escape(name)
    data = "Welcome %s" % safe_name
    return JsonResponse({'data': data}, safe=False)







@app.route("/welcome2/<string:name>")
The provided code doesn't seem to have any security issues related to the 'subprocess' function 'check_output' with 'shell=True' as mentioned in the reference. It's a simple function that escapes a given name and returns a welcome message. 

Here is the same code as there is nothing to fix:

```python
from flask import render_template

from werkzeug.utils import secure_filename

def welcome2(name):
    safe_name = secure_filename(name)
    return render_template('welcome.html', name=safe_name)

@app.route("/hello")




def hello_ssti():
    if request.args.get('name'):
        name = secure_filename(request.args.get('name'))
        template = f'''<div>
        <h1>Hello</h1>
        {name}
</div>
'''
        logging.basicConfig(filename="restapi.log", filemode='w', level=logging.DEBUG)
        logging.debug(str(template))
        return render_template_string(template)



@app.route("/get_users")
import shlex
from flask import jsonify

def get_users():
    try:
        hostname = request.args.get('hostname')
        command = shlex.split("dig " + hostname)
        data = subprocess.check_output(command, shell=False)
        return jsonify(json.loads(data.decode()))
    except:
        data = str(hostname) + " username didn't found"
        return jsonify(json.loads(data))





@app.route("/get_log/")
import subprocess
from flask import jsonify

import subprocess
from flask import jsonify

import shlex

def get_log():
    try:
        command=shlex.join(["cat", "restapi.log"])
        data=subprocess.check_output(command, shell=False)
        return data
    except:
        return jsonify(data="Command didn't run"), 200








@app.route("/read_file")
import logging

import os
from pathlib import Path

import logging


def read_file():
    filename = request.args.get('filename')
    if not filename:
        return "No filename provided", 400

    filename = os.path.basename(filename)
    filename = Path(filename).resolve(strict=True)

    if not os.path.isfile(filename):
        return "File does not exist", 404

    with open(filename, "r") as file:
        data = file.read()

    logging.basicConfig(filename="restapi.log", filemode='w', level=logging.DEBUG)
    logging.debug(html.escape(str(data)))

    return jsonify(data=data),200







@app.route("/deserialization/")
def deserialization():
    try:
        import socket, pickle
        HOST = "0.0.0.0"
        PORT = 8001
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((HOST, PORT))
            s.listen()
            connection, address = s.accept()
            with connection:
                received_data = connection.recv(1024)
                data=pickle.loads(received_data)
                return str(data)
    except:
        return jsonify(data="You must connect 8001 port"), 200


@app.route("/get_admin_mail/<string:control>")
def get_admin_mail(control):
    if control=="admin":
        data="admin@cybersecurity.intra"
        import logging
        logging.basicConfig(filename="restapi.log", filemode='w', level=logging.DEBUG)
        logging.debug(data)
        return jsonify(data=data),200
    else:
        return jsonify(data="Control didn't set admin"), 200

@app.route("/run_file")
def run_file():
    try:
        filename=request.args.get("filename")
        command="/bin/bash "+filename
        data=subprocess.check_output(command,shell=True)
        return data
    except:
        return jsonify(data="File failed to run"), 200

@app.route("/create_file")
def create_file():
    try:
        filename=request.args.get("filename")
        text=request.args.get("text")
        file=open(filename,"w")
        file.write(text)
        file.close()
        return jsonify(data="File created"), 200
    except:
        return jsonify(data="File didn't create"), 200


connection = {}
max_con = 50

def factorial(number):
    if number == 1:
        return 1
    else:
        return number * factorial(number - 1)


@app.route('/factorial/<int:n>')
def factroial(n:int):
    if request.remote_addr in connection:
        if connection[request.remote_addr] > 2:
            return jsonify(data="Too many req."), 403
        connection[request.remote_addr] += 1
    else:
        connection[request.remote_addr] = 1
    result=factorial(n)
    if connection[request.remote_addr] == 1:
        del connection[request.remote_addr]
    else:
        connection[request.remote_addr] -= 1
    return jsonify(data=result), 200


@app.route('/login',methods=["GET"])
from flask import request, jsonify


def login():
    username=request.args.get("username")
    passwd=request.args.get("password")
    hashed_passwd = 'pbkdf2:sha256:150000$cyber$abc123'
    if username == "anil" and check_password_hash(hashed_passwd, passwd):
        return jsonify(data="Login successful"), 200
    else:
        return jsonify(data="Login unsuccessful"), 403



@app.route('/route')
def route():
    content_type = request.args.get("Content-Type")
    response = Response()
    headers = Headers()
    headers.add("Content-Type", content_type)
    response.headers = headers
    return response

@app.route('/logs')
def ImproperOutputNeutralizationforLogs():
    data = request.args.get('data')
    import logging
    logging.basicConfig(filename="restapi.log", filemode='w', level=logging.DEBUG)
    logging.debug(data)
    return jsonify(data="Logging ok"), 200


@app.route("/user_pass_control")
def user_pass_control():
    import re
    username=request.form.get("username")
    password=request.form.get("password")
    if re.search(username,password):
        return jsonify(data="Password include username"), 200
    else:
        return jsonify(data="Password doesn't include username"), 200




@app.route('/upload', methods = ['GET','POST'])
def uploadfile():
   import os
   if request.method == 'POST':
      f = request.files['file']
      filename=secure_filename(f.filename)
      f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
      return 'File uploaded successfully'
   else:
      return '''
<html>
   <body>
      <form  method = "POST"  enctype = "multipart/form-data">
         <input type = "file" name = "file" />
         <input type = "submit"/>
      </form>   
   </body>
</html>


      '''



if __name__ == '__main__':
    app.run(host="0.0.0.0",port=8081)
