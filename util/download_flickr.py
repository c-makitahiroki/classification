import argparse
import os
import time
import traceback
import sys
import numpy as np
import pandas as pd
import json
import codecs

from flickrapi import FlickrAPI
from urllib.request import urlretrieve


def parse_args():
    parser = argparse.ArgumentParser(description="Process some integers.")
    parser.add_argument("setting_file", type=str)
    parser.add_argument("keyword_list", type=str)
    parser.add_argument("output_dir", type=str)
    args = parser.parse_args()
    return args


def load_flickrInfo(setting_file):
    f = open(setting_file, 'r')
    jsonData = json.load(f)
    print(jsonData['Flickrkeys']['key'])
    return jsonData['Flickrkeys']['key'], jsonData['Flickrkeys']['secret']


def load_keywords(keyword_list):
    with codecs.open(keyword_list, 'r', 'UTF-8', 'ignore') as file:
        keyword_list = pd.read_csv(file, header=0)
    word_list = np.array(keyword_list['keyword'])
    data_page = np.array(keyword_list['count'])
    return word_list, data_page


def search_image(word_list, data_list, output_dir, flickr):
    def _save_image(photos, save_dir):
        def _get_image(url, filepath):
            urlretrieve(url, filepath)
            time.sleep(1)

        if not os.path.exists(save_dir):
            os.mkdir(save_dir)
        for photo in photos['photo']:
            if 'url_o' in photo:
                url = photo['url_o']
                filepath = os.path.join(save_dir, photo['id'] + ".jpg")
                _get_image(url, filepath)

    for word, data in zip(word_list, data_list):
        photos_dir = os.path.join(output_dir, word)
        result = flickr.photos.search(text=word,
                                      per_page=data,
                                      media='photos',
                                      sort='relevance',
                                      safe_search=1,
                                      extras='url_o, license'
                                      )
        photos = result['photos']
        _save_image(photos, photos_dir)


def main(args):
    key, secret = load_flickrInfo(args.setting_file)
    word, data = load_keywords(args.keyword_list)
    flickr = FlickrAPI(key, secret, format='parsed-json')
    search_image(word, data, args.output_dir, flickr)


if __name__ == "__main__":
    main(parse_args())
