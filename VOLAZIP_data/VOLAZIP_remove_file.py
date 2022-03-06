from zipfile import ZipFile
from itertools import product
from telnetlib import theNULL
from numpy import character
import sys
import os
import string
import zipfile
from rich import print, pretty

pretty.install()


file_rm = r'volazip.zip'

print("Did you really want to delete these files? 'y/n' ")
option_delete = input("../ ")

if option_delete == 'y':
    print("This will delete your all archive files! 'yes/no' ")
    option_delete = input("../ ")
    if option_delete == 'yes':
        print(f"Removed 'volazip.zip' | {os.remove(file_rm)}")
elif option_delete == 'no' or option_delete == 'n':
    print("[red]EXITING...[/red]")
    exit()
