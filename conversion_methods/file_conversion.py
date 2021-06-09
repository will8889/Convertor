# Used to convert word documents from docx to pdf and vice versa

import subprocess
import time
from os.path import isfile

def convert(input_folder,output_folder,filename):
    ext = filename.split(".")[-1]
    if ext == "pdf": target = "docx"
    else: target = "pdf"
    converted_filename = filename.split(".")[0] + "." + target # Extract file name
    print(ext, target, converted_filename) 
    subprocess.Popen(["abiword","--to="+target,filename],cwd = input_folder) # Calls abiword to convert file
    while isfile(input_folder + "/" + converted_filename) == False: # Waits for output file
        continue
    subprocess.Popen(["mv", input_folder + "/" + converted_filename, output_folder]) # Move converted file to output folder
    return converted_filename
