import cv2
import numpy as np

img = cv2.imread("day01/photo.jpg")
b, g, r = cv2.split(img)
cv2.imshow("Blue channel", b)
cv2.imshow("Green channel", g)
cv2.imshow("Red channel", r)
print("Blue avg:", np.mean(b))
print("Green avg:", np.mean(g))
print("Red avg:", np.mean(r))


cv2.waitKey(0)
cv2.destroyAllWindows()