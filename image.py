import cv2

# import numpy as np
# photo= cv2.imread(r"C:\Users\solan\Downloads\Photos\Screenshot_2025.05.20_14.02.20.684.png")
# photo=cv2.resize(photo,(800,500))  #resize the photo 
# gray=cv2.cvtColor(photo,cv2.COLOR_BGR2GRAY)
# print(photo)

# cv2.imshow("loaded image",gray)
# cv2.waitKey(0)

import os
folder_path = r"C:\Users\solan\Downloads\Photos"
folder_name = os.path.basename(folder_path)

print("folder Name:", folder_name)
items = os.listdir(folder_path)
print("Item Inside Folder:", items)


print(items[0])

image_path = os.path.join(folder_path, items[0])
print("Image path :", image_path)

img = cv2.imread(image_path)
photo=cv2.resize(img,(800,500))
print(photo)

cv2.imshow("Image Loaded", photo)

cv2.waitKey(0)

X = [] #create an empty list for storing different images

for i in range(0,len(items)):
    image_path = os.path.join(folder_path,items[i])
    img = cv2.imread(image_path)
    photo=cv2.resize(img,(800,500))
    X.append(img)
    

cv2.imshow('Input Image:', X[1]) 
cv2.waitKey(0)

