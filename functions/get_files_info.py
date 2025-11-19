import os

def get_files_info(working_directory, directory="."):
    obspath_w_directory = os.path.abspath(working_directory)
    obspath_w_directory_and_directory = os.path.join(obspath_w_directory, directory)

    full_path_to_directory = os.path.join(working_directory, directory)
    obspath_full_path_to_directory = os.path.abspath(full_path_to_directory)

    if obspath_w_directory_and_directory != obspath_full_path_to_directory:
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory"

    if os.path.isdir(obspath_full_path_to_directory):
        return f'Error: "{directory}" is not a directory'
    
    items_list = os.listdir(directory)

    for item in items_list:
        is_dir = not os.path.isfile(item)
        file_size = os.path.getsize(item)
        print f'- {item}: file_size={file_size} bytes, is_dir={is_dir}\n'
