import cv2
import numpy as np

# 300 rows tall, 600 columns wide, all black
img = np.zeros((300, 600, 3), dtype=np.uint8)

# Gradient: blue grows from 0 to 255 across the width
for x in range(600):
    img[:, x, 0] = int(x / 600 * 255)

# A green square in the middle
img[100:200, 250:350, 1] = 255

# A white border
cv2.rectangle(img, (0, 0), (599, 299), (255, 255, 255), 4)

cv2.imshow("Made from nothing", img)
cv2.imwrite("day01/gradient.png", img)
cv2.waitKey(0)
cv2.destroyAllWindows()