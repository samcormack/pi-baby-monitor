import os
import subprocess

PICAM_DIR = '/home/pi/picam'
SHM_DIR = '/run/shm'
USE_DIRS = ['rec', 'hooks', 'state', 'archive']

def make_dirs():
    for dirname in USE_DIRS:
        os.makedirs(os.path.join(SHM_DIR, dirname), exist_ok=True)
        subprocess.run([
            'ln',
            '-sfn',
            os.path.join(SHM_DIR, dirname),
            os.path.join(PICAM_DIR, dirname)
        ])

def start():
    command = [
        os.path.join(PICAM_DIR, 'picam'),
        '-o', os.path.join(SHM_DIR, 'hls'),
        '--vfr',
        '--autoex',
        '--rotation 270',
        '--samplerate 48000',
        '--channels 2',
        '--time',
        '--alsadev plug:dmic_hw',
        '--volume 10',
        '> /var/log/picam.log 2&>1'
    ]
    make_dirs()
    return subprocess.Popen(command, cwd=PICAM_DIR)
