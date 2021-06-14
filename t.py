import cv2

cap = cv2.VideoCapture(0)
print(cap.set(cv2.CAP_PROP_CONVERT_RGB, 1))