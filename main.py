from socket import getservbyname
from tokenize import Imagnumber
import cv2
import os
import numpy as np
from cvzone.HandTrackingModule import HandDetector

width, height = 1280,720
folderPath="meme"
cap=cv2.VideoCapture(0)
cap.set(3, width)
cap.set(4, height)

pathImages= sorted(os.listdir(folderPath),key=len)
print(pathImages)

imgNumber=0
hs, ws = int(120),int (213)
gestureThreshold=300

buttonPress=False
buttonCounter=0
buttonDelay=60
annotations=[]
#hand detector
detector= HandDetector(detectionCon=0.9, maxHands=1)

while True:

    success, img= cap.read()
    img=cv2.flip(img, 1)
    pathFullImage= os.path.join(folderPath,pathImages[imgNumber])
    imgCurrent=cv2.imread(pathFullImage)   

    #detection of hand
    hands, img=detector.findHands(img,flipType=False)
    cv2.line(img,(0,gestureThreshold),(width,gestureThreshold), (0,255,0), 10)

    if hands and buttonPress is False :
        hand=hands[0]
        fingers=detector.fingersUp(hand)
        cx,cy=hand['center']
        lmList=hand['lmList']
        indexFinger = lmList[8][0], lmList[12][1]
        xVal=int(np.interp(lmList[8][0], [width//2, w],[0,width]))
        yVal=int(np.interp(lmList[8][1], [200,height -200], [0, height]))
        indexFinger=xVal,yVal

        if cy<=gestureThreshold:
            #g-1
            if fingers==[1,1,1,0,0] or fingers==[0,1,1,0,0]:
                print("Next")
                if imgNumber < len(pathImages)-1:
                    imgNumber +=1
                    buttonPress=True
                #g-2
            if fingers==[1,1,1,1,1] or fingers==[0,1,1,1,1]:
                print("Previous")
                if imgNumber>0:
                    imgNumber -=1
                    buttonPress=True
        if fingers==[1,0,1,0,0] or fingers==[0,0,1,0,0] :
            print("Quit")
            buttonPress=True
            cv2.imshow.close()
                #g-3
        if fingers==[1,1,0,0,0] or fingers==[0,1,0,0,0]:
            print("write")
            cv2.circle(imgCurrent, indexFinger,15,(0,0,255),cv2.FILLED)
        if fingers==[1,1,0,0,1] or fingers==[0,1,0,0,1]:
            print("write")
            cv2.circle(imgCurrent, indexFinger,15,(0,0,255),cv2.FILLED)
            annotations.append(indexFinger)
                #g-1
        if fingers==[1,1,1,1,0] or fingers==[0,1,1,1,0]:
                print("erase")
                buttonPress=True
                #g-1
            
    if buttonPress:
        buttonCounter +=1
        if buttonCounter>buttonDelay:
            buttonCounter=0
            buttonPress=False
    for i in range (len(annotations)):
        if i!=0:
            cv2.line(imgCurrent, annotations[i -1],annotations[i],(0,0,200),12)
    #image one software
    imgSmall=cv2.resize(img,(ws,hs))
    h, w, _=imgCurrent.shape
    imgCurrent[0:hs,w-ws:w]=imgSmall





    cv2.imshow("Image",img)
    cv2.imshow("Slides",imgCurrent)
    key= cv2.waitKey(1)
    if key == ord('q'):
        break