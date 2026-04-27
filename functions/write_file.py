import os
from google import genai
from google.genai import types

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="write content for the file given by the file_path",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="the file path to the file."
            ),
            "content": types.Schema(
                type=types.Schema.STRING,
                description="the content that is written into the file"
            ),
        },
        required = ["file_path", "content"]
    ),
)

def write_file(working_directory, file_path, content):
    try:
        abs_path_wd = os.path.abspath(working_directory)
        abs_file_path = os.path.join(abs_path_wd, file_path)
        target_file = os.path.normpath(abs_file_path)

        shared_path = os.path.commonpath([abs_path_wd, abs_file_path])
        is_valid_path = abs_path_wd == shared_path

        if not is_valid_path:
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
        
        if os.path.isdir(target_file):
            return f'Error: Cannot write to "file_path" as it is a directory'
        
        os.makedirs(file_path, exist_ok = True)

        with open(target_file, "w") as f:
            f.write(content)

        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'

    except Eception as e:
        return f'Error reading file "{file_path}": {e}'



