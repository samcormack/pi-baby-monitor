import subprocess
from multiprocessing.managers import BaseManager

from flask import Flask

import picam

app = Flask(__name__)

@app.route('/picam/start')
def start():
    manager = BaseManager(('', 37844), b'password')
    manager.register('get_picam_process')
    manager.connect()
    manager.get_picam_process(picam.start)
    return "Success!"

@app.route('/picam/stop')
def stop():
    manager = BaseManager(('', 37844), b'password')
    manager.register('get_picam_process')
    manager.connect()
    manager.get_picam_process().kill()
    return "Success!"

if __name__=='__main__':
    app.run()