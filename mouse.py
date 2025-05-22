from cvzone.HandTrackingModule import HandDetector
import cv2
import pyautogui
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import tkinter as tk
import screen_brightness_control as sbc


root = tk.Tk()
pyautogui.FAILSAFE = False
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
print(screen_height, screen_width)
fingers = []

cap = cv2.VideoCapture(0)
detector = HandDetector(detectionCon=0.9, maxHands=2)
pinkColor = (147,20,255)

devices = AudioUtilities().GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
print(volume.GetVolumeRange())
def convertedRange(x, a, b, c, d):
    return (x - a) * (d - c) / (b - a) + c

while True:
    # Get image frame
    success, img = cap.read()
    # Find the hand and its landmarks
    hands, img = detector.findHands(img)  # with draw

    if hands:
        # Hand 1
        hand1 = hands[0]
        lmList1 = hand1["lmList"]  # List of 21 Landmark points
        handType1 = hand1["type"]  # Handtype Left or Right
        

        #code for scroll
        if handType1 == "Left":
            startPoint = (lmList1[8][0], lmList1[8][1])
            cv2.circle(img, startPoint, 10, pinkColor, -1)
            if detector.fingersUp(hand1)[1] == 1 : 
                pyautogui.scroll(30)
            if detector.fingersUp(hand1)[1] == 0 :
                pyautogui.scroll(-30)
    
        #code for mouse movement
        if handType1 == 'Right':
            cv2.rectangle(img, (0, 00), (screen_width, screen_height), pinkColor, 3)
            if detector.fingersUp(hand1)[1] == 1 : 
                cv2.circle(img, (lmList1[8][0], lmList1[8][1]), 12, pinkColor, -1)
                pyautogui.moveTo(
                                convertedRange(lmList1[8][0], 0, screen_width, screen_width, 0), 
                                convertedRange(lmList1[8][1],screen_height, 0, screen_height, 0)
                             )
                
            if detector.fingersUp(hand1)[1]:
                startPointC = (lmList1[4][0], lmList1[4][1])
                endPointA = (lmList1[12][0], lmList1[12][1])
                endPointB = (lmList1[16][0],lmList1[16][1])
                endPointC = (lmList1[20][0],lmList1[20][1])
                cv2.circle(img, startPointC, 12, (0,0,255), -1)
                cv2.circle(img, endPointA, 12, (255,0,0), -1)
                cv2.circle(img, endPointB, 12, (0,255,0), -1)
                cv2.circle(img, endPointC, 12, (0,255,255), -1)
                if detector.findDistance(startPointC, endPointA)[0] < 25:
                    cv2.circle(img, endPointA, 12, (0, 255, 0), -1)
                    pyautogui.doubleClick()
                if detector.findDistance(startPointC, endPointB)[0] < 25:
                    cv2.circle(img, endPointB, 12, (0, 255, 0), -1)
                    pyautogui.leftClick()
                if detector.findDistance(startPointC, endPointC)[0] < 25:
                    cv2.circle(img, endPointC, 12, (0, 255, 0), -1)
                    pyautogui.rightClick()



    cv2.imshow("Image", img)
    cv2.waitKey(1)
