from . import File
import os, requests

def get_file(file: File):
    content_path = os.path.split(file.save_path)[0]
    if not os.path.exists(content_path):
        os.makedirs(content_path)
    
    data = requests.get(file.url).content
    with open(file.save_path, 'wb') as f:
        f.write(data)

    if file.is_json:
        return requests.get(file.url).json()