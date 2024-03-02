import requests, os, hashlib
from tqdm import tqdm

def get_version_list():
    data_dict = requests.get('https://launchermeta.mojang.com/mc/game/version_manifest.json').json()
    return data_dict
