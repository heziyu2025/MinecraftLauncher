import threading, os, requests, tqdm
from time import sleep

class File:
    def __init__(self, url: str, save_path: str, is_json: bool = False) -> None:
        self.url = url
        self.save_path = save_path
        self.is_json = is_json

class downloader:
    def __init__(self, file_list, max_thread = 8):
        thread_list = []
        for i in range(max_thread):
            thread_list.append(threading.Thread(target=self.get_file))

        for file in tqdm(file_list):
            found = False
            while not found:
                for thread in thread_list:
                    if not thread.is_alive():
                        thread._args = (file)
                        thread.start()
                        found = True
                        break

                if not found:
                    sleep(0.1)
    