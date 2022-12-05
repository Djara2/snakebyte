# File Tools by David Jara - Last Updated 08/31/2022

import os
import platform

"""
TABLE OF CONTENTS

1. OS AND FILE MANAGER METHODS
    - get_os
    - get_path
    - get_path_basename
    - get_full_file_path
    - get_full_folder_path

2. FILE METHODS
    - is_file
    - get_file_extension
    - get_all_file_extensions
    - get_files_by_extension
    - get_file_extension_map
    - delete_file

3. DIRECTORY METHODS
    * This includes those methods that have to deal with files; however if a method first and foremost has a connection to a specific directory, then it is considered a directory method, for example "get_directory_files()"

    - is_directory
    - get_directory_files
    - get_directory_files_set
    - get_directory_files_including_tilde
    - get_directory_directories
    - get_directory_directories_set
    - search_for_directory

4. INTERDEPENDENT FILE AND DIRECTORY METHODS
    * Some methods cannot just be in the FILES section, because they also use methods from the DIRECTORIES section.

    - search_for_file
"""

# 1. OS AND FILE MANAGER METHODS
# ----------------------------------------------------

def get_os():
    return platform.system()    

def get_path():
    return os.getcwd()

def get_path_basename(path):
    return os.path.basename(path)

def get_full_file_path(path, filename):
    return f"\"{path}\\{filename}\""

def get_full_folder_path(path, folder_name):
    return f"\"{path}\\{folder_name}\\\""

# 2. FILE METHODS
# -------------------------

def is_file(filename, path = None):
    if path == None:
        path = get_path()

    return os.path.isfile(os.path.join(path, filename))

def get_file_extension(file):
    if "." in file:
        split_file = file.split(".")
        extension = split_file[1]
        return extension

def get_all_file_extensions(files):
    file_types = set()
    for file in files:
        extension = get_file_extension(file)
        # should be faster by opting to use a set over a list
        if extension not in file_types:
            file_types.add(extension)
    return file_types

def get_files_by_extension(files, extension):
    sorted_files = []
    for file in files:
        if f".{extension}" in file:
            sorted_files.append(file)
    
    return sorted_files

def get_file_extension_map(files):
    fmap = dict()
    file_types = get_all_file_extensions(files)
    for file_type in file_types:
        fmap[file_type] = get_files_by_extension(files, file_type)

    return fmap

def delete_file(file, path=None):
    if path == None:
        path = get_path()

    os.system(f"del \"{path}\\{file}\"")

# 3. DIRECTORY METHODS
# -----------------------------------

def is_directory (directory, path = None):
    if path == None:
        path = get_path()

    return not(os.path.isfile(os.path.join(path, directory)))

def get_directory_files(path, argument=None):
    directory_contents = os.listdir(path)
    files_list = []
    for file in directory_contents:
        if os.path.isfile(os.path.join(path, file)):
            if argument == None:
                if not "~" in file:
                    files_list.append(file)
            else:
                if argument[0] in ["search", "s"]:
                    search_string = argument[1]
                    if (search_string in file) and (not "~" in file):
                        files_list.append(file)

                if argument[0] == "grouped_extensions":
                    # get ALL files, then filter
                    if not "~" in file:
                        files_list.append(file)

    return files_list

def get_directory_files_set(path, argument=None):
	directory_contents = os.listdir(path)
	files_set = {}
	for file in directory_contents:
		if os.path.isfile(os.path.join(path, file)):
			if argument == None:
				if not "~" in file:
					files_set.add(file)
	return files_set

def get_directory_files_including_tilde(path, argument=None):
    directory_contents = os.listdir(path)
    files_list = []
    for file in directory_contents:
        if os.path.isfile(os.path.join(path, file)):
            if argument == None:
                files_list.append(file)
            else:
                if argument[0] in ["search", "s"]:
                    search_string = argument[1]
                    if (search_string in file) and (not "~" in file):
                        files_list.append(file)

                if argument[0] == "grouped_extensions":
                    # get ALL files, then filter
                    if not "~" in file:
                        files_list.append(file)

    if argument != None:
        if argument[0] == "grouped_extensions":
            files_map = sort_files_by_extension(files_list)
            files_list = []
            for extension in files_map:
                for file in files_map[extension]:
                    files_list.append(file)

    return files_list

def get_directory_directories(path, argument = None):
    directory_contents = os.listdir(path)
    directories_list = []
    for file in directory_contents:
        if not (os.path.isfile(os.path.join(path, file))):
            if argument == None:
                directories_list.append(file)
            else:
                if argument[0] in ["search", "s"]:
                    search_string = argument[1]
                    if search_string in file:
                        directories_list.append(file)
    return directories_list

def get_directory_directories_set(path):
	directory_contents = os.listdir(path)
	directories_set = set()
	for file in directory_contents:
		if not(os.path.isfile(os.path.join(path, file))):
			directories_set.add(file)
	
	return directories_set		
	
def search_for_directory(directory_name, path = None):
    if path == None:
        path = get_path()

    directories_in_directory = get_directory_directories(path)

    if directory_name in directories_in_directory:
        return f"\"{path}\\{directory_name}\""

    else:
        print(f"Directory {directory_name} was not found in the directory {path}")
        return None

# INTERDEPENDENT FILE AND DIRECTORY METHODS

def search_for_file(filename, path=None):
    if path == None:
        path = get_path()

    files_in_directory = get_directory_files(path)

    if filename in files_in_directory:
        return f"\"{path}\\filename\""
    else:
        print(f"File {filename} was not found in the directory.")
        return None
