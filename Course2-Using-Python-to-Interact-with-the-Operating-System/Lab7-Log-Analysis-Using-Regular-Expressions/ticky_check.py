'''#!/usr/bin/env python3'''
import re
import csv
import operator
import sys

def readFile(log_file):
  logInfo = []
  with open(log_file, mode='r',encoding='UTF-8') as file:
    for log in file.readlines():
      logInfo.append(log.strip())
    #print(logInfo)
  return logInfo  

def errorRank(logInfo):
  error_dictionary ={}
  error_pattern = r"(ERROR) ([\w]+ [^\[\(]*)"

  for logLine in logInfo:
    #print(logLine)
    error = re.search(error_pattern, logLine)
    #print(error)
    if error is None:
      continue

    error = error.group(2)
    if error in error_dictionary:
       error_dictionary[error] += 1
    else:
       error_dictionary[error] = 1   

  print(error_dictionary)

  return sorted(error_dictionary.items(), key = operator.itemgetter(1), reverse=True)

def user_statistics(logInfo):
   user_dictionary = {}
   user_pattern = r"\(([\w.]+)\)"
   infoType = r"ticky: INFO "
   errorType = r"ticky: ERROR "

   for logLine in logInfo:
      username = re.search(user_pattern, logLine)
      #print(username)
      if username is None:
        continue
      
      username = username.group(1)
      if username[1] not in user_dictionary:
        user_dictionary[username[1]] = [0,0]
      if re.search(infoType, logLine) is not None:
        user_dictionary[username[1]][0] += 1
      if re.search(errorType, logLine) is not None:
        user_dictionary[username[1]][1] += 1  

   return sorted(user_dictionary.items(), key = operator.itemgetter(0))


def write_report(set, report_file):

    if re.search("error", report_file) is not None:
       keys = [("Error", "Count")]
       with open(report_file, 'w+', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(keys)
            writer.writerows(set)

    if re.search("user", report_file) is not None:
       keys = [("Username", "INFO", "ERROR")]        
       with open(report_file, 'w+', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(keys)
            for item in set:
                key, values = item
                writer.writerow([key] + values)

if __name__ == "__main__":

  log_file = r'Final_Project\syslog.log'
  logInfo = readFile(log_file)
  errorDic = errorRank(logInfo)
  write_report(errorDic, r'Final_Project\error_message.csv')
  userDic = user_statistics(logInfo)
  write_report(userDic, r'Final_Project\user_statistics.csv')

  sys.exit(0)