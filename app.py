from flask import Flask
import socket
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/hostname")
def hostname():
    return socket.gethostname()

@app.route("/healthz")
def healthcheck():
    return "OK"

if __name__ == "__main__":
    app.run(host='0.0.0.0')
