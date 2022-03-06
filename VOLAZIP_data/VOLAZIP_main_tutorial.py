from itertools import product
from telnetlib import theNULL
from numpy import character
from rich import print, pretty
from rich.console import Console
import webbrowser
import sys
import string
import zipfile
import os

pretty.install()

console = Console()

err01 = "[red]Command is either misspelled or could not be found![/red]"
tutorial_open = open("readme.txt", "r")
console.log(f"{tutorial_open.read()}") 


print("\n")
print("Type 'help' if you need help or if u want to create ticket")
print("Type 'how' if you dont know how to use VOLAZIP")
print("Type 'nvm' if you want return to app")
print("Type 'bso' if you need special ")
print("Type 'credits' to see credits :)")
print("Type 'exit' if you want leave")
tutorial_option = (input("../ "))

if tutorial_option == "help":
    webbrowser.open("https://github.com/jankupczyk/VOLAZIP/issues")
    print("'Redirecting to github.com'")
elif tutorial_option == "how":
    print(err01)
elif tutorial_option == "nvm":
    print(err01)
elif tutorial_option == "bso":
    print(err01)
elif tutorial_option == "credits":
    print("VOLAZIP|CREDITS".center(40, "+"))
    print("AUTHOR: JAN KUPCZYK")
    print("GITHUB: https://github.com/jankupczyk")
    print("LICENSE: ")
elif tutorial_option == "exit":
    print("[red]EXITING...[/red]")
    tutorial_open.close()
    exit()