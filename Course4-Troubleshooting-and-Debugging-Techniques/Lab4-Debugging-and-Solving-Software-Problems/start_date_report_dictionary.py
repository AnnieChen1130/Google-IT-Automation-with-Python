#!/usr/bin/env python3


import csv
import datetime
import requests


FILE_URL = "https://storage.googleapis.com/gwg-content/gic215/employees-with-date.csv"

def get_start_date():
    """Interactively get the start date to query for."""

    print()
    print('Getting the first start date to query for.')
    print()
    print('The date must be greater than Jan 1st, 2018')
    year = int(input('Enter a value for the year: '))
    month = int(input('Enter a value for the month: '))
    day = int(input('Enter a value for the day: '))
    print()

    return datetime.datetime(year, month, day)

def get_file_lines(url):
    """Returns the lines contained in the file at the given URL"""

    # Download the file over the internet
    response = requests.get(url, stream=True)
    lines = []

    for line in response.iter_lines():
        lines.append(line.decode("UTF-8"))
    return lines
  
def get_date_employee_dict(data):
    reader = csv.reader(data[1:])
    dict = {}

    for row in reader:
        row_date = datetime.datetime.strptime(row[3], '%Y-%m-%d').date()
        employee_name = row[0] + ' ' + row[1]
        #print(row_date)
        if row_date not in dict:
            dict[row_date] = []
        dict[row_date].append(employee_name[0])
    '''
    for d,e in dict.items():
        print(f"{d}: {e}")
    '''
    return dict

def list_newer(start_date):
    data = get_file_lines(FILE_URL)
    print(data)

    dict = get_date_employee_dict(data)
    print(start_date)
    while start_date < datetime.datetime.today():
        if start_date.date() in dict:
            employees = dict[start_date.date()]
            print("Started on {}: {}".format(start_date.strftime("%b %d, %Y"), employees))

        # Now move the date to the next one
        start_date = start_date + datetime.timedelta(days=1)

def main():
    start_date = get_start_date()
    list_newer(start_date)

if __name__ == "__main__":
    main()
