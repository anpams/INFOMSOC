from striprtf.striprtf import rtf_to_text
import os
import re

path_origin = 'C:/Users/anpae/Desktop/Data_Rtf/guardian2/'
path_dest = 'C:/Users/anpae/Desktop/Data_Rtf/guardian1'
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
                else:
                    regex = regex = re.sub(r'Mirror\n', "Mirror;", text)
                    name='mirror'
                #print(regex)
                num = str(idx)
                name_aux = name + "_" + num + ".txt"  # name of new file
                new_filepath = os.path.join(path_dest, name_aux)
                with open(new_filepath, 'w') as f:
                    f.write(regex.strip())
                    idx += 1
                    print(".")
