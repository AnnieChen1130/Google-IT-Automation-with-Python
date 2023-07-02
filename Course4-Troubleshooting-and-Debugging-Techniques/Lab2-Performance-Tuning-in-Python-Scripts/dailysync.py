#!/usr/bin/env python3
import subprocess
from multiprocessing import Pool
import os

src = "./data/prod/"
dest = "./data/prod_backup/"

def run(task):
  # Do something with task here
    #print("Handling: ", task)
    subprocess.call(["rsync", "-arq", os.path.join(src, task), dest])
if __name__ == "__main__":
  print(os.walk(src))
  tasks = []
  for (root,dirs,files) in os.walk(src, topdown=True):
      print (root)
      print (dirs)
      tasks.extend(dirs)
      #print (files)
      print ('--------------------------------')  

  # Create a pool of specific number of CPUs
  p = Pool(len(tasks))
  # Start each task within the pool     
  p.map(run, tasks)
