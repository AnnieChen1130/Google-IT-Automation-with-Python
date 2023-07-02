#!/usr/bin/env python3

import os
from PIL import Image

source_dir = "supplier-data/images"
#output_dir = "/opt/icons/"

for filename in os.listdir(source_dir):
    if filename.endswith('.tiff'):
        im = Image.open(os.path.join(source_dir, filename))
        im = im.resize((600,400)).convert("RGB")
        im.save(os.path.join(source_dir, filename.split(".")[0]+".jpeg"))
