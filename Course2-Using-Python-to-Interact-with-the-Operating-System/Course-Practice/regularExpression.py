import re
log = "July 30 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade"
regex = r"\[(\d+)\]"
result = re.search(regex, log)
print(result)
print(result[1])

import re
def check_aei (text):
  result = re.search(r"a.e.i", text)
  return result != None

print(check_aei("academia")) # True
print(check_aei("aerial")) # False
print(check_aei("paramedic")) # True

'''
Python raw string treats the backslash character (\) as a literal character. 
Raw string is useful when a string needs to contain a backslash, 
such as for a regular expression or Windows directory path, 
and you don’t want it to be treated as an escape character.
'''

# ^  to check if a line begins with a pattern
# $  and check if it ends with a pattern
print(re.search(r"aza", "plaza"))
print(re.search(r"aza", "bazaar"))
print(re.search(r"aza", "aza"))
print(re.search(r"^x", "xenon"))
print(re.search(r"^x", "qxenon"))
print(re.search(r"p.ng", "penguin"))
print(re.search(r"p.ng", "ping"))
print(re.search(r"p.ng", "pong"))
print(re.search(r"p.ng", "Penguin", re.IGNORECASE))

#Wildcards and Character Classes
print(re.search(r"[Pp]ython", "Python"))
print(re.search(r"[a-z]way", "The end of the highway"))
print(re.search(r"[a-z]way", "What a way to go"))
print(re.search(r"[a-z]way", "What a .way to go"))
print(re.search(r".way", "The end of the highway"))
print(re.search(r".way", "What a way to go"))
print(re.search(r".way", "What a $way to go"))

print(re.search(r"cloud[a-zA-Z0-9]", "cloudy"))
print(re.search(r"cloud[a-zA-Z0-9]", "cloud9"))


def check_punctuation (text):
  result = re.search(r"[.,;:?!]", text)
  return result != None

print(check_punctuation("This is a sentence that ends with a period.")) # True
print(check_punctuation("This is a sentence fragment without a period")) # False
print(check_punctuation("Aren't regular expressions awesome?")) # True
print(check_punctuation("Wow! We're really picking up some steam now!")) # True
print(check_punctuation("End of the line")) # False

#[^] means NOT in re.search
print(re.search(r"[^a-zA-Z]", "This is a sentence with spaces.")) #find not letter
print(re.search(r"[^a-zA-Z ]", "This is a sentence with spaces."))#find not letter or space

print(re.search(r"cat|dog", "I like cats"))
print(re.search(r"cat|dog", "I like dogs"))
print(re.search(r"cat|dog", "I like cats and dogs"))
print(re.findall(r"cat|dog", "I like cats and dogs"))

print(re.search(r"Py.*n", "Pygmalion")) #* more than 1 character
print(re.search(r"Py.*n", "Python Programming"))
print(re.search(r"Py[a-z]*n", "Python Programming"))
print(re.search(r"Py[a-z]*n", "Pyn"))

#Repate Letter
print(re.search(r"o+l+", "goldfish"))
print(re.search(r"o+l+", "woolly"))
print(re.search(r"o+l+", "boil"))

'''
The repeating_letter_a function checks if the text passed includes the letter "a" 
(lowercase or uppercase) at least twice. For example, repeating_letter_a("banana") is True, 
while repeating_letter_a("pineapple") is False. 
Fill in the code to make this work. 
'''

def repeating_letter_a(text):
  result = re.search(r"[aA].*[aA]", text)
  return result != None

print(repeating_letter_a("banana")) # True
print(repeating_letter_a("pineapple")) # False
print(repeating_letter_a("Animal Kingdom")) # True
print(repeating_letter_a("A is for apple")) # True

#? character before ? is optional
print(re.search(r"p?each", "To each their own"))
print(re.search(r"p?each", "I like peaches"))

#Escaping Characters
print(re.search(r".com", "welcome"))
print(re.search(r"\.com", "welcome"))

#\w: letter, numbers, underscores
print(re.search(r"\w*", "This is an example"))
print(re.search(r"\w*", "This_is_an_example"))

#\d for digit; \s for whitespace, tab, newline; \b for word boundaries

'''
Fill in the code to check if the text passed has at least 2 groups of alphanumeric characters 
(including letters, numbers, and underscores) separated by one or more whitespace characters.
'''
def check_character_groups(text):
  result = re.search(r"\w \w", text)
  return result != None

