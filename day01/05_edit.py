import cv2

img = cv2.imread("day01/photo.jpg")
h, w = img.shape[:2]
print(f"Width={w}, Height={h}")

# CROP: img[y_start:y_end, x_start:x_end]
crop = img[319:825, 1131:1421]
cv2.imshow("Crop", crop)

# PAINT a region red (on a copy!)
painted = img.copy()
painted[319:825, 1131:1421] = (0, 255, 0)
cv2.imshow("Painted", painted)

# FLIP horizontally (mirror)
mirror = cv2.flip(img, 0)
cv2.imshow("Mirror", mirror)

mirror2 = cv2.flip(img, -1)
cv2.imshow("Mirror", mirror2)

# RESIZE to half size
half = cv2.resize(img, (w // 2, h // 2))
cv2.imshow("Half", half)
print("Half shape:", half.shape)
cv2.imwrite("day01/crop.jpg", crop)

cv2.waitKey(0)
cv2.destroyAllWindows()