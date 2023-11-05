import json
from django.http import HttpRequest
from django.shortcuts import render
from django.utils.html import escape
import logging
import shlex
import subprocess
from flask import jsonify
import shlex
import sqlite3
from flask import jsonify
import logging
import shlex
import json
from io import BytesIO
import sqlite3
import logging
from flask import Flask, jsonify, render_template_string, request
from django.utils.html import escape
from django.shortcuts import render
from django.http import HttpRequest
from werkzeug.utils import secure_filename
from pathlib import Path
import os
import subprocess
from werkzeug.datastructures import Headers
import socket
from io import BytesIO
import pickle
from flask import jsonify
from flask import jsonify
import shlex
import socket, pickle
from flask import jsonify
app = Flask(__name__)
app.config['UPLOAD_FOLDER']="/home/kali/Desktop/upload"
app.config['MAX_CONTENT_LENGTH'] = 16 * 1000 * 1000


@app.route("/")
def main_page():
    return "REST API"

@app.route("/user/<string:name>")
def search_user(name):
    con = sqlite3.connect("test.db")
    cur = con.cursor()
    safe_name = shlex.quote(name)
    cur.execute("select * from test where username = ?", (safe_name,))
    data = cur.fetchall()
    con.close()
    logging.basicConfig(filename="restapi.log", filemode='w', level=logging.DEBUG)
    logging.debug(str(data))
    return jsonify(data), 200







@app.route("/welcome/<string:name>")
def welcome(name):
    safe_name = shlex.quote(name)
    data="Welcome "+safe_name
    return jsonify(data=data),200


@app.route("/welcome2/<string:name>")
def welcome2(name):
    data="Welcome "+name
    return data

@app.route("/hello")
def hello_ssti(request: HttpRequest):
    if 'name' in request.GET:
        name = escape(request.GET['name'])
        context = {'name': name}
        logging.basicConfig(filename="restapi.log", filemode='w', level=logging.DEBUG)
        logging.debug('Name: %s', escape(name))
        return render(request, 'hello.html', context)







@app.route("/get_users")
def get_users():
    try:
        hostname = request.args.get('hostname')
        command = "dig " + hostname
        data = subprocess.check_output(command, shell=True)
        return data
    except:
        data = str(hostname) + " username didn't found"
        return data

@app.route("/get_log/")
def get_log():
    try:
        command = shlex.escape("cat restapi.log")
        data = subprocess.check_output(shlex.split(command), shell=False)
        return data
    except:
        return jsonify(data="Command didn't run"), 200




@app.route("/read_file")
def read_file():
    filename = request.args.get('filename')
    filename = secure_filename(filename)
    file_path = os.path.abspath(filename)
    with open(file_path, "r") as file:
        data = file.read()
    logging.basicConfig(filename="restapi.log", filemode='w', level=logging.DEBUG)
    logging.debug(str(data))
    return jsonify(data=data),200


@app.route("/deserialization/")
def deserialization():
    try:
        HOST = "0.0.0.0"
        PORT = 8001
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((HOST, PORT))
            s.listen()
            connection, address = s.accept()
            with connection:
                received_data = connection.recv(1024)
                buffer = BytesIO(received_data)
                data = pickle.loads(buffer.read())
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
        filename = secure_filename(filename)
        filename = Path(os.path.abspath(filename))
        command="/bin/bash "+str(filename)
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
def login():
    username=request.args.get("username")
    passwd=request.args.get("password")
    if "anil" in username and "cyber" in passwd:
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
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        filename = secure_filename(f.filename)
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
    app.run(debug=True)

