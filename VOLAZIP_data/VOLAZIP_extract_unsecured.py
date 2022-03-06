from zipfile import ZipFile
from itertools import product
from telnetlib import theNULL
from numpy import character
import sys
import string
import zipfile
from rich import print, pretty

pretty.install()

with ZipFile('volazip.zip', 'r') as zipObj:
    zipObj.extractall('_Opened ZIP')
    print("All Files has been extracted inside the '_Opened ZIP' folder")
    with ZipFile('volazip.zip', 'r') as zipObj:
        listOfFileNames = zipObj.namelist()
        for fileName in listOfFileNames:
            if fileName.endswith('.csv'):
                zipObj.extract(fileName, 'temp_csv')
