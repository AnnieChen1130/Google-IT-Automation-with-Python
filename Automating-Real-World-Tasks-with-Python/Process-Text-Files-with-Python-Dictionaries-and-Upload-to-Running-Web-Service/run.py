#!/usr/bin/env python3
import os
import requests

feedbackList = []
fields =['title', 'name', 'date', 'feedback']

source_dir = "/data/feedback"
for filename in os.listdir(source_dir): #listdir returns only the file names
    print(filename)
    with open(os.path.join(source_dir, filename)) as file:
        feedbakc_dict = {}
        for i,line in enumerate(file):
            print(line)
            feedbakc_dict[fields[i]] = line.strip('\n')
        feedbackList.append(feedbakc_dict)

print(feedbackList)

for feedback in feedbackList:
    response = requests.post("http://34.171.223.201/feedback/", json=feedback)
    response.raise_for_status()
    print(response.ok)
    print(response.status_code)
