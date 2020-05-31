import cv2

im = cv2.imread("page.png")
cropped = im[190:590,90:485]
#cv2.imshow("a",cropped)


ima = cropped[0:130,0:130]
imb = cropped[0:130,130:260]
imc = cropped[0:130,260:390]
imd = cropped[130:260,0:130]
ime = cropped[130:260,130:260]
imf = cropped[130:260,260:390]
img = cropped[260:390,0:130]
imh = cropped[260:390,130:260]
imi = cropped[260:390,260:390]

cv2.imwrite("ima.png",ima)
cv2.imwrite("imb.png",imb)
cv2.imwrite("imc.png",imc)
cv2.imwrite("imd.png",imd)
cv2.imwrite("ime.png",ime)
cv2.imwrite("imf.png",imf)
cv2.imwrite("img.png",img)
cv2.imwrite("imh.png",imh)
cv2.imwrite("imi.png",imi)
