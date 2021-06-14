import cv2

# IMREAD_COLOR
# IMREAD_GRAYSCALE
# IMREAD_UNCHANGED (include transparent)
img_color = cv2.imread("Images/testImage.jpg", cv2.IMREAD_COLOR)

# Build Window
cv2.namedWindow("Show Image")

# Show Image
cv2.imshow("Show Image", img_color)

# Wait Keyboard
cv2.waitKey(0)

# change to gray
img_gray = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)

# Show Image
cv2.imshow("Show GrayScale Image", img_gray)

# Wait Keyboard
cv2.waitKey(0)

# Save Image
cv2.imwrite("Images/testImage_gray.jpg", img_gray)

# Destroy Windows
cv2.destroyAllWindows()
