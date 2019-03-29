import argparse
import glob
import os
import numpy as np

from util import data_io
from PIL import Image


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("input_dir", type=str)
    parser.add_argument("output_dir", type=str)
    parser.add_argument("--image_ext", type=str, default="jpg")
    args = parser.parse_args()

    return args


def main(args):
    dir_list = data_io.get_dir_list(args.input_dir)
    Image_list_all = []
    Label_list_all = []
    for index, dir in enumerate(dir_list):
        dirpath = os.path.join(args.input_dir, dir)
        Image_list, Label_list = convert_image_to_npz(dirpath, index, args.image_ext)
        Image_list_all.extend(Image_list)
        Label_list_all.extend(Label_list)
    Image_list_all = np.array(Image_list_all, dtype=np.float32)
    save_file = os.path.join(args.output_dir, "np_sample")
    np.savez(save_file, x=Image_list_all, y=Label_list_all)


def convert_image_to_npz(folder, label, file_ext):
    image_list = glob.glob(os.path.join(folder, '*.%s' % file_ext))

    Im_list = []
    Lb_list = []

    for image in image_list:
        im = Image.open(image, 'r')
        im = im.convert("RGB")
        dataset = np.asarray(im)
        dataset = dataset / 256
        im.close()
        Im_list.append(dataset)
        Lb_list.append(label)
    return Im_list, Lb_list


if __name__ == '__main__':
    main(parse_args())
