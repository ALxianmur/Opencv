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

    #标注圆的位置
    cv.circle(frame, maxLoc, 20, (255, 0, 0), 2)


    #定义计数器
    counter_red = 0
    counter_green = 0
    counter_yellow = 0
    i =[maxLoc[0],maxLoc[1],20]

     # 遍历范围内的每一像素点
    for x in [i[0]-i[2],i[0]+i[2]]:
            for y in [i[1]-i[2],i[1]+i[2]]:   
                counter = frame[(x,y)]
                print(counter)
                if (counter[0]>156)&(counter[0]<180):
                  counter_red =counter_red+1 
                if (counter[1]>35)&(counter[1]<77):
                  counter_green =counter_green+ 1
                if (counter[1]>26)&(counter[1]<34):
                  counter_yellow =counter_yellow+ 1

    #添加描述文字以及判断条件
    number = [counter_red ,counter_yellow ,counter_green] 
    print(number)
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
# 2023.3.8