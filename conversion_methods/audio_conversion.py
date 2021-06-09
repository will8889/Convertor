# Used to convert an audio file from 1 type to another

from pydub import AudioSegment
from pydub.utils import mediainfo

class AudioConvertor:

    def __init__(self, input_dir, output_dir):
        self.__input_dir = input_dir
        self.__output_dir = output_dir
        self.__extensions = ["mp3","wav","ogg","flac","mp4"] # Supported file types 
        self.__bitrate_low = "64k"
        self.__bitrate_medium = "128k"
        self.__bitrate_high = "256k"
     
    # Extract file name 
    def __extract_file_name(self, name):
        temp = name.split(".")
        out = ""
        for i in range(len(temp)-1):
            out += temp[i]
            if i != len(temp)-2:
                out += "."

        return out

    # The actual convertion function
    def convert(self, file_name, target, bitrate = "high"):
        if file_name.split(".")[-1] not in self.__extensions:
            print("File type must either be mp3, wav, ogg, flac or mp4")

        elif target not in self.__extensions or target =="mp4":
            print("Target file type must either be mp3, wav, ogg or flac")

        else:
            file_dir = self.__input_dir + "/" + file_name 
            temp_name = self.__extract_file_name(file_name)
            converted_dir = self.__output_dir + "/" + temp_name + "." + target
            file_audio = AudioSegment.from_file(file_dir)

            if target in ["flac", "wav"]:
                file_audio.export(converted_dir,format = target)
            
            else:
                if bitrate.lower() == "low":
                    file_audio.export(converted_dir, format = target, bitrate=self.__bitrate_low)
                elif bitrate.lower() == "medium":
                    file_audio.export(converted_dir, format = target, bitrate=self.__bitrate_medium)
                else:
                    file_audio.export(converted_dir, format = target, bitrate=self.__bitrate_high)

            return self.__extract_file_name(file_name) + "." + target

    def set_dir(self, input_dir = None, output_dir = None):
        if input_dir != None:
            self.__input_dir = input_dir
        if output_dir != None:
            self.__output_dir = output_dir

    def get_dir(self):
        print("Current input directory: {}".format(self.__input_dir))
        print("Current output directory: {}".format(self.__output_dir))



        

    

