import cv2 as cv
import numpy as np
import pytesseract as pyts
pyts.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

img = cv.imread("test_ocr.png")
img=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
img=cv.threshold(img,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)[1]

for i in range(57):
    for j in range(810):
        img[i,j]=255

for i in range(101,315):
    for j in range(810):
        img[i,j]=255
        
for i in range(360,406):
    for j in range(810):
        img[i,j]=255

for i in range(406):
    for j in range(52):
        img[i,j]=255

for i in range(406):
    for j in range(230,320):
        img[i,j]=255

for i in range(406):
    for j in range(505,595):
        img[i,j]=255

for i in range(406):
    for j in range(775,810):
        img[i,j]=255


#img = cv.medianBlur(img,5)
text = pyts.image_to_string(img)
print(text)
cv.imshow('valzkai ae',img)
cv.waitKey(0)