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
    skip_duplicates = True
    seen_file_hashes = list()

    def __init__(self):
        temp = self.get_parameters('host')
        if temp:
            self.program_function = 'Host to backup device'
        else: 
            self.program_function = 'Backup device to host'

        temp = self.get_parameters('duplicate')
        if temp:
            self.skip_duplicates = True
        else: 
            self.skip_duplicates = False

        hostname = socket.gethostname()
        print('='*60)
        if hostname == MAC_HOSTNAME:
            self.OS = 'Mac'
            folder_a = '.'
            folder_b = os.path.join(os.sep, 'Volumes', 'camera_roll')
        elif hostname == WINDOWS_HOSTNAME:
            self.OS = 'Windows'
            folder_a = 'x'
            folder_b = os.path.join(os.sep, 'camera_roll')
        print(f'Running backup script using {self.OS} settings\nHostname: {hostname}')
        print(f'Function: {self.program_function}\nSkip duplicates is set to {str(self.skip_duplicates)}')
        print('='*60)

        self.sort_function(folder_a, folder_b)

        self.check_destination_folder()

        if self.skip_duplicates:
            self.scan_destination()

        


    def get_parameters(self, value):
        return_value = True
        if value in sys.argv:
            return_value = False
        return return_value

    def sort_function(self, folder_a, folder_b):
        if self.program_function == "Host to backup device":
            self.source_folder = folder_a
            self.destination_folder = folder_b
        else:
            self.source_folder = folder_b
            self.destination_folder = folder_a
            

    def check_destination_folder(self):
        try:
            if not os.path.exists(self.destination_folder):
                os.makedirs(self.destination_folder, exist_ok=True)
        except Exception as exc:
            print(f'Something has gone wrong when trying to make this folder:\n{self.destination_folder}\n{exc}')
            sys.exit()

    def scan_destination(self):
        for root, dir, files in os.walk(self.destination_folder):
            for file in files:
                self.seen_file_hashes = self.get_hash(os.path.join(root,file))

    def get_hash(self, file_path):
        blocksize = 65536
        try:
            this_file = open(file_path, 'rb')
            hasher = hashlib.md5()
            buf = this_file.read(blocksize)
            while len(buf) > 0:
                hasher.update(buf)
                buf = this_file.read(blocksize)
            this_file.close()
            return hasher.hexdigest()
        except PermissionError:
            self.file_info.warning(
                f'Permission denied trying to read "{file_path}" marked it as a duplicate')
            return 1

    

if __name__ == "__main__":
    backup_pictures = PictureBackupinator()
