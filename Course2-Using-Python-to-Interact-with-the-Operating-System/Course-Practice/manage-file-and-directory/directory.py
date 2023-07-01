import os

print(os.getcwd())

#os.mkdir("new_dir")
#os.chdir("new_dir")
#print(os.getcwd())

#os.mkdir("newer_dir")
#os.rmdir("newer_dir")

print(os.listdir("new_dir"))
dir = "new_dir"
for name in os.listdir(dir):
    fullname = os.path.join(dir, name)
    if os.path.isdir(fullname):
        print("{} is a directory".format(fullname))
    else:
        print("{} is a file".format(fullname))    