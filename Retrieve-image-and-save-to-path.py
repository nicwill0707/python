

import urllib.request
import csv
import os

# ask user for pathway to local folder where images will be saved)
image_Folderpath = input(r'Enter full pathway to which images will be saved: ')

#join path input by user to name of file
fullfilename = os.path.join(image_Folderpath, 'filename')

#retrieve (download) image and store to pathway
urllib.request.urlretrieve('https://ukntrees.ca.uky.edu/sites/ukntrees.ca.uky.edu/files/webform/adopt-form/img_3957.png', fullfilename)
