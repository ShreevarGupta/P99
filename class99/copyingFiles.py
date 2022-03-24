import os
import shutil

source = input("Enter the name of the source folder. ")
destination = input("Enter the name of the destination folder. ")

source = source + '/'
destination = destination + '/'

listOfFiles = os.listdir(source)

for files in listOfFiles:
    shutil.copy((source + files), destination)
    