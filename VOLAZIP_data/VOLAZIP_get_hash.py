from stat import ST_INO
from rich.console import Console
import hashlib
from itertools import product
from telnetlib import theNULL
from numpy import character
from datetime import date, datetime
import ntpath
import sys
import os
import string
import zipfile
console = Console()

def zipdir(path, ziph):
    for root, dirs, files in os.walk(path):
        if '.git' not in root:
            for file in files:
                ziph.write(os.path.join(root, file))


file_hash_date_created_r = datetime.now()

file_hash_date_created = file_hash_date_created_r.strftime("%d/%m/%Y %H:%M:%S")
file_hash_o = open('tmp_hash.txt', 'a')
file_hash =  hashlib.md5(open('volazip.zip', 'rb').read()).hexdigest()

file_hash_o.write(f"[{file_hash_date_created}] initialized {ntpath.basename(r'VOLAZIP/VOLAZIP_data/VOLAZIP_GET_HASH.py')} -> obtained hash: {file_hash}\n")

console.log(f"[red]Hash: [/red] [blue]{file_hash}[/blue]\n")