import os
from tqdm import tqdm

from colorama import Fore
full_paths = []
for dirpath, dirnames, filenames in os.walk("repos"):
    for file in filenames:
        full_path = os.path.join(dirpath, file)
        full_paths.append(full_path)
        if full_path.endswith(".py"):
            print(Fore.GREEN + file)
        else:
            os.remove(full_path)
            print(Fore.RED+file)
print(Fore.RESET)

MAX_CHAR_LENGTH = 512
MIN_CHAR_LENGTH = 400

with open("python_code_text_data.txt", "a", encoding='utf-8') as f:
    for fpath in full_paths:
        d = open(fpath, "r", encoding='utf-8').read()
        # print(d)
        fd = d.replace("\n\n", "<N><N>")
        if 10 < len(fd) < MAX_CHAR_LENGTH:
            f.write(fd + '\n')
        else:
            sd = fd.split( "<N><N>")
            sub_string = ''
            for split in sd:
                sub_string += split + "<N><N>"
                if 10 <= len(sub_string) <= MAX_CHAR_LENGTH:
                    f.write(sub_string + "\n")
                    sub_string = ""

