from PIL import Image

class ImageConvertor:

    def __init__(self, input_dir, output_dir):
        self.__input_dir = input_dir
        self.__output_dir = output_dir
        self.__extensions = ["jpg","jpeg","tiff","bmp","png","eps"]
     
    def __extract_file_name(self, name):
        temp = name.split(".")
        out = ""
        for i in range(len(temp)-1):
            out += temp[i]
            if i != len(temp)-2:
                out += "."

        return out

    def convert(self, file_name, target):
        if file_name.split(".")[-1] not in self.__extensions:
            print("File type must either be jpg, jpeg, tiff, bmp, png or eps")

        elif target not in self.__extensions:
            print("Target file type must either be jpg, jpeg, tiff, bmp, png or eps")

        else:
            file_dir = self.__input_dir + "/" + file_name 
            temp_name = self.__extract_file_name(file_name)
            converted_dir = self.__output_dir + "/" + temp_name + "." + target
            file_image = Image.open(file_dir)
            
            if file_name.split(".")[-1] == "bmp" and target == "tiff":
                file_image.convert('RGB').save(converted_dir,format="tiff",compression=None)
            else:
                file_image.convert('RGB').save(converted_dir)
            
            return self.__extract_file_name(file_name) + "." + target

    def set_dir(self, input_dir = None, output_dir = None):
        if input_dir != None:
            self.__input_dir = input_dir
        if output_dir != None:
            self.__output_dir = output_dir

    def get_dir(self):
        print("Current input directory: {}".format(self.__input_dir))
        print("Current output directory: {}".format(self.__output_dir))