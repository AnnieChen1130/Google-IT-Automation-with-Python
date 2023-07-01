import os
import datetime

with open("novel.txt", "w") as file:
    file.write("It was a dark and stormy night")

#os.rename("novel.txt", "finished.txt")
#print(os.path.exists("novel.txt"))
#print(os.path.exists("finished.txt"))

#os.remove("novel.txt")

print(os.path.getsize("spider.txt"))
print(os.path.getmtime("spider.txt"))

timestamp = os.path.getmtime("spider.txt")
print(datetime.datetime.fromtimestamp(timestamp))
print(os.path.abspath("spider.txt"))


