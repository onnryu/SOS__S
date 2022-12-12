import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)

while(1):
    ret,frame = cap.read()
    frame = cv2.flip(frame,1)
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray,1.1,5)

    print ("Number of faces detected: "+str(len(faces)))

    if len(faces):
        for(x,y,w,h) in faces:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)

    cv2.imshow('result',frame)

    k = cv2.waitKey(30)&0xff
    if k ==27 or k==48:
        break

cap.release()
cv2.destroyAllWindows()