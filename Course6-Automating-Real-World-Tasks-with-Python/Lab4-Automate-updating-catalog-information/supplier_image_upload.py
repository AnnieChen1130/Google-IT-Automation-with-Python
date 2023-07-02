
#!/usr/bin/env python3

import os
import requests

source_dir = "supplier-data/images"
url = "http://localhost/upload/"
for image in os.listdir(source_dir):
    if image.endswith('.jpeg'):
        print(image)
        image_path = os.path.join(source_dir, image)  # Get the full path of image
        with open(image_path, 'rb') as opened:
            r = requests.post(url, files={'file': opened})
            r.raise_for_status
