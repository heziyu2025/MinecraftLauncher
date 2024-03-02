from . import File, downloader
from .Ultities import get_file

import requests, os

# def calculate_sha1(file_path):
#     sha1 = hashlib.sha1()
#     with open(file_path, "rb") as f:
#         while True:
#             data = f.read(65536)  # 64KB buffer
#             if not data:
#                 break
#             sha1.update(data)
#     return sha1.hexdigest()

def install_version(url, version_name):
    print('Downloading json file...')
    info_dict = get_file(url, 
                         f'.minecraft/versions/{version_name}/{version_name}.json', 
                         is_json=True)

    print('Downloading assets index file...')
    assets = info_dict['assets']
    assets_index_file = get_file(info_dict['assetIndex']['url'],
                           f'.minecraft/assets/indexes/{assets}.json', 
                           is_json=True)

    jar_file = File(info_dict['downloads']['client']['url'],
                    f'.minecraft/versions/{version_name}/{version_name}.jar')
    
    file_list = [jar_file]

    for lib in info_dict['libraries']:
        # if os.path.exists(lib['downloads']['artifact']['path']) and calculate_sha1(lib['downloads']['artifact']['path']) == lib['downloads']['artifact']['hash']:
        #     continue

        path = lib['downloads']['artifact']['path']
        full_path = f'.minecraft/libraries/{path}'
        url = lib['downloads']['artifact']['url']
        file_list.append(File(url, full_path))

    downloader(file_list)

install_version('https://piston-meta.mojang.com/v1/packages/dc6fd93b4a4856000343557281a47c27192cdd3b/24w09a.json', 'aaa')