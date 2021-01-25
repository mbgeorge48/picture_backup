import os
import shutil
import socket

WINDOWS_HOSTNAME = 'griffin'
MAC_HOSTNAME = 'phhenix'

hostname = socket.gethostname()
print('='*60)
if hostname == MAC_HOSTNAME:
    OS = 'Mac'
    SOURCE_FOLDER = '.'
    DESTINATION_FOLDER = os.path.join(os.sep, 'Volumes', 'camera_roll')
elif socker.gethostname() == WINDOWS_HOSTNAME:
    OS = 'Windows'
    SOURCE_FOLDER = 'x'
    DESTINATION_FOLDER = os.path.join(os.sep, 'Volumes', 'camera_roll')
print(f'Running backup script using {OS} settings\nHostname: {hostname}')
print('='*60)


def backup():
    for item in os.listdir(SOURCE_FOLDER):
        if item[0] != '.' and item[-3:] != '.py':
            print(f'Backing up {item}')
            shutil.copytree(os.path.join(SOURCE_FOLDER, item),
                            os.path.join(DESTINATION_FOLDER, item))


backup()