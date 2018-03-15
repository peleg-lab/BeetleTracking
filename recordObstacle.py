import cv2
import sys
from scipy import misc
import glob
import numpy as np

ix,iy = -1,-1
# mouse callback function
def draw_circle(event,x,y,flags,param):
    global ix,iy
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img,(x,y),10,(0,0,255),-1)
        ix,iy = x,y

# Reading from Arena Snap
for image_path in glob.glob("Arena Snap.png"):
    img = misc.imread(image_path)
    print (img.shape)
    print (img.dtype)

cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_circle)

# Creating File to Store Co-ordinates based on given scale and data
file = open("obstacles.txt", "w")

while(1):
    cv2.imshow('image',img)
    k = cv2.waitKey(20) & 0xFF
    if k == 27:
        break
    elif k == ord('a'):

        ix/=8.05
        iy/=8.05
        print (str(round(ix, 2))+" "+str(round(iy, 2))) # Printing the data
        file.write(str(round(ix, 2))+" "+str(round(iy, 2))+ "\n") # Adding it to the file
cv2.destroyAllWindows()
file.close()