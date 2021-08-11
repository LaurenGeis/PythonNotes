#! python3
# backup_to_zip.py - Copies an entire folder and its contents into
# a zip file whose filename increments

import zipfile, os

def backup_to_zip(folder):
    # backup the entire contents of "folder" into a zip file

    folder = os.path.abspath(folder)    # make sure the folder is absolute

    # figure out the filnemae this code was based on
    # use a file that already exists

    number = 1
    while True:
        zip_filename = os.path.basename(folder) + '_' + str(number) +'.zip'
        if not os.path.exists(zip_filename):
            break
        number = number + 1             # this is the increment

    # TODO: Create the zip file

    #TODO: Walk the entire folder tree and compress the files in each folder



