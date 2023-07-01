file = open("spider.txt")
print(file.readline())
print(file.read())
file.close()

print("-------------")
with open("spider.txt") as file:
    print(file.read())


print("-------------")
with open("spider.txt") as file:
    for line in file:
        print(line.upper())   


print("-------------")
with open("spider.txt") as file:
    for line in file:
        print(line.strip().upper())     

print("-------------")
file = open("spider.txt")
lines = file.readlines()
file.close

print(lines)