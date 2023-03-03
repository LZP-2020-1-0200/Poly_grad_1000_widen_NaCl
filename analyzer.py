import os
import zipfile
import sqlite3
import cnst as c
import json


def prepare_clean_output_folder(folder_name):
    global OUTFOLDER
    OUTFOLDER = folder_name
    if os.path.exists(folder_name):
        for f in os.listdir(folder_name):
            os.remove(os.path.join(folder_name, f))
    else:
        os.mkdir(folder_name)
