from itertools import product
from telnetlib import theNULL
from numpy import character
import cv2
import sys
import os
import string
import zipfile
from rich import print, pretty
from simplejson import dump
from pyfiglet import Figlet

pretty.install()

banner = Figlet(font='smslant')

print(banner.renderText('VOLAZIP'))
print("Created by JAN KUPCZYK")
print("0. Type '0' if u need help, this will provide you a step by step solution to your problem")
print("1. Create a list of possible passwords [.txt]")
print("2. Open any archive secured [BRUTEFORCE]")
print("3. Open any archive unsecured [NORMAL]")
print("4. Get hash of zip folder [.zip .rar .rar4]")
print("5. List all files in archive")
print ("6. Repair corrupted archive and its files")
print("7. Remove all archive files")
option = int(input("--> Choose option: "))
exit_key = cv2.waitKey(1) & 0xFF

if option == 0:
    import VOLAZIP_data.VOLAZIP_main_tutorial as VOLAZIP_main_tutorial
elif option == 1:
    import VOLAZIP_data.VOLAZIP_generate_wordlist as VOLAZIP_generate_wordlist
    import run
elif option == 2:
    import VOLAZIP_data.VOLAZIP_extract_secured as VOLAZIP_extract_secured
    import run
elif option == 3:
    import VOLAZIP_data.VOLAZIP_extract_unsecured as VOLAZIP_extract_unsecured
    import run
elif option == 4:
    import VOLAZIP_data.VOLAZIP_get_hash as VOLAZIP_get_hash
elif option == 5:
    import VOLAZIP_data.VOLAZIP_get_details as VOLAZIP_get_details
elif option == 6:
    import VOLAZIP_data.VOLAZIP_check_valid_zip as VOLAZIP_check_valid_zip
elif option == 7:
    import VOLAZIP_data.VOLAZIP_remove_file as VOLAZlP_remove_file
elif exit_key == ord('\x1b'):
    run.close()
    exit()

if __name__ == '__main__':
    pass