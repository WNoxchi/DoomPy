# 2017-Oct-27 22:14
# pt17: Making your own Haar Cascade Intro
# https://www.youtube.com/watch?v=jG3bu0tjFbk&index=17&list=PLQVvvaa0QuDdttJXlLtAJxJetJcqmqlQq
# pt18: Gathering Images for Haar Cascade
# https://www.youtube.com/watch?v=z_6fPS5tDNU&list=PLQVvvaa0QuDdttJXlLtAJxJetJcqmqlQq&index=18
# pt19: Cleaning images and creating description files
# https://www.youtube.com/watch?v=t0HOVLK30xQ&index=19&list=PLQVvvaa0QuDdttJXlLtAJxJetJcqmqlQq

import urllib.request; import cv2; import numpy as np; import os
# print("WOOOO")

def store_raw_images():
    # run one, update pic_num, resave, comment, run other
    # neg_images_link = 'http://image-net.org/api/text/imagenet.synset.geturls?wnid=n01861778'
    neg_images_link = 'http://image-net.org/api/text/imagenet.synset.geturls?wnid=n00523513'
    neg_images_urls = urllib.request.urlopen(neg_images_link).read().decode()

    if not os.path.exists('neg'):
        os.makedirs('neg')

    # pic_num = 1 # must be past the highest num img in folder
    pic_num = 756

    for i in neg_images_urls.split('\n'):
        try:
            print(i)
            urllib.request.urlretrieve(i, 'neg/'+str(pic_num)+'.jpg')
            img = cv2.imread('neg/'+str(pic_num)+'.jpg', cv2.IMREAD_GRAYSCALE)
            resized_image = cv2.resize(img, (100,100))
            cv2.imwrite('neg/'+str(pic_num)+'.jpg', resized_image)
            pic_num += 1
        except Exception as e:
            print(str(e))

    pos_images_link = 'http://image-net.org/api/text/imagenet.synset.geturls?wnid=n03335030'

def find_uglies():
    '''removes 'ugly' placeholder images'''
    for file_type in ['neg']:
        for img in os.listdir(file_type):   # will iter thru all imgs in neg dir
            for ugly in os.listdir('ugly'):
                try:
                    current_image_path = str(file_type)+'/'+str(img)
                    ugly = cv2.imread('ugly/'+str(ugly))
                    question = cv2.imread(current_image_path)

                    # det if same image
                    if ugly.shape == question.shape and not(np.bitwise_xor(ugly,question).any()):
                        print('gdamn u ugly!')
                        os.remove(current_image_path)

                except Exception as e:
                    print(str(e))

# def find_uglies():
#     match = False
#     for file_type in ['neg']:
#         for img in os.listdir(file_type):
#             for ugly in os.listdir('ugly'):
#                 try:
#                     current_image_path = str(file_type)+'/'+str(img)
#                     ugly = cv2.imread('ugly/'+str(ugly))
#                     question = cv2.imread(current_image_path)

def create_pos_n_neg():
    '''creates neg & pos imgs description files'''
    for file_type in ['neg']:
        for img in os.listdir(file_type):
            if file_type == 'neg':  # we're in 'neg' directory anyway
                line = file_type+'/'+img+'\n'   # path of neg image
                with open('bg.txt','a') as f:
                    f.write(line)
            # not run but here as example -- createsamples does this automatically
            elif file_type == 'pos':
                line = file_type+'/'+img+' 1 0 0 50 50\n'   #1: num objs in img; 0 0 50 50: rectangle coords of obj
                with open('info.dat','a') as f:
                    f.write(line)

# run in pt18
# store_raw_images()

# run in pt19 first
find_uglies()

# run in pt19 second
create_pos_n_neg()
