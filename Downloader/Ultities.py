import os, requests, hashlib

def calculate_sha1(file_path):
    sha1 = hashlib.sha1()
    with open(file_path, "rb") as f:
        while True:
            data = f.read(65536)  # 64KB buffer
            if not data:
                break
            sha1.update(data)
    return sha1.hexdigest()

def get_file(file):
    file_basename = os.path.basename(file.save_path)
    if os.path.exists(file.save_path) and calculate_sha1(file.save_path) == file.sha1:
        print(f'File {file_basename} is Already existed')
    else:
        print(f'Downloading {file_basename}...')
        content_path = os.path.split(file.save_path)[0]
        if not os.path.exists(content_path):
            os.makedirs(content_path)
        
        data = requests.get(file.url).content
        with open(file.save_path, 'wb') as f:
            f.write(data)

        if file.is_json:
            return requests.get(file.url).json()