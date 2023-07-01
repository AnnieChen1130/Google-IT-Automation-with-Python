import csv

'''
file = open("csv_file.txt")
csv_f = csv.reader(file)
    
for row in csv_f:
    name, phone, role = row        
    print(name, phone, role)

file.close()
'''

#write and read csv file without header
'''
hosts = [["local", "192.168.25.46"], ["cloud", "10.2.5.6"]]
with open('hosts.csv', 'w', newline='') as hosts_csv:
    writer = csv.writer(hosts_csv)
    writer.writerows(hosts)

with open('hosts.csv') as file:
    reader = csv.reader(file)
    for row in reader:
        location, address = row
        print(location, address)
'''

#write and read csv file with header
'''
software = [["name", "version","status","users"], ["Mike", "10.6","production", "324"], 
            ["Cal", "1.2","beta", "22"], ["Lili", "0.52","alpha", "9"]]
with open('software.csv', 'w', newline='') as software_csv:
    writer = csv.writer(software_csv)
    writer.writerows(software)

with open('software.csv') as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(("{} has {} users").format(row["name"], row["users"]))        
'''

#write and read csv file with dictionary format
users = [{"name":"Sol", "username":"solm", "department":"IT"},
         {"name":"Lio", "username":"lion", "department":"UX"},
         {"name":"Char", "username":"greyC", "department":"Dev"}]
keys = ["name", "username", "department"]

#!!!!The csv.writer module directly controls line endings and writes \r\n into the file directly. In Python 3 the file must be opened in untranslated text mode with the parameters 'w', newline='' (empty string) or it will write \r\r\n on Windows, where the default text mode will translate each \n into \r\n.
with open('department.csv', 'w', newline='') as dep:
    writer = csv.DictWriter(dep, fieldnames=keys)
    writer.writeheader()
    writer.writerows(users)

with open('department.csv') as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)    







