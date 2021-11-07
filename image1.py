import cv2    #import cv2

img=cv2.imread("E:\python\Open cv\Photos\wolf.jfif")   
img2=cv2.imread("E:\python\Open cv\Photos\wolf.jfif",0)   
img3=cv2.flip(img2,1)
cv2.imshow("Flip1",img3)
img3=cv2.flip(img2,0)
cv2.imshow("Flip0",img3)
img3=cv2.flip(img2,-1)
cv2.imshow("Flip-1",img3)
cv2.imshow("Wolf",img)
cv2.imshow("Gray cale",img2)

cv2.waitKey(0) #parameter decide  diplay time
cv2.destroyAllWindows()
