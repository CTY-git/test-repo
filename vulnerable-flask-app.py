import re





import socket
import pickle
from subprocess import check_output

import socket, pickle






from flask import request




from flask import Response, request



from flask import Flask, jsonify, request

import os
from flask import Flask, request, jsonify






from flask import Flask, render_template_string, request

import shlex







from flask import Flask, jsonify, render_template

import logging

from flask import Flask, jsonify

from flask import jsonify

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
import sqlite3


import sqlite3

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello, world!"

@app.route("/search_user/<name>")
import sqlite3

from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/user/<username>")
import sqlite3
import logging


app = Flask(__name__)

@app.route("/search_user/<username>")
def search_user(username):
    con = sqlite3.connect("test.db")
    cur = con.cursor()
    cur.execute("select * from test where username = ?", (username,))
    data = cur.fetchall()
    con.close()
    logging.basicConfig(filename="restapi.log", filemode='w', level=logging.DEBUG)
    logging.debug(data)
    return jsonify(data=data), 200

if __name__ == "__main__":
    app.run()






@app.route("/welcome/<string:name>")
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/welcome/<string:name>")
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
from flask import Flask, jsonify, render_template

app = Flask(__name__)


@app.route('/')
from flask import Flask, jsonify

app = Flask(__name__)


def welcome():
    name = "John Doe"
    data = {"message": f"Welcome {name}"}
    return jsonify(data)


if __name__ == '__main__':
    app.run()




@app.route("/welcome2/<string:name>")
import subprocess

def welcome2(name):
    data = f"Welcome {shlex.escape(name)}"
    return data





@app.route("/hello")
app = Flask(__name__)


@app.route('/')
from flask import Flask, render_template_string, request

app = Flask(__name__)


@app.route('/')
from flask import Flask, render_template_string, request

app = Flask(__name__)


@app.route('/')
def hello_ssti():
    name = request.args.get('name')
    return render_template_string(f"""
<div>
    <h1>Hello</h1>
    {name}
</div>
""")


if __name__ == '__main__':
    app.run()




@app.route("/get_users")
import subprocess

import subprocess



import subprocess
from flask import request


def get_users():
    try:
        hostname = request.args.get('hostname')
        command = ["dig", hostname]
        data = subprocess.check_output(command, shell=False)
        return data
    except Exception as e:
        data = f"{hostname} username didn't found"
        return data






@app.route("/get_log/")
def get_log():
    return jsonify({"data": get_users()})


def get_log():
    command = "cat restapi.log"
    try:
import os
import subprocess
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/run_command", methods=["POST"])
def run_command():
    command = request.json.get("command")
    try:
        data = subprocess.check_output(command, shell=True)
        return data
    except:
        return jsonify(data="Command didn't run"), 200


@app.route("/read_file", methods=["GET"])
def read_file():
    file_path = request.args.get("file_path")
    if not file_path:
        return jsonify(data="No file path provided"), 400

    if not os.path.exists(file_path):
        return jsonify(data=f"File path '{file_path}' does not exist"), 404

    try:
        with open(file_path, "r") as file:
            data = file.read()
            return data
    except Exception as e:
        return jsonify(data=f"Failed to read file '{file_path}': {e}"), 500




@app.route("/read_file", methods=["POST"])
import os
from flask import Flask, request, jsonify

app = Flask(__name__)


def read_file():
    filename = request.args.get("filename")
    if not os.path.exists(filename):
        return jsonify(error="File does not exist"), 404
    with open(filename, "r") as file:
        data = file.read()
    return jsonify(data=data), 200


@app.route("/read_file", methods=["GET"])
def read_file():
    return read_file()


if __name__ == "__main__":
    app.run()









@app.route("/deserialization/")
import socket
import pickle
import shlex

import socket
import pickle
import os


def deserialization():
import socket
import pickle
import os

HOST = "0.0.0.0"
PORT = 8001

import socket
import pickle

HOST = "0.0.0.0"
PORT = 8080

def handle_client(conn, addr):
    with conn:
        print("Connected by", addr)
        data = conn.recv(1024)
        if not data:
            return
        data = pickle.loads(data)
        response = str(data)
        conn.sendall(response.encode())

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print(f"Listening on {HOST}:{PORT}")
    while True:
        conn, addr = s.accept()
        print(f"Connected by {addr}")
        try:
            handle_client(conn, addr)
        except Exception as e:
            print(f"Error occurred: {e}")
        finally:
            conn.close()








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
    response.headers["Content-Type"] = content_type
    return response


@app.route('/logs')
def ImproperOutputNeutralizationforLogs():
    data = request.args.get('data')
    import logging
    logging.basicConfig(filename="restapi.log", filemode='w', level=logging.DEBUG)
    logging.debug(data)
    return jsonify(data="Logging ok"), 200


@app.route("/user_pass_control")
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/")
def index():
    return "<h1>Hello, world!</h1>"


@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")
    if re.search(username, password):
        return jsonify(data="Password include username"), 200
    else:
        return jsonify(data="Password doesn't include username"), 200


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")





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
