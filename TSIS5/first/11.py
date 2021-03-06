import os
info = os.stat('./doc.txt')
print(info.st_size)