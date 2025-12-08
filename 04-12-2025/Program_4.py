# delete the file
import os
if os.path.exists("file.txt"):
    os.remove("file.txt")
    print("File deleted sucessfully")
else:
    print("File not found")
