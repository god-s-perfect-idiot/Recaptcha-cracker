import cv2
#cv2.imshow("a",cropped)

def prepare():

    im = cv2.imread("page.png")
    cropped = im[260:750,110:600]

    ima = cropped[0:165,0:165]
    imb = cropped[0:165,165:330]
    imc = cropped[0:165,330:490]
    imd = cropped[165:330,0:165]
    ime = cropped[165:330,165:330]
    imf = cropped[165:330,330:490]
    img = cropped[330:490,0:165]
    imh = cropped[330:490,165:330]
    imi = cropped[330:490,330:490]

    cv2.imwrite("ima.png",ima)
    cv2.imwrite("imb.png",imb)
    cv2.imwrite("imc.png",imc)
    cv2.imwrite("imd.png",imd)
    cv2.imwrite("ime.png",ime)
    cv2.imwrite("imf.png",imf)
    cv2.imwrite("img.png",img)
    cv2.imwrite("imh.png",imh)
    cv2.imwrite("imi.png",imi)

prepare()
