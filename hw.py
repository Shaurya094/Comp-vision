import cv2

image = cv2.imread('flicker.png')

cv2.namedWindow('Small Image', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Small Image', 200, 200)

cv2.namedWindow('Mid Image', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Mid Image', 400, 400)

cv2.namedWindow('Large Image', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Large Image', 800, 800)

cv2.imshow('Small Image', image)
cv2.imshow('Mid Image', image)
cv2.imshow('Large Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

