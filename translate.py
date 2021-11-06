import cv2
import numpy as np

img = cv2.imread('./img/fish.jpg')
rows,cols = img.shape[0:2]  

dx, dy = 500, 500           

mtrx = np.float32([[1, 0, dx],
                   [0, 1, dy]])  

dst = cv2.warpAffine(img, mtrx, (cols+dx, rows+dy))   

dst2 = cv2.warpAffine(img, mtrx, (cols+dx, rows+dy), None, cv2.INTER_LINEAR, cv2.BORDER_CONSTANT, (255,0,0) )

dst3 = cv2.warpAffine(img, mtrx, (cols+dx, rows+dy), None, cv2.INTER_LINEAR, cv2.BORDER_REFLECT)
dst4 = cv2.warpAffine(img, mtrx, (cols+dx, rows+dy), None, cv2.INTER_NEAREST, cv2.BORDER_REPLICATE)

dst5 = cv2.warpAffine(img, mtrx, (cols+dx, rows+dy), None, cv2.INTER_AREA, cv2.BORDER_WRAP)

dst6 = cv2.warpAffine(img, mtrx, (cols+dx, rows+dy), None, cv2.INTER_CUBIC, cv2.BORDER_WRAP)

dst7 = cv2.warpAffine(img, mtrx, (cols+dx, rows+dy), None, cv2.INTER_LANCZOS4, cv2.BORDER_WRAP)

cv2.imshow('original', img)
cv2.imshow('trans',dst)
cv2.imshow('BORDER_CONSTATNT', dst2)
cv2.imshow('BORDER_FEFLECT', dst3)
cv2.imshow('BORDER_REPLICATE', dst4)
cv2.imshow('BORDER_WRAP', dst5)
cv2.imshow('INTER_CUBIC & BORDER_WRAP', dst6)
cv2.imshow('INTER_LANCZOS4 & BORDER_WRAP', dst7)
cv2.waitKey(0)
cv2.destroyAllWindows()
