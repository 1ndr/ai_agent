import os
from config import MAX_CHARS

schema_get_files_info = types.FunctionDeclaration(
    name="get_file_content",
    description="Returns the contents of a file in a specified file_path relative to the working directory",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                types=types.Type.STRING,
                description="path to the file relative to the working directory",
            ),
        },
    ),
)

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
        
        with open(target_path, "r") as f:
            file_content_string = f.read(MAX_CHARS)

            if f.read(1) != '':
                file_content_string += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
            return file_content_string

    except Exception as e:
        return f'Error reading file "{file_path}": {e}'





