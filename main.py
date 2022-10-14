import subprocess
from flask import Flask


def start():
    pid = str(subprocess.Popen(
        "ssh -D 0.0.0.0:1080 YOUR_HOST_ADDRESS -Nnt",
        shell=True).pid)
    with open("pid", "w") as file:
        file.write(pid)
    return pid


def kill():
    with open("pid", 'r') as file:
        subprocess.Popen("kill -9 " + str(file.read()), shell=True)
        print(file.read())


app = Flask(__name__)


@app.route("/start")
def start_route():
    result = start()
    return f"<p>server started ${result}</p>"


@app.route("/kill")
def kill_route():
    kill()
    return "<p>process kileed</p>"
