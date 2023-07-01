import re

def rearrange_name(name):
  #result = re.search(r"^(\w+), (\w+) (\w\.)$", name)
  result = re.search(r"^([\w .]*), ([\w .]*)$", name)
  if result == None:
    return name
  return "{} {}".format(result[2],result[1])

# Simple Test
name=rearrange_name("Kennedy, John F.")
print(name) #John F. Kennedy
