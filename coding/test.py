import os
dir = "../images"
for file in os.listdir(dir):
    f = file.split('.')
    print(f[0])