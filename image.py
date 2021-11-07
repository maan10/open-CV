import cv2    #import cv2

img=cv2.imread("E:\python\Open cv\Photos\wolf.jfif")   
img2=cv2.imread("E:\python\Open cv\Photos\wolf.jfif",0)   
#imread: firt path of the location , second (-1,0,1) parameter 
img3=cv2.imread("E:\python\Open cv\Photos\wolf.jfif",-1)   
img1=cv2.resize(img,(1000,700))
cv2.imshow("Wolf",img)
cv2.imshow("Resize img",img1)
cv2.imshow("Gray cale",img2)
cv2.imshow("saturation",img3)
cv2.waitKey(0) #parameter decide  diplay time
cv2.destroyAllWindows()
