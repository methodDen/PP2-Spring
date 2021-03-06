import os
import shutil
import time
import pathlib
import datetime
def move_to_dir(new_path):
	os.chdir(new_path)


def move_to_parent_dir():
	path_parent = os.path.dirname(os.getcwd())
	os.chdir(path_parent)	


def clear_manager():
	os.system('cls')


def print_cur_path():
	print(f"Path: {os.getcwd()}")	

def is_fileordir_exists(path):
	return os.path.exists(path)	

def count_files_and_directories():
	cntFiles = 0
	cntDir = 0
	noOfFiles = 0
	for path in pathlib.Path(".").iterdir():
		if path.is_file():
			cntFiles += 1

	for _, dirs, files in os.walk('.'):
		for directories in dirs:
			cntDir += 1    
	print(f'There are {cntFiles} files and {cntDir} directories')

def help():
	print("List of available commands: ")
	commands = {
		"touch": "Create new file in current path",
		"delete file": "Delete specified file in current path",
		"open file": "Show contents of specified file in console",
		"rename file": "Change name of specified file", 
		"add content": "Add user content to specified file", 
		"rewrite content": "Rewrite content of specified file", 
		"create dir": "Create new directory in current path",
		"rename dir": "Change name of specified directory",
		"delete dir": "Delete specified directory in current path",
		"list dir": "List content of current directory and print number of files and subdirectories",
		"path": "Print current path", 
		"cd ..": "Return to parrent directory",
		"cd": "Move up to specified directory",
		"cls": "Clear console",
		"exit": "Shutdown console"
	}

	for x, y in commands.items():
		print(f"{x} --> {y}")	

def action():
	print("FileManager PEDRO v. 1.0.0")
	time.sleep(1.5)
	print("Created by: Daniyar Absatov. Contact creator at: admin@example.com. ")
	print("Initialization...")
	time.sleep(1.5)
	print("Note: in order to use commands, firstly write their names only.")
	time.sleep(0.5)
	print("After that, you will see hints, in which you will have to write necessary data.")
	time.sleep(0.5)
	print("""For listing all possible commands type in "help". """)




