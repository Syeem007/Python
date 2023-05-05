import os
import re

directory = r"C:\Users\MD00875297\Desktop\merzed"

os.chdir(directory)

pattern1=r"F23046BH"
pattern2=r"F32046B"
with open("merged.txt", "r") as outfile:
    output = outfile.read()
    print(output)
    if pattern1 in output:
        print(re.search(pattern1))
    if pattern2 in output:
        print(re.search(pattern2))

