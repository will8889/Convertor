# This file acts as a script to clean up both upload and output folder daily 

from os.path import join,isfile
from os import remove,listdir


UPLOAD_FOLDER = "/home/convertorwebapp/Convertor/uploads"
OUTPUT_FOLDER = "/home/convertorwebapp/Convertor/output"

# Removes contents of both folder
for i in listdir(UPLOAD_FOLDER):
    i = join(UPLOAD_FOLDER,i)
    if isfile(i):
        remove(i)

for i in listdir(OUTPUT_FOLDER):
    i = join(OUTPUT_FOLDER,i)
    if isfile(i):
        remove(i)
