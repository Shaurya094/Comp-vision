import cv2
image = cv2.imread('flicker.png')

greyscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
resized_image = cv2.resize(greyscale, (224, 224))
cv2.imshow('Flicker', resized_image)

key = cv2.waitKey(0)
if key == ord('s'):
    cv2.imwrite('grayscale.png', resized_image)
    print ("Image saved as 'grayscale.png")
else:
    print("Not saved")

cv2.destroyAllWindows()
print("Image Dimentions: {resized_image.shape}")