import cv2 

eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
def detect(gray ,frame):
    eyes =eye_cascade.detectMultiScale(gray, 1.1, 3)
    for (x,y ,w ,h) in eyes :
        cv2.rectangle(frame , (x,y), (x+w ,y+h) , (255,0,0) ,2 )
        roi_gray = gray[ y:y+h ,x:x+w ]
        roi_color = frame[y:y+h ,x:x+w ]     
    return frame 

capture = cv2.VideoCapture(0)
while True :
     _, frame =capture.read()
     gray = cv2.cvtColor(frame , cv2.COLOR_BGR2GRAY)
     canvas =detect(gray,frame) 
     cv2.imshow('Eye',canvas) 
     if cv2.waitKey(1) & 0xFF == ord('q'): 
            break
capture.release()
cv2.destroyAllWindows()
 
 
        
        

