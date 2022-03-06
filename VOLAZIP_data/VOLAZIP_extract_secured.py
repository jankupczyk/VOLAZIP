from itertools import product
from telnetlib import theNULL
from numpy import character
import sys
import os
import string
import zipfile
from rich.console import Console
from time import sleep

console = Console()


pswd_list = "volazip_passwords.txt" 
file_in_zip = "test.txt"
zip_path = "volazip.zip"

with open(pswd_list, "rb") as passwords:
    
    passwords_list = passwords.readlines()
    
    passwords_list_enm = len(passwords_list)

    zip_file_to_crack = zipfile.ZipFile(zip_path)
    
    for index, password in enumerate(passwords_list):
        try:
            zip_file_to_crack.extractall(path="_Cracked ZIP",  pwd=password.strip())
            console.log(f"[green]PASSWORD FOUND!![/green]")
            console.log(f"Password was: ", password.decode().strip())
            print(f"All Files has been extracted inside the '_Cracked ZIP' folder")
        except:
            print(f"Scanning complete {round((index/passwords_list_enm)*100, 2)}%")
            print(f"Trying password: [white] {password.decode().strip()} [/white]")
            console.log(f"[red]Password failed![/red]\n")
            continue