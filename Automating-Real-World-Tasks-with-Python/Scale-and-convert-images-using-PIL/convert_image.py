#!/usr/bin/env python3
import os
from PIL import Image

source_dir = "images/"
output_dir = "/opt/icons/"

for filename in os.listdir(directory):
    if not filename.startswith('.'):
        im = Image.open(os.path.join(source_dir, filename))
        im = im.rotate(90).resize((128,128)).convert("RGB")
        im.save(os.path.join(output_dir, filename+".jpeg"))
