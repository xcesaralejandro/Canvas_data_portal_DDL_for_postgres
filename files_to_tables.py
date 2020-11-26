import pandas as pd
from os import path, listdir, mkdir
from tqdm import tqdm
import gzip
import csv
from sqlalchemy import create_engine
import psycopg2 
import io
import time


# Preparing the database engine
db_user = 'YOUR_DB_USER'
db_pass = 'YOUR_DB_PASS'
db_host = 'YOUR_DB_HOST'
db_port = 'YOUR_DB_PORT'
db_name = 'YOUR_DB_NAME'
db_engine = create_engine('postgresql+psycopg2://'+db_user+':'+db_pass+'@'+db_host+':'+db_port+'/'+db_name)

# Path to the "dataFiles" folder. This folder is generated when downloading the data from canvas data portal with CanvasDataCli
path_to_folders = 'PATH_TO_DATA_FILES'
folders = listdir(path_to_folders)
folders.remove("schema.json")


# Tour of folders, files and upload to the database
for current_folder in range(len(folders)):
    print('\n')
    print("Filling table: " + folders[current_folder])
    path_to_files = path_to_folders + folders[current_folder] + '/'
    table_name = folders[current_folder]
    files = listdir(path_to_files)
    for current_file in tqdm(range(len(files))):
        file_path = path_to_files + files[current_file]
        dataframe = pd.read_csv(file_path, compression='gzip', 
                                         header = None, 
                                         sep='\t', 
                                         quoting=csv.QUOTE_NONE,
                                         error_bad_lines=False, 
                                         low_memory=False,
                                         encoding='utf-8')
        db_connection = db_engine.raw_connection()
        db_cursor = db_connection.cursor()
        output = io.StringIO()
        dataframe.to_csv(output, sep='\t', header=False, index=False)
        output.seek(0)
        contents = output.getvalue()
        db_cursor.copy_from(output, table_name)
        db_connection.commit()