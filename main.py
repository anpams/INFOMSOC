from striprtf.striprtf import rtf_to_text
import os
import re

path_origin = 'C:/Users/anpae/Desktop/Data_Rtf/MirrGuard_NoDuplicates/'
path_dest = 'C:/Users/anpae/Desktop/Data_Rtf/guardian_txt'
name = 'mirrGuard'
idx = 0
aux = 0

# regex="\b(Sunday|Monday|Tuesday|Wednesday|Friday|Saturday).*\n*\b\b.*\n*.*\n*\W*\w*\b\W*\bByline.*\b\W*\bBody"gm


for filename in os.listdir(path_origin):
    filepath = os.path.join(path_origin, filename)
    if os.path.isfile(filepath):
        with open(filepath, 'r') as file:
            rtf_file = file.read()  # rtf to txt
            text = rtf_to_text(rtf_file) # writes to file
            if (text[0:5] != "[Loca"):
                num = str(idx)
                name_aux = name + "_"+num +".txt"  # name of new file
                new_filepath = os.path.join(path_dest, name_aux)
                with open(new_filepath, 'w') as f:
                    f.write(text.strip())
                    idx += 1
                    print(".")