print(check_character_groups("One")) # False
print(check_character_groups("123  Ready Set GO")) # True
print(check_character_groups("username user_01")) # True
print(check_character_groups("shopping_list: milk, bread, eggs.")) # False

'''
Fill in the code to check if the text passed looks like a standard sentence, 
meaning that it starts with an uppercase letter, 
followed by at least some lowercase letters or a space, 
and ends with a period, question mark, or exclamation point. 
'''
def check_sentence(text):
  result = re.search(r"^[A-Z][a-z ].*[.?!]$", text)
  return result != None

print(check_sentence("Is this is a sentence?")) # True
print(check_sentence("is this is a sentence?")) # False
print(check_sentence("Hello")) # False
print(check_sentence("1-2-3-GO!")) # False
print(check_sentence("A star is born.")) # True

'''
Fill in the code to check if the text passed includes a possible U.S. zip code, 
formatted as follows: exactly 5 digits, and sometimes, 
but not always, followed by a dash with 4 more digits. 
The zip code needs to be preceded by at least one space, 
and cannot be at the start of the text.
'''

def check_zip_code (text):
  result = re.search(r"[ ]\d{5}|[ ]\d{5}-\d{4}", text)
  return result != None

print(check_zip_code("The zip codes for New York are 10001 thru 11104.")) # True
print(check_zip_code("90210 is a TV show")) # False
print(check_zip_code("Their address is: 123 Main Street, Anytown, AZ 85258-0001.")) # True
print(check_zip_code("The Parliament of Canada is at 111 Wellington St, Ottawa, ON K1A0A9.")) # False

'''
The contains_acronym function checks the text for the presence of 2 or more characters or digits surrounded by parentheses, 
with at least the first character in uppercase (if it's a letter), 
returning True if the condition is met, or False otherwise. 
For example, "Instant messaging (IM) is a set of communication technologies used for text-based communication" 
should return True since (IM) satisfies the match conditions." Fill in the regular expression in this function: 
'''

def contains_acronym(text):
  pattern = r"\([A-Z0-9].*\)" 
  result = re.search(pattern, text)
  return result != None

print(contains_acronym("Instant messaging (IM) is a set of communication technologies used for text-based communication")) # True
print(contains_acronym("American Standard Code for Information Interchange (ASCII) is a character encoding standard for electronic communication")) # True
print(contains_acronym("Please do NOT enter without permission!")) # False
print(contains_acronym("PostScript is a fourth-generation programming language (4GL)")) # True
print(contains_acronym("Have fun using a self-contained underwater breathing apparatus (Scuba)!")) # True

#() group
result = re.search(r"^(\w*), (\w*)$", "Lovelace, Ada")
print(result)
print(result.groups())
print(result[0])
print(result[1])
print(result[2])

def rearrange_name(name):
  #result = re.search(r"^(\w*), (\w*) (\w\.)$", name)
  result = re.search(r"^([\w .-]*), ([\w .-]*)$", name)
  if result == None:
    return name
  return "{} {}".format(result[2],result[1])

name=rearrange_name("Kennedy, John F.")
print(name) #John F. Kennedy

#Exact number of character for a word
print(re.search(r"[a-zA-Z]{5}","a ghost"))
print(re.search(r"[a-zA-Z]{5}","a scary ghost appeared"))
print(re.findall(r"[a-zA-Z]{5}","a scary ghost appeared"))
print(re.findall(r"\b[a-zA-Z]{5}\b","a scary ghost appeared"))

#{num,num} range of num
print(re.findall(r"\w{5,10}","I really like strawberries"))
print(re.findall(r"\w{5,}","I really like strawberries"))

'''
We're working with a CSV file, which contains employee information. 
Each record has a name field, followed by a phone number field, 
and a role field. The phone number field contains U.S. phone numbers, 
and needs to be modified to the international format, 
with "+1-" in front of the phone number. Fill in the regular expression, 
using groups, to use the transform_record function to do that.
'''
def transform_record(record):
  new_record = re.sub(r",(\d{3})",r",+1-\1",record)
  return new_record

print(transform_record("Sabrina Green,802-867-5309,System Administrator")) 
# Sabrina Green,+1-802-867-5309,System Administrator

print(transform_record("Eli Jones,684-3481127,IT specialist")) 
# Eli Jones,+1-684-3481127,IT specialist

print(transform_record("Melody Daniels,846-687-7436,Programmer")) 
# Melody Daniels,+1-846-687-7436,Programmer

print(transform_record("Charlie Rivera,698-746-3357,Web Developer")) 
# Charlie Rivera,+1-698-746-3357,Web Developer

