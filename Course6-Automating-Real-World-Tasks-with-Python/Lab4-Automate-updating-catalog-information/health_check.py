#!/usr/bin/env python3

import psutil
import shutil
import os
import emails


#CPU usage is over 80%
def check_cpu_usage():
    cpu = psutil.cpu_percent(1)
    return cpu > 80

#Available disk space is lower than 20%
def check_disk_usage():
    percent = psutil.disk_usage('/').percent
    return percent > 80

#Available memory is less than 500MB
def check_memoru_usage():
    free_mem = psutil.virtual_memory().free /1024 /1024
    return free_mem < 500

#hostname "localhost" cannot be resolved to "127.0.0.1"
def resolve_hostname():
    hostname = socket.gethostbyname('localhost')
    return hostname == '127.0.0.1'

if __name__ == "__main__":

    sender = "automation@example.com"
    receiver = "{}@example.com".format(os.environ.get('USER'))
    subject = ""
    body = "Please check your system and resolve the issue as soon as possible."

    if check_cpu_usage:
        subject = "Error - CPU usage is over 80%"
        message = emails.generate(sender, receiver, subject, body)
        emails.send(message)

    if check_disk_usage:
        subject = "Error - Available disk space is less than 20%"
        message = emails.generate(sender, receiver, subject, body)
        emails.send(message)

    if check_memoru_usage:
        subject = "Error - Available memory is less than 500MB"
        message = emails.generate(sender, receiver, subject, body)
        emails.send(message)

    if resolve_hostname:
        subject = "Error - localhost cannot be resolved to 127.0.0.1"
        message = emails.generate(sender, receiver, subject, body)
        emails.send(message)

'''
#CPU usage is over 80%
if(psutil.cpu_percent(1) > 80):
    subject = "Error - CPU usage is over 80%"
    message = emails.generate_basic_email(sender, receiver, subject, body)
    emails.send(message)

#Available disk space is lower than 20%
if(psutil.disk_usage('/').percent > 80):
    subject = "Error - Available disk space is less than 20%"
    message = emails.generate_basic_email(sender, receiver, subject, body)
    emails.send(message)

#Available memory is less than 500MB
if(psutil.virtual_memory().free < 5*10**8):
    subject = "Error - Available memory is less than 500MB"
    message = emails.generate_basic_email(sender, receiver, subject, body)
    emails.send(message)

#hostname "localhost" cannot be resolved to "127.0.0.1"

#Error - localhost cannot be resolved to 127.0.0.1

'''
