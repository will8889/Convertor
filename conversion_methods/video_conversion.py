# Used to convert a video file from 1 type to another

import ffmpeg

class VideoConvertor:

    def __init__(self, input_dir, output_dir):
        self.__input_dir = input_dir
        self.__output_dir = output_dir
        self.__extensions = ["mp4","mov","mkv","avi","wmv","flv"] # Supported file types
    
    # Extract file name
    def __extract_file_name(self, name):
        temp = name.split(".")
        out = ""
        for i in range(len(temp)-1):
            out += temp[i]
            if i != len(temp)-2:
                out += "."

        return out

    # The actual conversion function
    def convert(self, file_name, target):
        if file_name.split(".")[-1] not in self.__extensions:
            print("File type must either be mp4, mov, mkv, avi, wmv, or flv")

        elif target not in self.__extensions:
            print("Target file type must either be mp4, mov, mkv, avi, wmv, or flv")

        else:
            file_dir = self.__input_dir + "/" + file_name 
            temp_name = self.__extract_file_name(file_name)
            converted_dir = self.__output_dir + "/" + temp_name + "." + target
            (
            ffmpeg
            .input(file_dir)
            .output(converted_dir)
            .run()
            )
            return self.__extract_file_name(file_name) + "." + target 

    def set_dir(self, input_dir = None, output_dir = None):
        if input_dir != None:
            self.__input_dir = input_dir
        if output_dir != None:
            self.__output_dir = output_dir

    def get_dir(self):
        print("Current input directory: {}".format(self.__input_dir))
        print("Current output directory: {}".format(self.__output_dir))
