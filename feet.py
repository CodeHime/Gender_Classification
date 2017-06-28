# import the necessary packages
import argparse
import imutils
import cv2

zero=float(0)
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
			feet_img=image[y+(9*h/10):y+h,x:x+w]
			cv2.imwrite('feet'+str(i) + '_'+ str(idx) +'.png', feet_img)

			f_edged = cv2.Canny(feet_img, 10, 250)
			(_,f_cnts, _) = cv2.findContours(f_edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

			feet=1
			# loop over the contours
			for f_c in f_cnts:
				# compute the center of the contour
				
				f_M = cv2.moments(f_c)
				print i, '\n', f_M["m00"], '\n'

				f_cX[feet] = int(f_M["m10"] / f_M["m00"])
				f_cY[feet] = int(f_M["m01"] / f_M["m00"])
				 
				# draw the contour and center of the shape on the image
				cv2.drawContours(feet_img, [f_c], -1, (0, 255, 0), 2)
				cv2.circle(feet_img, (f_cX[feet], f_cY[feet]), 7, (0, 255, 255), -1)
				cv2.putText(feet_img, "center", (f_cX[feet] - 20, f_cY[feet] - 20),
				cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 255), 2)
				 
				# show the image
				cv2.imshow("Image", feet_img)
				cv2.waitKey(0)
				feet+=1

			print ((f_cX[1]-f_cX[2])**2+(f_cY[1]-f_cY[2])**2)**(1/2.0),'\n'

	# loop over the contours
	for c in cnts:
		# compute the center of the contour
		M = cv2.moments(c)
		cX = int(M["m10"] / M["m00"])
		cY = int(M["m01"] / M["m00"])
		 
		# draw the contour and center of the shape on the image
		cv2.drawContours(image, [c], -1, (0, 255, 0), 2)
		cv2.circle(image, (cX, cY), 7, (0, 255, 255), -1)
		cv2.putText(image, "center", (cX - 20, cY - 20),
		cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 255), 2)
		 
		# show the image
		cv2.imshow("Image", image)
		cv2.waitKey(1)
	cv2.imshow("im",new_img)
	cv2.waitKey(1)