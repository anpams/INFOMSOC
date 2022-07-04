from striprtf.striprtf import rtf_to_text
import os
import re

path_origin = 'C:/Users/anpae/Desktop/Data_Rtf/all/'
path_dest = 'C:/Users/anpae/Desktop/Data_Rtf/allAux'
#name = 'guardian'
idx = 0
aux = 0

for filename in os.listdir(path_origin):
    filepath = os.path.join(path_origin, filename)
    if os.path.isfile(filepath):
        with open(filepath, 'r') as file:
            text = file.read()
            if text[0:5] != "[Loca":
                if text[0:5] == "The G":
                    regex = re.sub(r'The Guardian\n', "The Guardian;", text)
                    name='guardian'
                elif text[0:5] == "The D":
                    regex = regex = re.sub(r'Telegraph\s\W\w*\W\n', "Telegraph;", text)
                    name='telegraph'
                elif text[0:5] == "The S":
                    regex = regex = re.sub(r'Sun\s\W\w*\W\n', "Sun;", text)
                    name='sun'
                elif text[0:5] == "Daily":
                    regex = regex = re.sub(r'Mirror\n', "Mirror;", text)
                    name = 'Mirror'
                #print(regex)
                num = str(idx)
                name_aux = name + "_" + num + ".txt"  # name of new file
                new_filepath = os.path.join(path_dest, name_aux)
                with open(new_filepath, 'w') as f:
                    f.write(regex.strip())
                    idx += 1
                    print(".")
