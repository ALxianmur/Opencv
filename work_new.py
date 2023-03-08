from http.client import SWITCHING_PROTOCOLS
import cv2 as cv
import numpy as np
import matplotlib as plt
#读取视频
capture = cv.VideoCapture('./video/example.mp4')
while True:
    ret,frame = capture.read()

    #创建606*1080窗口
    cv.namedWindow('output',0)
    cv.resizeWindow('output',width =606 ,height = 1080)
    cv.namedWindow('output2',0)
    cv.resizeWindow('output2',width =606 ,height = 1080)
    #图像处理
    gray = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    hsv=cv.cvtColor(frame,cv.COLOR_BGR2HSV)
   

    #添加描述文字以及判断条件
    font = cv.FONT_HERSHEY_SIMPLEX

    """         cv.putText(frame,'red',(10,400),font,4,(0,0,0),5,cv.LINE_AA)
        cv.putText(frame,'yellow',(10,400),font,4,(0,0,0),5,cv.LINE_AA)
        cv.putText(frame,'green',(10,400),font,4,(0,0,0),5,cv.LINE_AA) """
    number = hsv[(1,2)]
    print(type(number))
    print(number)
    #显示结果
    cv.imshow('output',frame)
    cv.imshow('output2',hsv)
    #键入‘Esc’以退出
    if cv.waitKey(20) & 0xff == 27:
        break
#释放内存
capture.release()
cv.destroyAllWindows()
