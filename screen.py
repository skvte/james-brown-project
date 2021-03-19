import cv2

img = cv2.imread('templ.png')
img_tot_bed = img[800:1400, :2150, :]

# font
font = cv2.FONT_HERSHEY_DUPLEX

# org
org = (100, 350)

# fontScale
fontScale = 15

# Blue color in BGR
color = (0, 0, 0)

# Line thickness of 2 px
thickness = 2

# Using cv2.putText() method
image = cv2.putText(img_tot_bed, '\u20ac 100.00', org, font,
                    fontScale, color, thickness, cv2.LINE_AA)


cv2.imshow('test', img_tot_bed)
cv2.waitKey(0)