import cv2
import numpy as np

img = cv2.imread("day01/photo.jpg")

# Read one pixel: row 100, column 200
pixel = img[100, 200]
print("Pixel [100, 200] =", pixel)

b, g, r = pixel
print(f"Blue={b}, Green={g}, Red={r}")

# Make a pure blue image, 100x100 pixels
blue = np.zeros((100, 100, 3), dtype=np.uint8)
blue[:] = (0, 255, 255)

cv2.imshow("I asked for (255, 0, 0)", blue)
cv2.waitKey(0)
cv2.destroyAllWindows()