'''
The convert_phone_number function checks for a U.S. phone number format: XXX-XXX-XXXX (3 digits followed by a dash, 3 more digits followed by a dash, and 4 digits), 
and converts it to a more formal format that looks like this: (XXX) XXX-XXXX. 
Fill in the regular expression to complete this function.
'''

import re
def convert_phone_number(phone):
  result = re.sub(r"\b(\d{3})-(\d{3})-(\d{4})\b",r"(\1)\2-\3",phone)
  return result

print(convert_phone_number("My number is 212-345-9999.")) # My number is (212) 345-9999.
print(convert_phone_number("Please call 888-555-1234")) # Please call (888) 555-1234
print(convert_phone_number("123-123-12345")) # 123-123-12345
print(convert_phone_number("Phone number of Buckingham Palace is +44 303 123 7300")) # Phone number of Buckingham Palace is +44 303 123 7300

#The multi_vowel_words function returns all words with 3 or more consecutive vowels (a, e, i, o, u). Fill in the regular expression to do that.
def multi_vowel_words(text):
  pattern =r"\w+[a|e|i|o|u]{3,}\w+"
  result = re.findall(pattern, text)
  return result

print(multi_vowel_words("Life is beautiful")) 
# ['beautiful']

print(multi_vowel_words("Obviously, the queen is courageous and gracious.")) 
# ['Obviously', 'queen', 'courageous', 'gracious']

print(multi_vowel_words("The rambunctious children had to sit quietly and await their delicious dinner.")) 
# ['rambunctious', 'quietly', 'delicious']

print(multi_vowel_words("The order of a data queue is First In First Out (FIFO)")) 
# ['queue']

print(multi_vowel_words("Hello world!")) 
# []


'''
We're working with a CSV file, which contains employee information. 
Each record has a name field, followed by a phone number field, and a role field. The phone number field contains U.S. phone numbers, 
and needs to be modified to the international format, with "+1-" in front of the phone number. 
Fill in the regular expression, using groups, to use the transform_record function to do that.
'''
def transform_record(record):
  new_record = re.sub(r",(\d{3})",r",+1-\1",record)
  return new_record

print(transform_record("Sabrina Green,802-867-5309,System Administrator")) 
# Sabrina Green,+1-802-867-5309,System Administrator

print(transform_record("Eli Jones,684-3481127,IT specialist")) 
# Eli Jones,+1-684-3481127,IT specialist

print(transform_record("Melody Daniels,846-687-7436,Programmer")) 
# Melody Daniels,+1-846-687-7436,Programmer

print(transform_record("Charlie Rivera,698-746-3357,Web Developer")) 
# Charlie Rivera,+1-698-746-3357,Web Developer

''''''
#We're using the same syslog, and we want to display the date, time, and process id 
# that's inside the square brackets. We can read each line of the syslog and pass the contents to the show_time_of_pid function. 
# Fill in the gaps to extract the date, time, and process id from the passed line, and return this format: Jul 6 14:01:23 pid:29440.


def show_time_of_pid(line):
  pattern = r"([a-zA-Z]+ \d+ \d+:\d+:\d+).*\[(\d+)\]\:"
  result = re.search(pattern, line)
  print(result)
  print(result[1], result[2])
  return "{} pid:{}".format(result.group(1), result.group(2))

print(show_time_of_pid("Jul 6 14:01:23 computer.name CRON[29440]: USER (good_user)")) # Jul 6 14:01:23 pid:29440

print(show_time_of_pid("Jul 6 14:02:08 computer.name jam_tag=psim[29187]: (UUID:006)")) # Jul 6 14:02:08 pid:29187

print(show_time_of_pid("Jul 6 14:02:09 computer.name jam_tag=psim[29187]: (UUID:007)")) # Jul 6 14:02:09 pid:29187

print(show_time_of_pid("Jul 6 14:03:01 computer.name CRON[29440]: USER (naughty_user)")) # Jul 6 14:03:01 pid:29440

print(show_time_of_pid("Jul 6 14:03:40 computer.name cacheclient[29807]: start syncing from \"0xDEADBEEF\"")) # Jul 6 14:03:40 pid:29807

print(show_time_of_pid("Jul 6 14:04:01 computer.name CRON[29440]: USER (naughty_user)")) # Jul 6 14:04:01 pid:29440

print(show_time_of_pid("Jul 6 14:05:01 computer.name CRON[29440]: USER (naughty_user)")) # Jul 6 14:05:01 pid:29440