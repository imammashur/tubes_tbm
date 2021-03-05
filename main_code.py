import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import os # ngutak ngatik operating system
import random
import pydicom as dicom # file dicom
import cv2 # computer vision
import matplotlib.pyplot as plt # plotting

def konversi_ke_jpg(folder_path, PNG, output):
    jpg_folder_path = output
    images_path = os.listdir(folder_path)
    for n, image in enumerate(images_path):
        ds = dicom.dcmread(os.path.join(folder_path, image))
        pixel_array_numpy = ds.pixel_array
        if PNG == False:
            image = image.replace('.dcm', '.jpg')
        else:
            image = image.replace('.dcm', '.png')
        cv2.imwrite(os.path.join(jpg_folder_path, image), pixel_array_numpy)
        print('{} image converted'.format(n))

def tampilkan_gambar(path):
    img = cv2.imread(path, 0)
    print("menampilkan "+path)
    plt.imshow(img)
        
if __name__ == "__main__":
    for dirname, _, filenames in os.walk('../input/lung-cancer-dataset/PCsub1-20090909/PCsub1-20090909/W0001/1.2.826.0.1.3680043.2.656.1.136/S02A01'): 
        print (dirname)
        lokasi = dirname
        konversi_ke_jpg(lokasi, False, './')

    i = 0
    files = []
    for dirname, _, filenames in os.walk('./'):
        for filename in filenames:
            print (filename)
            files.append(filename)
            i += 1
            
    print (files)
    cuplik_random = files[random.randrange(len(files))]
    tampilkan_gambar(cuplik_random)
