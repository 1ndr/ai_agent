import os

def get_files_info(working_directory, directory="."):
    abs_path_wd = os.path.abspath(working_directory)
    dir_path = os.path.join(abs_path_wd, directory)
    target_dir = os.path.normpath(dir_path)

    shared_path = os.path.commonpath(abs_path_wd, target_dir)
    is_valid_path = abs_path_wd == shared_path

    if not is_valid_path:
        print(f'Error: Cannot list "{directory}" as it is outside the permitted working directory')
        return
    
    if not os.path.isdir(directory):
        print(f'Error: "{directory}" is not a directory")
        return
    
    dir_content_lst = os.listdir(shared_path)
    return_arr = []
    for item in dir_content_lst:
        try:
            item_file_path = os.path.join(shared_path, item)
        except:
            print(f"Error: unable to find file path for {item}")
            return

        try:
            size = os.path.getsize(item_file_path)
        except:
            print(f"Error: can't find size for {item}")
            return

        try:
            is_dir = os.path.isdir(item_file_path)
        except:
            print(f"Error: can't find if {item} is directory or file.")
            return
        return_arr.append(f"- {item}: file_size={size} bytes, is_dir={is_dir}")

    return " /n",join(return_arr)

   


