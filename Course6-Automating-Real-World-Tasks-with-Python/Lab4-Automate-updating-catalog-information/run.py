#! /usr/bin/env python3
import os
import locale
import requests

def process_data():
    fruitList = []
    fruitName = []
    fields =['name', 'weight', 'description', 'image_name']

    source_dir = "supplier-data/descriptions/"
    for filename in os.listdir(source_dir): #listdir returns only the file names
        #print(filename)
        with open(os.path.join(source_dir, filename)) as file:
            fruit_dict = {}
            for i,line in enumerate(file):
                #print(line)
                fruit_dict[fields[i]] = line.strip('\n')

            fruit_dict["weight"] = locale.atof(fruit_dict["weight"].strip("lbs"))
            fruitList.append(fruit_dict)
            fruitName.append(fruit_dict["name"])

    for fruit in fruitList:
        if fruit["name"] == "Apple":
            fruit["image_name"] = "001.jpeg"
        if fruit["name"] == "Avocado":
            fruit["image_name"] = "002.jpeg"
        if fruit["name"] == "Blackberry":
            fruit["image_name"] = "003.jpeg"
        if fruit["name"] == "Grape":
            fruit["image_name"] = "004.jpeg"
        if fruit["name"] == "Kiwifruit":
            fruit["image_name"] = "005.jpeg"
        if fruit["name"] == "Lemon":
            fruit["image_name"] = "006.jpeg"
        if fruit["name"] == "Mango":
            fruit["image_name"] = "007.jpeg"
        if fruit["name"] == "Plum":
            fruit["image_name"] = "008.jpeg"
        if fruit["name"] == "Strawberry":
            fruit["image_name"] = "009.jpeg"
        if fruit["name"] == "Watermelon":
            fruit["image_name"] = "010.jpeg"

    #print(fruitList)
    # print(fruitName)

fruitList = process_data()


for fruit in fruitList:
    print(fruit)
    response = requests.post("http://35.232.132.98/fruits/", json=fruit)
    response.raise_for_status()
    print(response.ok)
    print(response.status_code)



