
###############################################
##      Controlando um jogo por gestos       ##
###############################################
#importação das libs usadas
import cv2
import numpy as np
import handTrackingModule as htm
import math
import pyautogui


cap = cv2.VideoCapture(1)


detector = htm.handDetector(detectionCon=0.6)

while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lmlist = detector.findPosition(img, draw=False)
    
    if len(lmlist) != 0:
        # print(lmlist[4], lmlist[8])

        x1, y1 = lmlist[4][1], lmlist[4][2]
        x2, y2 = lmlist[8][1], lmlist[8][2]

        cx, cy = (x1 + x2)//2, (y1 + y2) //2


        cv2.circle(img, (x1, y1), 13, (255,0,255), cv2.FILLED)
        cv2.circle(img, (x2, y2), 13, (255,0,255), cv2.FILLED)

        cv2.line(img, (x1, y1), (x2,y2), (255,0,255),3)
        cv2.circle(img, (cx, cy), 10, (255,0, 255), cv2.FILLED)

        length:int = math.hypot(x2-x1,y2-y1)
        # print(length)
        if length >= 100:
            cv2.circle(img, (cx, cy), 10, (0,155, 0), cv2.FILLED)
            
            #O gesto ativado faz com que use esaço#
            pyautogui.press('space')    

    img = cv2.flip(img,1)
    cv2.imshow("Controle por gestos", img)
    key = cv2.waitKey(1)
    if key == 27:
        break

img.release()
cv2.destroyAllWindows()