import os
import hashlib
import json
from pathlib import Path


def calculate_md5(file_path):
    """计算文件的MD5值"""
    hash_md5 = hashlib.md5()
    try:
        with open(file_path, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)
        return hash_md5.hexdigest()
    except Exception as e:
        print(f"错误：无法读取文件 {file_path} - {e}")
        return None


if __name__ == "__main__":
    for dir_name in os.listdir("."):
        if not os.path.isdir(dir_name) or dir_name.startswith("."):
            continue

        files_list = {}

        for root, dirs, files in os.walk(dir_name):
            for file_name in files:
                if not file_name.startswith("."):
                    file_path = os.path.join(root, file_name)
                    md5_value = calculate_md5(file_path)
                    if md5_value:
                        files_list[os.path.relpath(file_path, dir_name)] = md5_value

        with open(os.path.join(dir_name, ".files.json"), "w", encoding="utf-8") as f:
            json.dump(files_list, f, indent=4)
