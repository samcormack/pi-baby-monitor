import subprocess

from flask import Flask

app = Flask(__name__)

@app.route('/picam/start')
def start():
    subprocess.run('sudo /etc/init.d/picam start')
    return "Success!"

@app.route('/picam/stop')
def stop():
    subprocess.run('sudo /etc/init.d/picam stop')
    return "Success!"