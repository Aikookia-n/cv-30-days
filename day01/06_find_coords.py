import cv2

img = cv2.imread("day01/photo.jpg")

def show_coords(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(f"Clicked: x(column)={x}, y(row)={y}")

cv2.imshow("Click on corners", img)
cv2.setMouseCallback("Click on corners", show_coords)
cv2.waitKey(0)
cv2.destroyAllWindows()