#引入库函数
import numpy as np
import cv2 as cv
import matplotlib as plt
capture = cv.VideoCapture("./video/example.mp4")
#导入视频
while 1:
    ret,frame = capture.read()
  
    #RGB转HSV
    bridge1 = cv.cvtColor(frame,cv.COLOR_RGB2HSV)

    #高斯滤波去噪
    dx = cv.Scharr(bridge2,cv.CV_64F,1,0)
    dy = cv.Scharr(bridge2,cv.CV_64F,0,1)
    bridge2 = cv.addWeighted(dx,0.5,dy,0.5,25)
        #创建窗口
    cv.namedWindow("output",0)

    #显示结果
    cv.imshow("output",bridge2)
    #控制台显示
#     print("red:%d yellow:%d green:%d"%(counter_red,counter_yellow,counter_green))
    #键入“q”退出
    if cv.waitKey(20) & 0xff == ord("q"):
            break
 #释放内存
capture.release()
cv.destroyAllWindows()
