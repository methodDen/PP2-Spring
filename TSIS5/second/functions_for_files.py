import os
import shutil

def create_file(name):
	f = open(name, 'x')
	print(f"File {name} is created succesfully!")


def delete_file(name):
	name_path = os.path.join(os.getcwd(), name)
	os.remove(name_path)
	print(f"File {name} was succesfully deleted!")


def open_file(name):
	name_path = os.path.join(os.getcwd(), name)
	print("Current file content: ")
	with open(rf'{name_path}', 'r') as file:
		print(file.read())
	if os.stat(f'{name_path}').st_size == 0:
		print("(This file is empty!)")	

def rename_file(name, new_name):
	name_path = os.path.join(os.getcwd(), name)
	new_name_path = os.path.join(os.getcwd(), new_name)
	os.rename(rf'{name_path}', rf'{new_name_path}')
	print(f"File name {name} was succesfully changed to {new_name}!")

def add_content(name, text):
	name_path = os.path.join(os.getcwd(), name)
	with open(rf'{name_path}', 'a') as file:
		file.write(text)
	print(f"File {name} is changed succesfully!")	
	print("Current file content: ")
	with open(rf'{name_path}', 'r') as file:
		print(file.read())		
	if os.stat(f'{name_path}').st_size == 0:
		print("(This file is empty!)")					

def rewrite_content(name, text):
	name_path = os.path.join(os.getcwd(), name)
	with open(rf'{name_path}', 'w') as file:
		file.write(text)
	print(f"File {name} is changed succesfully!")	
	print("Current file content: ")
	with open(rf'{name_path}', 'r') as file:
		print(file.read())
	if os.stat(f'{name_path}').st_size == 0:
		print("(This file is empty!)")				
