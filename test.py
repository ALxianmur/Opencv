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
    bridge2 = cv.GaussianBlur(bridge1,(15,15),0)

    #统计像素点数量
    H,S,V =cv.split(bridge2)
    (minVal, maxVal, minLoc, maxLoc) = cv.minMaxLoc(H)
    bridge2 = cv.GaussianBlur(bridge1,(5,5),0)
    cv.circle(bridge2, minLoc, 20, (255, 0, 0), 2)
    #创建窗口
    cv.namedWindow("output",0)

    #显示结果
    cv.imshow("output",frame)
    #控制台显示
#     print("red")
#     print("green")
#     print("yellow")
    #键入“Esc”退出
    if cv.waitKey(20) & 0xff == 27:
            break
 #释放内存
capture.release()
cv.destroyAllWindows()
