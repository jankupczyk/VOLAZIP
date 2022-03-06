from itertools import product
from telnetlib import theNULL
from numpy import character
import sys
import os
import string
import zipfile
from rich import print, pretty

pretty.install() 

maxsize = sys.maxsize
minsize = 1

print("\n---Be aware that a greater number than 6 may cause internal lag!---")
min_pswd_lenght = int(input("------Enter the minimum length of the password: "))
max_pswd_lenght = int(input("---------Enter the maximum length of the password: "))

count = 1
character_set = string.ascii_lowercase+string.ascii_uppercase+string.digits+string.punctuation

file_path_o = open('volazip_passwords.txt', 'w')

for i in range (min_pswd_lenght,max_pswd_lenght+1):
    for j in product(character_set,repeat=i):
        word = "".join(j)
        file_path_o.write(word)
        file_path_o.write('\n')
        count+=1
print(f"Creating 'volazip_passwords.txt' file complete {round((i/max_pswd_lenght)*100, 2)}%")
print("Created [{}] passwords ".format(count))