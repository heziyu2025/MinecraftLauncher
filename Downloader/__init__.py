import threading, os, requests
from time import sleep
from tqdm import tqdm

from .InstallVersion import install_version

class File:
    def __init__(self, url: str, save_path: str, is_json: bool = False) -> None:
        self.url = url
        self.save_path = save_path
        self.is_json = is_json

class downloader:
    def get_file(self, old_thread, file):
        content_path = os.path.split(file.save_path)[0]
        if not os.path.exists(content_path):
            os.makedirs(content_path)
        
        data = requests.get(file.url).content
        with open(file.save_path, 'wb') as f:
            f.write(data)

        if not len(self.file_list) == 0:
            self.thread_list.remove(old_thread)

            new_thread = threading.Thread(target=self.get_file, args=((self.file_list[0],)))
            new_thread._args = (new_thread, self.file_list[0])
            new_thread.start()

            self.thread_list.append(new_thread)
            self.file_list.pop()

    def __init__(self, file_list, max_thread = 8):
        self.file_list = file_list

        self.thread_list = []
        for i in range(max_thread):
            thread = threading.Thread(target=self.get_file)
            thread._args = (thread, self.file_list[0])
            thread.start()
            self.thread_list.append(thread)
            self.file_list.pop(0)

def get_version_list():
    return requests.get('https://launchermeta.mojang.com/mc/game/version_manifest.json').json()
    