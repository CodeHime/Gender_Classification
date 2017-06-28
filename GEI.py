# crop the sequence
# and apply GEI

import argparse
import imutils
import cv2
from PIL import Image
import numpy as np

begin=35
end=93
zero=float(0)

with Image.open("090/001-bg-01-090-035.png") as img:
    width, height = img.size
print 'w= ',width,'h= ',height

avg_img = np.zeros((height,width,3), np.uint8)

for i in range(begin,end):
	image = cv2.imread("090/001-bg-01-090-0"+str(i)+".png")
	gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
	edged = cv2.Canny(image, 10, 250)
	(_,cnts, _) = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
	idx = 0
	for c in cnts:
		x,y,w,h = cv2.boundingRect(c)
		if w>50 and h>50:
			idx+=1
			new_img = np.zeros((height,width,3), np.uint8)
			new_img[(height-h)/2:(height-h)/2+h,(width-w)/2:(width-w)/2+w]=image[y:y+h,x:x+w]
			avg_img+=new_img
			print ', '.join(str(avg_img))	
			cv2.imwrite(str(i) + '_'+ str(idx) +'.png', new_img)
	cv2.imshow("im",new_img)
	cv2.waitKey(1)
avg_img/=(end-begin)
# not averaging properly
print ', '.join(str(avg_img))
cv2.imwrite('GEI.png', avg_img)
