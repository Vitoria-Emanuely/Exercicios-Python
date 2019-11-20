import os, platform

print(platform.system())
if platform.system() == "Windows":
    os.system("dir")
elif platform.system() == "Linux":
    os.system("ls")


