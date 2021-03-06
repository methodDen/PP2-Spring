from functions_for_files import *
from functions_for_dirs import *
from utils import *
import os
import sys
import shutil
import time
import pathlib
action()
while True:
	inp = input(">> ")
	inp = inp.strip()

	if inp == 'create file':
		name = input("Enter new file name: ")
		try:
			create_file(name)
		except FileExistsError:
			print("You cannot create file with this name, because it already exists!")

	if inp == 'delete file':
		name = input(">> Specify file you want to delete: ")
		name = name.strip()
		name_path = os.path.join(os.getcwd(), name)
		if is_fileordir_exists(name_path) == False:
			print("The file you specified doesn't exist!")
		else:
			delete_file(name)

	if inp == 'open file':
		name = input(">> Specify file you want to open: ")
		name = name.strip()
		name_path = os.path.join(os.getcwd(), name)
		if is_fileordir_exists(name_path) == False:
			print("The file you specified doesn't exist!")
		else:
			open_file(name)	
	
	if inp == 'rename file':
		name = input(">> Specify file you want to rename: ")
		name_path = os.path.join(os.getcwd(), name)
		if is_fileordir_exists(name_path) == False:
			print("File with specified filename doesn't exist!")
		else:	
			new_name = input("Specify new file name: ")
			new_name_path = os.path.join(os.getcwd(), new_name)
			if is_fileordir_exists(new_name_path) == True:
				print("File with specified new name already exists!")
			else:	
				rename_file(name, new_name)	
	
	if inp == 'add content':
		name = input(">> Specify file you want to add content to: ")
		name = name.strip()
		name_path = os.path.join(os.getcwd(), name)
		if is_fileordir_exists(name_path) == False:
			print("The file you specified doesn't exist!")
		else:
			print("Note: press Ctrl-Z to see changes")
			print("Content: ")
			cont = (str(sys.stdin.read()))
			# print(cont)
			add_content(name, cont)	

	if inp == 'rewrite content':
		name = input(">> Specify file you want to rewrite: ")
		name = name.strip()	
		name_path = os.path.join(os.getcwd(), name)
		if is_fileordir_exists(name_path) == False:
			print("The file you specified doesn't exist!")
		else:
			ans = input(f"Are you sure to rewrite {name} content? [y/N]")
			if ans == 'y':
				print("Note: press Ctrl-Z to see changes")
				print("Content: ")
				cont = (str(sys.stdin.read()))
				# print(cont)
				rewrite_content(name, cont)
			else:
				if ans == 'N':
					print("Ok, file rewriting is canceled")
				else: 
					print("Please, write characters correctly!")

	if inp == 'create dir':
		name = input(">> Enter new directory name: ")
		try:
			create_dir(name)
		except FileExistsError:
			print("You cannot create file with this name, because it already exists!")	


	if inp == 'rename dir':
		name = input(">> Specify directory you want to rename: ")
		name_path = os.path.join(os.getcwd(), name)
		if is_fileordir_exists(name_path) and os.path.isdir(name_path): 
			new_name = input("Specify new directory name: ")
			new_name_path = os.path.join(os.getcwd(), new_name)
			if is_fileordir_exists(new_name_path) == True:
				print("Directory with specified new name already exists!")
			else:	
				rename_dir(name, new_name)	
		else:	
			print("Specified directory doesn't exist!")

	if inp == 'delete dir':
		name = input(">> Specify file you want to delete: ")
		name = name.strip()
		name_path = os.path.join(os.getcwd(), name)
		if is_fileordir_exists(name_path) and os.path.isdir(name_path):
			delete_dir(name)
		else: 
			print("Specified directory doesn't exist!")	

	if inp == 'list dir':
		list_content_of_dir()	
		count_files_and_directories()	

	if inp == 'path':
		print_cur_path()		

	if inp == 'cd ..':
		move_to_parent_dir()
		print_cur_path()

	if inp == 'cd':
		name = input(">> Specify directory you want to open: ")
		name = name.strip()
		name_path = os.path.join(os.getcwd(), name)
		if is_fileordir_exists(name_path) == False:
			print("Specified directory doesn't exist!")
		else:
			move_to_dir(name_path)
			print_cur_path()	

	if inp == 'help':
		help()
			
	if inp == 'cls':
		clear_manager()		
		print_cur_path()

	if inp == 'exit':
		break

	if inp == 'bruh':
		print("When will you be done with coding at 4AM? (available answers: never)")
		ans = input()
		if ans == 'never':
			print("That's rough, buddy")
		else:
			print("KBTU Students lives matter ;)")	
	if inp == 'python':
		print("Nice joke, hahaha")