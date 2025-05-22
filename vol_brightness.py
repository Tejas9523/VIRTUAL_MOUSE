from cvzone.HandTrackingModule import HandDetector
import cv2
import pyautogui
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import tkinter as tk
import screen_brightness_control as sbc


root = tk.Tk()
# root.configure(bg='blue')
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
print(sbc.get_brightness())
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
        

        #code for brightness control
        if handType1 == "Left":
            # thumb top point
            startPoint = (lmList1[8][0], lmList1[8][1])
            cv2.circle(img, startPoint, 10, pinkColor, -1)
            # first finger top point
            endPoint = (lmList1[4][0], lmList1[4][1])
            cv2.circle(img, endPoint, 10, pinkColor, -1)

            cv2.line(img, startPoint, endPoint, pinkColor, 2)
            distance = detector.findDistance(startPoint, endPoint)[0]
            print(distance)

            if distance >=25 and distance <= 125 and detector.fingersUp(hand1)[1] and detector.fingersUp(hand1)[0]: 
                print("Bright: ",sbc.get_brightness())
                sbc.set_brightness(distance)

        #code for volume control
        if handType1 == 'Right':
             # thumb top point
            startPoint = (lmList1[8][0], lmList1[8][1])
            cv2.circle(img, startPoint, 10, pinkColor, -1)
            # first finger top point
            endPoint = (lmList1[4][0], lmList1[4][1])
            cv2.circle(img, endPoint, 10, pinkColor, -1)

            cv2.line(img, startPoint, endPoint, pinkColor, 2)
            distance = detector.findDistance(startPoint, endPoint)[0]
            print(distance)

            if distance >=25 and distance <= 190 and detector.fingersUp(hand1)[1] and detector.fingersUp(hand1)[0]: 
                volume.SetMasterVolumeLevel(convertedRange(distance, 25, 190, volume.GetVolumeRange()[0], volume.GetVolumeRange()[1]), None)



    cv2.imshow("Image", img)
    cv2.waitKey(1)
