import numpy as np
import cv2


url = "http://192.168.1.103:8080/video"
cap = cv2.VideoCapture(url)
while True:
    camera, frame = cap.read()
    # if frame is not None:
    cv2.imshow("Frame", frame)

    q = cv2.waitKey(1)
    if q == ord("q"):
        break

# cap.release()
cv2.destroyAllWindows()
