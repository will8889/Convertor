from docx2pdf import convert
from pdf2docx import Converter

class FileConvertor:

    def __init__(self, input_dir, output_dir):
        self.__input_dir = input_dir
        self.__output_dir = output_dir
        self.__extensions = ["docx","pdf"]
     
    def __extract_file_name(self, name):
        temp = name.split(".")
        out = ""
        for i in range(len(temp)-1):
            out += temp[i]
            if i != len(temp)-2:
                out += "."

        return out

    def convert_file(self, file_name):
        ext = file_name.split(".")[-1]
        if ext == "pdf": target = "docx"
        else: target = "pdf"
        if ext not in self.__extensions:
            print("File type must either be docx or pdf")

        else:
            file_dir = self.__input_dir + "/" + file_name 
            temp_name = self.__extract_file_name(file_name)
            converted_dir = self.__output_dir + "/" + temp_name + "." + target

            if target == "pdf":
                convert(file_dir,converted_dir)

            elif target == "docx":
                convertor = Converter(file_dir)
                convertor.convert(converted_dir, start = 0, end = None)
                convertor.close()
        
            return self.__extract_file_name(file_name) + "." + target

    def set_dir(self, input_dir = None, output_dir = None):
        if input_dir != None:
            self.__input_dir = input_dir
        if output_dir != None:
            self.__output_dir = output_dir

    def get_dir(self):
        print("Current input directory: {}".format(self.__input_dir))
        print("Current output directory: {}".format(self.__output_dir))



        

    

