# coding:utf-8
from __future__ import absolute_import
import argparse
import os
import traceback
import random
from glob import glob
import json


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--sz-dir', default='data/sz')
    args = parser.parse_args()
    return args


def main(args):
    label_file = os.path.join(args.sz_dir, 'label.idl')
    new_label_file = os.path.join(args.sz_dir, 'label_lights.idl')
    origin_label_id = 20

    with open(label_file) as f:
        with open(new_label_file, 'w') as save_f:
            for line in f:
                j = json.loads(line)
                key = None
                for x in j:
                    key = x
                    break
                write_json = None
                write_json = {key: []}
                for bbox in j[key]:
                    """我们只要特定的类别"""
                    if bbox[4] == origin_label_id:
                        """如果修改类别号，在这里修改即可"""
                        bbox[4] = 1
                        write_json[key].append(bbox)
                # print('----------')
                # print(json.dumps(write_json))
                # print('---------')
                save_f.write(json.dumps(write_json))
                save_f.write('\n')

if __name__ == '__main__':
    args = parse_args()
    main(args)
    print('done.')
