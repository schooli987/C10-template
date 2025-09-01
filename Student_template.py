import mediapipe as mp
import pyautogui
import cv2
import time

capture = cv2.VideoCapture(0)

play = False
mute_active = False

while True:
    ret, frame = capture.read()
    frame = cv2.flip(frame, 1)

    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
   

    cv2.imshow("AI Music Controller", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()