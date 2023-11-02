



from subprocess import check_output, CalledProcessError, STDOUT


from subprocess import check_output, CalledProcessError

from os import system



from flask import Flask, render_template_string


import re



import shlex




import json
import socket
import pickle





from flask import Flask, render_template_string, request

from flask import Response, request





from flask import Flask, request, jsonify
from flask_cors import CORS


from flask import request





import os



from flask import Flask, render_template, request, jsonify


from flask import Flask, jsonify

from flask import Flask, jsonify, request

from flask import Flask, render_template

from flask import Flask
from flask import render_template

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
app = Flask(__name__)

@app.route("/")
def main_page():
    return render_template("main_page.html", title="REST API")

@app.route("/user/<name>")
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", title="Home")

@app.route("/user/<name>")
def user_page(name):
    return render_template("user_page.html", title=f"User {name}", name=name)

if __name__ == "__main__":
    app.run()



import sqlite3

app = Flask(__name__)

@app.route("/search_user/<username>", methods=["GET"])
def search_user(username):
    con = sqlite3.connect("test.db")
    cur = con.cursor()
    cur.execute("select * from test where username = ?" , (username,))
    data = str(cur.fetchall())
    con.close()
    return jsonify(data=data),200

if __name__ == "__main__":
    app.run()




@app.route("/welcome/<string:name>")
app = Flask(__name__)

@app.route("/welcome/<string:name>")
from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/welcome2/<string:name>")
app = Flask(__name__)


@app.route("/welcome/<name>")
def welcome(name):
    data = {"message": f"Welcome {name}"}
    return jsonify(data)


@app.route("/")
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()









@app.route("/hello")
app = Flask(__name__)


from flask import Flask, render_template_string, request

app = Flask(__name__)

@app.route('/')
def hello_ssti():
    if request.args.get('name'):
        name = request.args.get('name')
        template = f'''\
<div>
<h1>Hello</h1>
{name}
</div>
'''
        return render_template_string(template)
    else:
        return 'No name provided'

if __name__ == '__main__':
    app.run()



@app.route("/hello_ssti", methods=['GET'])
def hello_ssti_route():
    return hello_ssti()


@app.route("/get_users", methods=['GET'])
import subprocess

app = Flask(__name__)


@app.route("/")
def index():
    users = subprocess.run(["ls", "/home"], stdout=subprocess.PIPE).stdout.decode().split('\n')
    template = f"""
<div>
<h1>Users</h1>
{users}
</div>
"""
    return render_template_string(template)


if __name__ == "__main__":
    app.run()



import subprocess
from flask import request


def get_users():
    try:
        hostname = request.args.get('hostname')
        command = ["dig", hostname]
        data = subprocess.run(
            command, stdout=subprocess.PIPE, check=True,
            encoding='utf-8', errors='strict'
        ).stdout
        return data
    except subprocess.CalledProcessError as e:
        data = f"{hostname} username didn't found: {e}"
        return data







@app.route("/get_log/")
def get_log():
    try:
        command="cat restapi.log"
        data=subprocess.check_output(command,shell=True)
        return data
    except:
        return jsonify(data="Command didn't run"), 200


@app.route("/read_file")
import os



app = Flask(__name__)
CORS(app)

@app.route("/read_file", methods=['GET'])
import os
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/read-file", methods=["GET"])
import os
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/read-file", methods=["GET"])
import os
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/read_file", methods=["GET"])
import os
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/read_file", methods=["POST"])
from flask import Flask, request, jsonify
import os

app = Flask(__name__)


@app.route("/read_file", methods=["GET"])
from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route("/read", methods=["POST"])
def read_file():
    filename = request.args.get("filename")
    if not filename:
        return jsonify({"error": "filename parameter is required"}), 400
    if not os.path.exists(filename):
        return jsonify({"error": "file does not exist"}), 404
    try:
        with open(os.path.abspath(filename), "r") as file:
            data = file.read()
        return jsonify(data=data), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='127.0.0.1', port=port)









@app.route("/deserialization/")
import socket
import json

import socket
import json

import socket
import json



import json
import socket

import socket
import json

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
                data = json.loads(received_data.decode())
                return data
    except:
        return {"data": "You must connect 8001 port"}, 200


@app.route("/get_admin_mail/<string:control>")
from flask import Flask, jsonify


app = Flask(__name__)

@app.route("/admin_mail", methods=["GET"])
from flask import Flask, jsonify, request


app = Flask(__name__)


@app.route("/get_admin_mail", methods=["GET"])
import shlex
from subprocess import check_output, CalledProcessError
from flask import Flask, jsonify


app = Flask(__name__)


import os
import shlex

from flask import Flask, jsonify

app = Flask(__name__)


from subprocess import check_output, CalledProcessError
from flask import Flask, jsonify
import shlex


app = Flask(__name__)


@app.route("/admin/mail", methods=["GET"])
import os
import shlex
from subprocess import check_output, CalledProcessError, STDOUT
from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/get_admin_mail", methods=["GET"])
def get_admin_mail():
    control = "admin"

    if control == "admin":
        try:
            data = check_output(shlex.split("whoami"), stderr=STDOUT)
            return jsonify(data=data.decode("utf-8"))
        except CalledProcessError as e:
            return jsonify(data=f"Error while getting admin mail: {e}")
    else:
        return jsonify(data="Control didn't set admin")


if __name__ == "__main__":
    app.run(debug=True)








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
def user_pass_control():
    if request.method == 'POST':
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')
        if username == 'test' and password == 'test':
            return jsonify(message="Login successful"), 200
        else:
            return jsonify(message="Login failed"), 401
    else:
        return jsonify(message="Method not allowed"), 405


@app.route("/")
def index():
    return "Hello World!"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)


@app.route("/user_pass_control", methods=["POST"])
def user_pass_control():
    username = request.form.get("username")
    password = request.form.get("password")
    if not re.search(username, password):
        return jsonify(data="Password include username"), 200
    else:
        return jsonify(data="Password doesn't include username"), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)






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
