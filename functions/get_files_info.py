import os

def get_files_info(working_directory, directory="."):
    abs_path_to_dir = os.path.abspath(directory)
    abs_path_to_work_dir = os.path.abspath(working_directory)

    rel_path_dir = os.path.join(working_directory, directory)
    abs_path_to_dir_from_work_dir = os.path.abspath(rel_path_dir)

    if abs_path_to_dir != abs_path_to_dir_from_work_dir:
        raise Exception(f"rror: Cannot list "{directory}" as it is outside the permitted working directory")

    if: 

    

def finding_directory_in_working_directory(working_directory, directory):
    
