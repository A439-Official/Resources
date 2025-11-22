import os
import hashlib
import json
from pathlib import Path


def sha256(file_path, chunk_size=8192):
    """SHA-256"""
    sha256_hash = hashlib.sha256()
    try:
        with open(file_path, "rb") as f:
            for chunk in iter(lambda: f.read(chunk_size), b""):
                sha256_hash.update(chunk)
        return sha256_hash.hexdigest()
    except IOError:
        print(f"文件 {file_path} 打开失败！")
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
                    print(f"正在处理文件 {file_path}...")
                    md5_value = sha256(file_path)
                    if md5_value:
                        files_list[os.path.relpath(file_path, dir_name)] = md5_value

        with open(os.path.join(dir_name, ".files.json"), "w", encoding="utf-8") as f:
            json.dump(files_list, f, indent=4)
