from flask import request, Response, Headers

from flask import Flask, request, jsonify



from flask import request, jsonify


import os


from flask import request




import shlex


from flask import Flask, render_template_string, request




from flask import Flask, request, jsonify, render_template_string

from flask import Flask, jsonify, request

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
import sqlite3


app = Flask(__name__)


@app.route("/")
def main_page():
    return "REST API"


@app.route("/user/<name>")
def user_page(name):
    conn = sqlite3.connect("database.db")
    cur = conn.cursor()

    cur.execute(f"SELECT * FROM users WHERE name = '{name}'")
    user = cur.fetchone()

    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404

    conn.close()


import sqlite3

app = Flask(__name__)

@app.route("/search_user", methods=["POST"])
def search_user():
    data = request.get_json()
    name = data["name"]

    con = sqlite3.connect("test.db")
    cur = con.cursor()
    cur.execute("select * from test where username = :name", {"name": name})
    data = str(cur.fetchall())
    con.close()
    return jsonify(data=data), 200


if __name__ == "__main__":
    app.run(debug=True)





@app.route("/welcome/<string:name>")
app = Flask(__name__)


@app.route("/welcome/<string:name>")
from flask import Flask, jsonify

app = Flask(__name__)


def welcome(name):
    data = f"Welcome {name}"
    return jsonify(data=data), 200


@app.route("/welcome2/<string:name>")
from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
from flask import Flask, jsonify

app = Flask(__name__)


from flask import Flask, jsonify

def welcome():
    name = "John Doe"
    data = {"message": f"Welcome {name}"}
    return jsonify(data)

def fix_subprocess(code):
    return code.replace("shell=True", "shell=False")

if __name__ == "__main__":
    app.run()





from flask import Flask, render_template_string, request

app = Flask(__name__)


@app.route("/")
from flask import Flask, render_template_string, request

app = Flask(__name__)


@app.route("/")
def hello_ssti():
    if request.args.get("name"):
        name = request.args.get("name")
        template = f"""
<div>
    <h1>Hello</h1>
    {name}
</div>
"""
        return render_template_string(template)


if __name__ == "__main__":
    app.run()





@app.route("/get_users")
import subprocess



from flask import request
import subprocess


def get_users():
    try:
        hostname = request.args.get("hostname")
        command = f"dig {hostname}"
        data = subprocess.check_output(command, shell=True)
        return data
    except:
        data = f"{hostname} username didn't found"
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
import subprocess

import os
import shlex
import subprocess



import os
import shlex
import subprocess
from flask import request, jsonify

import os
import shlex


app = Flask(__name__)

@app.route("/read-file", methods=["POST"])
def read_file():
    filename = request.args.get("filename")
    if not filename:
        return "Bad Request", 400

    file = open(filename, "r")
    data = file.read()
    file.close()

    # Don't allow subprocess commands
    if "os.system" in data or "subprocess." in data:
        return "Bad Request", 400

    # Use Python API for system commands
    with open("restapi.log", "w") as f:
        os.system(shlex.split(data.replace(" ", ""))[0])

    return jsonify(data=data), 200

if __name__ == '__main__':
    app.run(debug=True)







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
    headers["Content-Type"] = content_type
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
