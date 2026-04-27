import os
import subprocess
from google import genai
from google.genai import types

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="executes a python file, with an optional list of arguments (args)",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="path to the file, relative to the working directory",
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                items=types.Schema(type=types.Type.STRING),
                description="additional arguments for the function. Default is NONE",
            ),
        }, required = ["file_path"],
    ),
)

def run_python_file(working_directory, file_path, args=None):
    try:
        abs_path_wd = os.path.abspath(working_directory)
        full_file_path = os.path.join(abs_path_wd, file_path)
        target_file = os.path.normpath(full_file_path)

        shared_path = os.path.commonpath([abs_path_wd, target_file])

        if shared_path != abs_path_wd:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        
        if not os.path.isfile(target_file):
            return f'Error: "{file_path}" does not exist or is not a regular file'
        
        last_three_chars = target_file[-3:]
        if last_three_chars !=".py":
            return f'Error: "{file_path}" is not a Python file'

        command = ["python", target_file]
        
        if args != None:
            command.extend(args)

        command_output = subprocess.run(command, cwd = abs_path_wd, capture_output = True, text = True, timeout = 30)

        output_string = "";
        if command_output.returncode != 0:
            output_string += f'Process exited with code "{command_output.returncode}".'
        if command_output.stdout == None and command_output.stderr == None:
            output_string += 'No output produced.'
        if command_output.stdout != None:
            output_string += f'STDOUT: "{command_output.stdout}".'
        if command_output.stderr != None:
            output_string += f'STDERR: f"{command_output.stderr}".'

        return output_string
    except Exception as e:
        return f'Error: executing Python file: {e}'



    



