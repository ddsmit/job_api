import json
import pathlib
import os

def get_config():
    path = list(pathlib.Path('').rglob('parameters'))[0]
    config_file_paths = [
        file_path for file_path in path.glob('*.json')
        if 'template' not in file_path.stem.lower()
    ]
    if config_file_paths:
        config_file_path = config_file_paths[0]
        return json.load(open(config_file_path))
    else:
        return os.environ

def source():
    db = get_config()['db']
    if db == 'mongo':
        from services.mongo import get, post, update, delete
        return get, post, update, delete
    elif db == 'postgres':
        from services.mongo import get, post, update, delete
        return get, post, update, delete



