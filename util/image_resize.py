import os
import argparse
import cv2
import numpy as np

from util import data_io
from util import image_edit


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("input_dir", type=str)
    parser.add_argument("output_dir", type=str)
    parser.add_argument("--resolution", type=str, choices=['VGA', 'QVGA', 'FHD', '4K'], default='VGA')
    args = parser.parse_args()
    return args


def imread(filename, flags=cv2.IMREAD_COLOR, dtype=np.uint8):
    try:
        n = np.fromfile(filename, dtype)
        img = cv2.imdecode(n, flags)
        return img
    except Exception as e:
        print(e)
        return None


def imwrite(filename, img, params=None):
    try:
        ext = os.path.splitext(filename)[1]
        result, n = cv2.imencode(ext, img, params)
        if result:
            with open(filename, mode='w+b') as f:
                n.tofile(f)
            return True
        else:
            return False
    except Exception as e:
        print(e)
        return False

def get_resize(resolution):
    if resolution == 'QVGA':
        width = 1280
        height = 960
    elif resolution == 'FHD':
        width = 1920
        height = 1080
    elif resolution == '4K':
        width = 3840
        height = 2160
    else:
        width = 640
        height = 480
    return width, height


def main(args):
    dir_list = data_io.get_dir_list(args.input_dir)
    resize_width, resize_height = get_resize(args.resolution)
    for dir in dir_list:
        dirpath = os.path.join(args.input_dir, dir)
        save_dir = os.path.join(args.output_dir, dir)
        os.makedirs(save_dir, exist_ok=True)
        file_list = data_io.get_file_list(dirpath)

        for file in file_list:
            img = imread(file)
            if img is not None:
                img = image_edit.image_resize(img, resize_width, resize_height)
                imgname = os.path.basename(file)
                filename = os.path.join(save_dir, imgname)
                imwrite(filename, img)
            else:
                print(os.path.basename(file), "resize failed.")


if __name__ == '__main__':
    main(parse_args())
