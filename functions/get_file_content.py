import os
from config import MAX_CHARS

def get_file_content(working_directory, file_path):
    try:
        abs_path_wd = os.path.abspath(working_directory)
        file_path = os.path.join(abs_path_wd, file_path)
        target_path = os.path.normpath(file_path)

        shared_path = os.path.commonpath([abs_path_wd, target_path])

        if shared_path != abs_path_wd:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        
        if not os.path.isfile(target_path):
            return f'Error: File not found or is not a regular file: "{file_path}"' 
        
        with open(target_path) as f:
            f.read()



