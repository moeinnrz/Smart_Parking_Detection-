import cv2
import pickle
import cvzone
import numpy as np





cap=cv2.VideoCapture("carPark.mp4")
with open('CarParkPos', 'rb') as f:
    posList = pickle.load(f)


width,height= 107,48
def checkParkingSpace(imgPro):
    spaceCounter=0
    for pos in posList:
        x,y=pos
        imageCrop=imgPro[y:y+height,x:x+width]
        # cv2.imshow(str(x*y),imageCrop)
        count=cv2.countNonZero(imageCrop)
        cvzone.putTextRect(img,str(count),(x,y+height-3),scale=1,thickness=2,offset=0,colorR=(0,0,255))

        if count<900:
            color=(0,255,0)
            thickness=5
            spaceCounter+=1
        else:
            color=(0,0,255)
            thickness=2

        cv2.rectangle(img,pos,(pos[0]+width,pos[1]+height),color,thickness)

    cvzone.putTextRect(img,f'Free: {spaceCounter}/{len(posList)}', (100, 50), scale=3, thickness=5, offset=20, colorR=(0, 255,0))


while True:
    success, img = cap.read()
    if cap.get(cv2.CAP_PROP_POS_FRAMES) == cap.get(cv2.CAP_PROP_FRAME_COUNT):
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
    imgGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    imgBlur=cv2.GaussianBlur(imgGray,(3,3),1)
    imgThreshold=cv2.adaptiveThreshold(imgBlur,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                       cv2.THRESH_BINARY_INV,25,16)
    imgMedian=cv2.medianBlur(imgThreshold,5)
    kernel=np.ones((3,3),np.uint8)
    imgdilate=cv2.dilate(imgMedian,kernel,iterations=1)
    checkParkingSpace(imgdilate)





    cv2.imshow("Image",imgdilate)
    cv2.imshow("Image2",imgThreshold)
    cv2.imshow("Image3",img)
    
    if cv2.waitKey(3) & 0XFF==ord('q'):
        break
