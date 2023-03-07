from http.client import SWITCHING_PROTOCOLS
import cv2 as cv
import numpy as np
import matplotlib as plt
#读取视频
capture = cv.VideoCapture('./video/example.mp4')
while True:
    ret,frame = capture.read()
    hsv=cv.cvtColor(frame,cv.COLOR_BGR2HSV)
    #创建606*1080窗口
    cv.namedWindow('output',0)
    cv.resizeWindow('output',width =606 ,height = 1080)
    cv.namedWindow('output2',0)
    cv.resizeWindow('output2',width =606 ,height = 1080)
    #图像灰度处理
    gray = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    #高斯模糊处理
    gray = cv.GaussianBlur(gray,(15,15),0)
    #寻找图中最亮点以确定判定区域--由于进行了模糊处理这里指的是均值最亮的小范围区域的中心
    (minVal, maxVal, minLoc, maxLoc) = cv.minMaxLoc(gray)
    cv.circle(frame, maxLoc, 20, (255, 0, 0), 2)
    number = (hsv[maxLoc])
    print('number:' , number)
    print(type(number))
    print(max(number))
    #添加描述文字以及判断条件
    font = cv.FONT_HERSHEY_SIMPLEX
    if max(number)==number[0]:
        cv.putText(frame,'red',(10,400),font,4,(0,0,0),5,cv.LINE_AA)
    elif max(number)==number[1]:
        cv.putText(frame,'yellow',(10,400),font,4,(0,0,0),5,cv.LINE_AA)
    elif max(number)==number[2]:   
        cv.putText(frame,'green',(10,400),font,4,(0,0,0),5,cv.LINE_AA)
        

    #显示结果
    cv.imshow('output',frame)
    cv.imshow('output2',hsv)
    #键入‘Esc’以退出
    if cv.waitKey(20) & 0xff ==27:
        break
#释放内存
capture.release()
cv.destroyAllWindows()
# 2023.1.12