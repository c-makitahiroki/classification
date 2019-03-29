import os
import glob


def get_file_list(dir_path, ext=""):
    path = dir_path + R"\*" + ext
    file_list = glob.glob(path)

    return file_list


def get_dir_list(dir_path):
    files = os.listdir(dir_path)
    dir_list = [f for f in files if os.path.isdir(os.path.join(dir_path, f))]

    return dir_list
