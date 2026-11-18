import cv2
import numpy as np
image1 = cv2.imread("add1.jpg",cv2.IMREAD_GRAYSCALE)
image2 = cv2.imread("add2.jpg",cv2.IMREAD_GRAYSCALE)
if image1 is None or image2 is None:
    raise Exception("file error")

alpha, beta = 0.6,0.7
add_img1 = cv2.add(image1,image2)
add_img2 = cv2.add(image1 * alpha, image2 * beta)
add_img2 = np.clip(add_img2,0,255).astype('uint8')
add_img3 = cv2.addWeighted(image1,alpha,image2,beta,0)

cv2.imshow("image1",image1)
cv2.imshow("image2",image2)
cv2.imshow("add1",add_img1)
cv2.imshow("add2",add_img2)
cv2.imshow("add3",add_img3)
cv2.waitKey(0)