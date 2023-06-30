#!/usr/bin/env python3

import csv

def read_employees(csv_file_location):
  #parsing CSV file
  csv.register_dialect('empDialect', skipinitialspace=True, strict=True)
  employee_file = csv.DictReader(open(csv_file_location), dialect = 'empDialect')
  
  #array list to hold dictionary data
  employee_list = []
  for data in employee_file:
    employee_list.append(data)
  return employee_list

#Check read from CSV and store data
employee_list = read_employees('employees.csv')
print(employee_list)
print()

def process_data(employee_list):
  
  #Get List of Department from employee list, department may have duplicate
  department_list = [] 
  for employee_data in employee_list:
    department_list.append(employee_data['Department'])
  
  print("------department_list------------") 
  print(department_list)  
  print()

  #uses the set() method, which converts iterable elements to distinct elements.
  #Count num of department in Department list
  #department_data is a dictionary(key-value)   
  department_data = {}
  for department_name in set(department_list):
    department_data[department_name] = department_list.count(department_name)
  return department_data

dictionary = process_data(employee_list)
print(dictionary)


def write_report(dictionary, report_file):
  with open(report_file, "w+") as f:
    for k in sorted(dictionary):
      f.write(str(k)+':'+str(dictionary[k])+'\n')
    f.close()

write_report(dictionary, 'test_report.txt')

