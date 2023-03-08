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

    #RGB转GRAY
    bridge2 = cv.cvtColor(frame,cv.COLOR_RGB2GRAY)

    #高斯滤波去噪
    frame = cv.medianBlur(bridge2,7)

    #霍夫变换
    
    circle = cv.HoughCircles(bridge2, cv.HOUGH_GRADIENT, 1, 50,param1=100, param2=100, minRadius=0, maxRadius=1000)
    print(circle)

    # 遍历矩阵的每一行的数据
    for i in circle[0, :]:  
    # 绘制圆形
     cv.circle(frame, (int(i[0]), int(i[1])), int(i[2]), (255, 0, 0), 10)
    # 绘制圆心
     cv.circle(frame, (int(i[0]), int(i[1])), 10, (255, 0, 0), -1)
          
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
