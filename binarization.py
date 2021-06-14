import cv2

# R G B (0 ~ 255)
# Gray (0 ~ 255) -> Binarization -> Black / White

# dummy function for TrackBar
def nothing(x):
    pass


# Build Window
cv2.namedWindow("Binary")

# Create Track Bar
cv2.createTrackbar("threshold", "Binary", 0, 255, nothing)

# Set init Track Bar value
cv2.setTrackbarPos("threshold", "Binary", 170)

img_color = cv2.imread("Images/red_ball.jpg", cv2.IMREAD_COLOR)

cv2.imshow("Color", img_color)
cv2.waitKey(0)

img_gray = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)
cv2.imshow("Color", img_gray)
cv2.waitKey(0)

while True:
    # Get threshold Value
    low = cv2.getTrackbarPos("threshold", "Binary")

    # Binarization
    # 0 ~ low : black
    # low ~ 255 : white
    ret, img_binary = cv2.threshold(img_gray, low, 255, cv2.THRESH_BINARY_INV)

    cv2.imshow("Binary", img_binary)

    # BitWise original image and binary image
    img_result = cv2.bitwise_and(img_color, img_color, mask=img_binary)
    cv2.imshow("Result", img_result)

    # Wait one second to get KeyBoard
    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows()