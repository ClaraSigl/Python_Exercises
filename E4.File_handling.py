'''
Created: 13/May/2023
Last Updated: 13/May/2023
Author: Clara Sigl

This script contains the answers for a number of exercises concerning collection data types from the course BINP16 (Programming in Python).
BINP16 is thaugt at Lund University, and the exercies were obtained from autumn 2022.
Note that the exercises have been modified somewhat to fit as standalone exercises (and not as a continuation of a previous exercise).
'''

'''
Excercise 1. Create a function which takes two inputs, a directory and a pattern. The function should print all files or folders within the directory matching the pattern. 
The function should not print any file/folder extensions, but it should print what type each file/folder is.
Example:
> find_file(ex_dir, test_123) 
> Folder  test_123  
> File    test_12345
'''
from pathlib import Path

def find_file(inp_dir, pattern):
    dir = Path(inp_dir)
    if dir.is_dir() == True:
        pattern = "*{}*".format(pattern)
        file_list = list(dir.glob(pattern))
        if len(file_list) > 0:
            for i in file_list:
                if i.is_file() == True:
                    print("File\t{}".format(i.stem))
                elif i.is_dir() == True:
                    print("Folder\t{}".format(i.stem))
        else:
            print("No files or folders containing the pattern could be found within the directory.")
            exit()
    else:
        print("Please make sure you entered an existing directory as the first argument.")
        exit()
