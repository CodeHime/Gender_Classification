# crop the sequence

import cv2 
for i in range(35,93):
	image = cv2.imread("090/001-bg-01-090-0"+str(i)+".png")
	gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
	edged = cv2.Canny(image, 10, 250)
	(_,cnts, _) = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
	idx = 0
	for c in cnts:
		x,y,w,h = cv2.boundingRect(c)
		if w>50 and h>50:
			idx+=1
			new_img=image[y:y+h,x:x+w]
			cv2.imwrite(str(i) + '_'+ str(idx) +'.png', new_img)
	cv2.imshow("im",new_img)
	cv2.waitKey(1)