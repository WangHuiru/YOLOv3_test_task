# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 16:19:21 2020

@author: luzgin
"""

import glob
import os
#import numpy as np
#import sys

current_dir = "data/images"
split_pct = 10  # 10% validation set
file_train = open("data/train.txt", "w")  
file_val = open("data/val.txt", "w")  
counter = 1
index_test = round(100/split_pct)  
for fullpath in glob.iglob(os.path.join(current_dir, "*.jpg")):
    title, ext = os.path.splitext(os.path.basename(fullpath))
    if counter == index_test:
        counter = 1
        file_val.write(current_dir + "/" + title + '.jpg' + "\n")
    else:
        file_train.write(current_dir + "/" + title + '.jpg' + "\n")
        counter = counter + 1
file_train.close()
file_val.close()