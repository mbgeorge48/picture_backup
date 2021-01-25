import os
import shutil
import socket
import hashlib
import sys

# Functions
# Copy from host to backup device
# Copy from backup device to host
# Don't copy files that are already there


# Needs rewriting so we can deduplicate
# def backup():
#     for item in os.listdir(SOURCE_FOLDER):
#         if item[0] != '.' and item[-3:] != '.py':
#             print(f'Backing up {item}')
#             shutil.copytree(os.path.join(SOURCE_FOLDER, item),
#                             os.path.join(DESTINATION_FOLDER, item))

WINDOWS_HOSTNAME = 'griffin'
MAC_HOSTNAME = 'phoenix'

class PictureBackupinator:
    source_folder = os.sep
    destination_folder = os.sep

    def __init__(self):
        self.program_function = self.get_parameters()
        hostname = socket.gethostname()
        print('='*60)
        if hostname == MAC_HOSTNAME:
            self.OS = 'Mac'
            folder_a = '.'
            folder_b = os.path.join(os.sep, 'Volumes', 'camera_roll')
        elif hostname == WINDOWS_HOSTNAME:
            self.OS = 'Windows'
            folder_a = 'x'
            folder_b = os.path.join(os.sep, 'd', 'camera_roll')
        print(f'Running backup script using {self.OS} settings\nHostname: {hostname}')
        print(f'Function: {self.program_function}')
        print('='*60)

        self.sort_function(folder_a, folder_b)
        # self.check_destination_folder()

    def get_parameters(self):
        try:
            if sys.argv[1] == "Host":
                return "Backup device to host"
            else:
                raise IndexError
        except IndexError:
            return "Host to backup device"

    def sort_function(self, folder_a, folder_b):
        if self.program_function == "Host to backup device":
            self.source_folder = folder_a
            self.destination_folder = folder_b
        else:
            self.source_folder = folder_b
            self.destination_folder = folder_a
            

    def check_destination_folder(self):
        try:
            if not os.path.exists(DESTINATION_FOLDER):
                os.makedirs(DESTINATION_FOLDER, exist_ok=True)
        except Exception as exc:
            print(f'Something has gone wrong when trying to make this folder:\n{DESTINATION_FOLDER}\n{exc}')
            sys.exit()


if __name__ == "__main__":
    backup_pictures = PictureBackupinator()
