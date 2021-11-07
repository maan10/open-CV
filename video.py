import cv2
vid=cv2.VideoCapture("E:\python\Open cv\Video\Video.mp4")
while True:
    ret,frame=vid.read()
    print(ret)
    print("Width ==>",cv2.CAP_PROP_FRAME_WIDTH)
    print("Height==>",cv2.CAP_PROP_FRAME_HEIGHT)
    frame=cv2.resize(frame,(1000,700))
    cv2.imshow("first video ",frame)
    color=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow("color video ",color)
    if cv2.waitKey(10) & 0xff==ord("p"):   #terminate
        break

vid.release()
cv2.destroyAllWindows()
