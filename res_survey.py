import sys
import cv2
import os

dir_name = sys.argv[1]
files = os.listdir(dir_name)
print('"name","height","width","ratio"')
for fname in files:
    img = cv2.imread(os.path.join(dir_name, fname))
    print('"{}",{},{},{}'.format(fname, img.shape[0], img.shape[1], img.shape[0]/img.shape[1]))



