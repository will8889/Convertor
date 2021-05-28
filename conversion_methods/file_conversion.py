import subprocess
import time

def convert(input_folder,output_folder,filename):
    ext = filename.split(".")[-1]
    if ext == "pdf": target = "docx"
    else: target = "pdf"
    converted_filename = filename.split(".")[0] + "." + target
    subprocess.Popen(["abiword","--to=pdf",filename],cwd = input_folder)
    time.sleep(5)
    subprocess.Popen(["mv", input_folder + "/" + converted_filename, output_folder])
    return converted_filename
