import cv2

img = cv2.imread("day01/photo.jpg")

if img is None:
    print("Could not load image! Check the path.")
    exit()

print("Shape:", img.shape)
print("Data type:", img.dtype)

cv2.imshow("My photo", img)
cv2.waitKey(0)
cv2.destroyAllWindows()