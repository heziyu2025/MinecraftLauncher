import json, requests

def get_version_list():
    data = requests.get('https://launchermeta.mojang.com/mc/game/version_manifest.json').text
    data_dict = json.loads(data)
    return data_dict

version_dict = get_version_list()
lastest_verson = version_dict['latest']['release']
print(f'最新版本：{lastest_verson}')