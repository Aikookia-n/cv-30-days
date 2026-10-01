import cv2

img = cv2.imread("day01/photo.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
wrong = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
print("Color shape: ", img.shape)
print("Gray shape: ", gray.shape)

cv2.imshow("Color", img)
cv2.imshow("Gray", gray)
cv2.imshow("Wrong", wrong)

cv2.waitKey(0)
cv2.destroyAllWindows()