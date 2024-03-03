import threading, requests

from .InstallVersion import install_version
from.Ultities import get_file

class File:
    def __init__(self, url: str, save_path: str, sha1 = None, is_json: bool = False) -> None:
        self.url = url
        self.save_path = save_path
        self.sha1 = sha1
        self.is_json = is_json

class downloader:
    def get_file_thread(self, old_thread, file):
        get_file(file)

        if len(self.file_list) != 0:
            new_file = self.file_list[0]
            self.file_list.pop()

            self.thread_list.remove(old_thread)

            new_thread = threading.Thread(target=self.get_file_thread, args=((new_file,)))
            new_thread._args = (new_thread, new_file)
            new_thread.start()

            self.thread_list.append(new_thread)

    def __init__(self, file_list, max_thread = 8):
        self.file_list = file_list

        self.thread_list = []
        for i in range(max_thread):
            thread = threading.Thread(target=self.get_file_thread)
            thread._args = (thread, self.file_list[0])
            thread.start()
            self.thread_list.append(thread)
            self.file_list.pop(0)

def get_version_list():
    return requests.get('https://launchermeta.mojang.com/mc/game/version_manifest.json').json()
    