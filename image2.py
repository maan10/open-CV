#in this ection we ave the image 
import cv2    #import cv2

img=cv2.imread("E:\python\Open cv\Photos\wolf.jfif",0)   

img=cv2.flip(img,0)
cv2.imshow("Gray cale",img)
k=cv2.waitKey(0) #parameter decide  diplay time
if k==ord("p"):
    cv2.imwrite("E:\python\Open cv\Photos\wolf_Reize.png",img)
    cv2.destroyAllWindows()
elif k==ord("q"):   
    cv2.destroyAllWindows()


