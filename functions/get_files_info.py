import os

def get_files_info(working_directory, directory="."):
    abs_path_wd = os.path.abspath(working_directory)
    dir_path = os.path.join(abs_path_wd, directory)
    target_dir = os.path.normpath(dir_path)

    shared_path = os.path.commonpath([abs_path_wd, target_dir])
    is_valid_path = abs_path_wd == shared_path

    if not is_valid_path:
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    
    if not os.path.isdir(target_dir):
        return f'Error: "{directory}" is not a directory'
    
    dir_content_lst = os.listdir(target_dir)
    return_arr = []
    for item in dir_content_lst:
        try:
            item_file_path = os.path.join(target_dir, item)
        except:
            return f"Error: unable to find file path for {item}"

        try:
            size = os.path.getsize(item_file_path)
        except:
            return f"Error: can't find size for {item}"

        try:
            is_dir = os.path.isdir(item_file_path)
        except:
            return f"Error: can't find if {item} is directory or file."

        return_arr.append(f"- {item}: file_size={size} bytes, is_dir={is_dir}")

    return "\n".join(return_arr)

   


