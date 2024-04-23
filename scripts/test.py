import os

path = '/root/jinyfeng/datas/llava-grounding/flickr30k_entities/flickr30k-images'

#####  '4797050581.jpg' not in test folder


filenames = os.listdir(path)
print(len(filenames))

train_path = '/root/jinyfeng/datas/llava-grounding/flickr30k_entities/train'
val_path = '/root/jinyfeng/datas/llava-grounding/flickr30k_entities/val'
test_path = '/root/jinyfeng/datas/llava-grounding/flickr30k_entities/test'
for filename in filenames:
    filepath = os.path.join(train_path, filename)
    if not os.path.exists(filepath):
        filepath = os.path.join(val_path, filename)
        if not os.path.exists(filepath):
            filepath = os.path.join(test_path, filename)
            if not os.path.exists(filepath):
                print(filename, 'not in folder')
