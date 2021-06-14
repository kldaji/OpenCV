import cv2

# Capture
cap = cv2.VideoCapture("output.avi")

# Codec
fourcc = cv2.VideoWriter_fourcc(*"XVID")

while True:
    # Get Capture Image
    ret, img_color = cap.read()

    if ret == False:  # Video End
        break

    img_gray = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)

    # Show Image
    cv2.imshow("Color", img_color)
    cv2.imshow("Gray Color", img_gray)

    # Wait one second to get KeyBoard
    if cv2.waitKey(1) & 0xFF == 27:
        break

# Memory Release
cap.release()
cv2.destroyAllWindows()