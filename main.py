from striprtf.striprtf import rtf_to_text
import os
import re

path_origin = 'C:/Users/anpae/Desktop/test.txt'
path_dest = 'C:/Users/anpae/Desktop/'
#name = 'guardian'
idx = 0
aux = 0


with open(path_origin, 'r') as file:
    text = file.read()
    regex = regex = re.sub(r'@[^\s]*', "", text)
    name_aux = "data" + "_" +".txt"  # name of new file
    new_filepath = os.path.join(path_dest, name_aux)
    with open(new_filepath, 'w') as f:
        f.write(regex.strip())

