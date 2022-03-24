import imp
import shutil
import os
import shutil

source = input("Name the source folder. ")
destination = input("Name the destination folder. ")

source = source + '/'
destination = destination + '/'

list_of_files = os.listdir(source)

for files in list_of_files:
    shutil.move((source + files), destination)
    