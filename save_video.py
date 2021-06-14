import cv2

# Capture
cap = cv2.VideoCapture(0)

# Codec
fourcc = cv2.VideoWriter_fourcc(*"XVID")

# Video Writer
writer = cv2.VideoWriter("output.avi", fourcc, 30.0, (640, 480))

while True:
    # Get Capture Image
    ret, img_color = cap.read()

    if ret == False:  # Capture Fails
        continue

    img_gray = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)

    # Show Image
    cv2.imshow("Color", img_color)
    cv2.imshow("Gray Color", img_gray)

    # Write Image
    writer.write(img_color)

    # Wait one second to get KeyBoard
    if cv2.waitKey(1) & 0xFF == 27:
        break

# Memory Release
cap.release()
writer.release()
cv2.destroyAllWindows()