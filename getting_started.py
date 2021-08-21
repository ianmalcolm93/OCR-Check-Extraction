import cv2 
import pytesseract

img = cv2.imread('data/handwritten.jpg')
# img = cv2.imread('data/check1.jpg')

# Adding custom options
custom_config = r'--psm 11'
output = pytesseract.image_to_string(
    img,
    config=custom_config
    )
print(output)