import os
import shutil
import pathlib
def create_dir(name):
	parent_dir = os.getcwd()
	path = os.path.join(parent_dir, name)
	os.mkdir(path)
	print(f'Directory {name} was created succesfully!')	


def rename_dir(name, new_name):
	name_path = os.path.join(os.getcwd(), name)
	new_name_path = os.path.join(os.getcwd(), new_name)
	os.rename(rf'{name_path}', rf'{new_name_path}')
	print(f"Directory name {name} was succesfully changed to {new_name}!")

def delete_dir(name):
	dir_path = os.path.join(os.getcwd(), name)
	shutil.rmtree(dir_path)
	print(f"Directory {name} was succesfully deleted!")
	
def list_content_of_dir():
	path = "."
	dir_list = os.listdir(path)
	for file in dir_list:
		print(file)
	