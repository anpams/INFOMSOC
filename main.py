import os
import re

path_origin = 'C:/Users/anpae/Desktop/Data_Rtf/all/'
path_dest = 'C:/Users/anpae/Desktop/Data_Rtf/aux_folder'

idx = 0
aux = 0

for filename in os.listdir(path_origin):
    filepath = os.path.join(path_origin, filename)
    if os.path.isfile(filepath):
        with open(filepath, 'r') as file:
            text = file.read()
            if text[0:5] != "[Loca":
                # regex = re.sub(r'\.;', ".", text)
                test = re.findall(r'GMT', text)
                if (test != ""):
                    print(filename)
                    # print(re.search(r';', text).group())
                num = str(idx)
                # name_aux = name + "_" + num + ".txt"  # name of new file
                new_filepath = os.path.join(path_dest, filename)
                with open(filepath, 'w') as f:
                    # f.write(regex.strip())

                    idx += 1
                    # print(".")
