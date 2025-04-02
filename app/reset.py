import shutil

if __name__ == '__main__':
    _path = "app/core/"
    shutil.copyfile(f'{_path}freshdb.json', f'{_path}db.json')
