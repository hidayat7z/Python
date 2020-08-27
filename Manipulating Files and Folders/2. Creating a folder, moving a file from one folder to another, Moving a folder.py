# MOVING A FILE

import os
import shutil

##create a new directory (in Linux)
os.mkdir("/home/hidayat7z/Documents/Nu foldr")


#MOVING A FILE FROM ONE FOLDER TO ANOTHER
shutil.move("/home/hidayat7z/first.txt","/home/hidayat7z/Documents/NUfoldr/first.txt")

#MOVING A FOLDER
shutil.move("/home/hidayat7z/Documents/NUfoldr","/home/hidayat7z/Documents/Nu2/")
