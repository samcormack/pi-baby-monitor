import atexit
from multiprocessing import Lock
from multiprocessing.managers import BaseManager
from subprocess import Popen

lock = Lock()
picam_process = Popen(['/home/pi/picam/picam', '--version'])

def get_picam_process(start_func=None):
    with lock:
        if picam_process.poll() is None:
            return picam_process
        else:
            global picam_process
            picam_process = start_func()
            return picam_process


@atexit.register
def close_picam():
    picam_process.kill()


manager = BaseManager(('', 37844), b'password')
manager.register('get_picam_process', get_picam_process)
server = manager.get_server()
server.serve_forever()