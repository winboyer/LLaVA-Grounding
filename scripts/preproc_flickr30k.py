import os
import pandas as pd
import json
import shutil

root_dir = '/root/jinyfeng/datas/llava-grounding/flickr30k_entities'
token_path = os.path.join(root_dir, 'results_20130124.token')
# annotations = pd.read_table(token_path, sep='\t', header=None, names=['image', 'caption'])
# print(annotations)
# print(annotations['caption'])

train_json_file = os.path.join(root_dir, 'annotations/final_flickr_separateGT_train.json')
val_json_file = os.path.join(root_dir, 'annotations/final_flickr_separateGT_val.json')
test_json_file = os.path.join(root_dir, 'annotations/final_flickr_separateGT_test.json')

image_folder = os.path.join(root_dir, 'flickr30k-images')

train_folder = os.path.join(root_dir, 'train')
val_folder = os.path.join(root_dir, 'val')
test_folder = os.path.join(root_dir, 'test')

if not os.path.exists(train_folder):
    os.makedirs(train_folder)
if not os.path.exists(val_folder):
    os.makedirs(val_folder)
if not os.path.exists(test_folder):
    os.makedirs(test_folder)

with open(test_json_file) as json_file:
    parsed_json = json.load(json_file)

print(len(parsed_json['images']))
print(len(parsed_json['annotations']))
print(len(parsed_json['categories']))

for imageInfo in parsed_json['images']:
    filename = imageInfo['file_name']
    # print(filename)
    from_path = os.path.join(image_folder, filename)
    if not os.path.exists(from_path):
        print(filename, ' not exist')
    shutil.copy(from_path, test_folder)

