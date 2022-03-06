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

with ZipFile('volazip.zip', 'r') as zipObj:
    listOfiles = zipObj.infolist()
    for elem in listOfiles:
        print("\n")
        print(f"{elem.filename, ' : ', elem.file_size, ' : ', elem.date_time, ' : ', elem.compress_size}")
        print(f"Details of all files in archive")
        with ZipFile('volazip.zip', 'r') as zipObj:
            zipObj.printdir()