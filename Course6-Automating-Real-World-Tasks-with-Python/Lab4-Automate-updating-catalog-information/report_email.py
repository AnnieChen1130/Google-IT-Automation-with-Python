#!/usr/bin/env python3

import emails
import os
import reports
import requests
import datetime
import run

def fruit_dict_to_table(data):
  """Turns the data in car_data into a list of lists."""
  body_data = ""
  for item in data:
    body_data += "name: {}".format(item["name"])
    body_data += "<br/>"
    body_data += "weight: {} lbs".format(item["weight"])
    body_data += "<br/><br/>"
  return body_data

fruitListData = run.process_data()

#Title
today = datetime.datetime.today()
report_title = "Processed Update on {} {}, {}".format(today.strftime("%B"), today.day, today.year)

#Attachment
report_file = "/tmp/processed.pdf"

#generate report
reports.generate(report_file, report_title, fruit_dict_to_table(fruitListData))

# TODO: send the PDF report as an email attachment

sender = "automation@example.com"
receiver = "{}@example.com".format(os.environ.get('USER'))
subject = "Upload Completed - Online Fruit Store"
body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."

message = emails.generate(sender, receiver, subject, body, report_file)
emails.send(message)
