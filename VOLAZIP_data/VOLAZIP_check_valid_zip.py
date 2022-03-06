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

zip_path = 'volazip.zip'

zipfile_archive = zipfile.ZipFile(zip_path)

import zipfile

try:
    zipfile_archive = zipfile.ZipFile(zip_path)
except zipfile.BadZipfile:
    import commands
    commands.getoutput('zip -FF '+zip_path)
    zipfile_archive = zipfile.ZipFile(zip_path)

for i in zipfile_archive.infolist():
    print (f'Reading... {i.filename, i.file_size}\n')

try: 
    print (f'Finished fixing files in {zipfile_archive}')
    print (f'[green]Files repaired successfully!!![/green]')
except zipfile.BadZipfile:
    print ('[red]Theres something wrong with CRC-23 CC[/red]')
    print ('[red]Theres something wrong with CRC-32[/red]')
    print (f'[red]Files repair failed!!![/red]')