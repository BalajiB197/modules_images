from PIL import Image
from glob import glob
import os
import argparse

def j2p(path):
    '''
    converts jpg to png images in a bulk.
    args : image folder path
    output: converts and saves in the same folder path tagged with converted
    return: success status of function call
    '''
    image_files = glob(os.path.join(path, '*.jpg'))
    for index, filename in enumerate(image_files):
        img = Image.open(filename).convert('RGB')
        img.save('./images/converted_'+str(index)+'.png', 'png')
    return True

def p2j(path):
    '''
    converts png to jpg images in a bulk.
    args : image folder path
    output: converts and saves in the same folder path tagged with converted
    return: success status of function call
    '''
    image_files = glob(os.path.join(path, '*.png'))
    for index, filename in enumerate(image_files):
        img = Image.open(filename).convert('RGB')
        img.save('./images/converted_'+str(index)+'.jpg', 'jpeg')
    return True

def res_w(path, new_width):
    '''
    resizes both jpg and png images in a bulk.
    args : image folder path and new width value
    output: resizes and saves in the same folder path tagged with resized_w_
    return: success status of function call
    '''
    extension = ['.jpg', '.png']
    for ext in extension:
        image_files = glob(os.path.join(path, '*'+ext))
        for index, filename in enumerate(image_files):
            img = Image.open(filename)
            wpercent = (int(new_width)/float(img.size[0]))
            hsize = int((float(img.size[1])*float(wpercent)))
            img = img.resize((int(new_width),hsize), Image.ANTIALIAS)
            img.save('./images/resized_w_'+str(index+1)+ext)
    return True

def res_h(path, new_height):
    '''
    resizes both jpg and png images in a bulk.
    args : image folder path and new height value
    output: resizes and saves in the same folder path tagged with resized_h_
    return: success status of function call
    '''
    extension = ['.jpg', '.png']
    for ext in extension:
        image_files = glob(os.path.join(path, '*'+ext))
        for index, filename in enumerate(image_files):
            img = Image.open(filename)
            hpercent = (int(new_height)/float(img.size[0]))
            wsize = int((float(img.size[1])*float(hpercent)))
            img = img.resize((int(new_height),wsize), Image.ANTIALIAS)
            img.save('./images/resized_h_'+str(index+1)+ext)
    return True

def res_p(path, new_percent):
    '''
    resizes both jpg and png images in a bulk.
    args : image folder path and new percentage value
    output: resizes and saves in the same folder path tagged with resized_
    return: success status of function call
    '''
    extension = ['.jpg', '.png']
    for ext in extension:
        image_files = glob(os.path.join(path, '*'+ext))
        if len(image_files)>0:
            for index, filename in enumerate(image_files):
                img = Image.open(filename)
                wsize = int((float(img.size[0])*float(new_percent)))
                hsize = int((float(img.size[1])*float(new_percent)))
                img = img.resize((wsize,hsize), Image.ANTIALIAS)
                img.save('./images/resized_'+str(index+1)+ext)
    return True

def crp_px(path,new_length=None):
    '''
    centre crop both jpg and png images in a bulk.
    args : image folder path and accepts both as percentage and as well pixel value
    output: crops and saves in the same folder path tagged with cropped_
    return: success status of function call
    '''
    extension = ['.jpg', '.png']
    for ext in extension:
        image_files = glob(os.path.join(path, '*'+ext))
        if len(image_files)>0:
            for index, filename in enumerate(image_files):
                img = Image.open(filename)
                width, height = img.size   # Get dimensions
                new_width, new_height = new_length, new_length
                if new_height < height and new_width < width:
                    if new_height < 1 and new_width < 1:
                        new_height = int((float(img.size[1])*float(new_length)))
                        new_width = int((float(img.size[0])*float(new_length)))
                    # Crop the image
                    left = (width - new_width)/2
                    top = (height - new_height)/2
                    right = (width + new_width)/2
                    bottom = (height + new_height)/2

                    # Crop the center of the image
                    img = img.crop((left, top, right, bottom))
                    img.save('./images/cropped_'+str(index+1)+ext)
                else:
                    print('Error!!! Original image size is:', width, height) 
    return True