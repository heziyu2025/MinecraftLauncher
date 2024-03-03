from .Ultities import get_file, check_rules

def install_version(url, version_name):
    from . import File, downloader

    json_file = File(url, 
                     f'.minecraft/versions/{version_name}/{version_name}.json', 
                     is_json=True)
    info_dict = get_file(json_file)

    assets = info_dict['assets']
    assets_file = File(info_dict['assetIndex']['url'],
                       f'.minecraft/assets/indexes/{assets}.json', 
                       is_json=True,
                       sha1=info_dict['assetIndex']['sha1'])
    assets_index_file = get_file(assets_file)

    
    jar_file = File(info_dict['downloads']['client']['url'],
                    f'.minecraft/versions/{version_name}/{version_name}.jar',
                    sha1=info_dict['downloads']['client']['sha1'])
    
    file_list = [jar_file]

    for lib in info_dict['libraries']:
        if check_rules(lib['rules']):
            path = lib['downloads']['artifact']['path']
            full_path = f'.minecraft/libraries/{path}'
            
            url = lib['downloads']['artifact']['url']
            sha1 = lib['downloads']['artifact']['sha1']
            file_list.append(File(url, full_path, sha1))

    downloader(file_list)