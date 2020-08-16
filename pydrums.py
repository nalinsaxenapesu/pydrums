def play():
    from playsound import playsound
    playsound('Snare-Drum-Hit-Level-6a-www.fesliyanstudios.com.mp3')




import numpy as np
import cv2
import winsound
import multiprocessing
p1 = multiprocessing.Process(target=play) 
cap = cv2.VideoCapture(0)

while 1:
    ret, img = cap.read()
    hsv_frame=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    
     
    #lower_red = np.array([0,120,70])

    #upper_red = np.array([10,255,255])

    #mask1 = cv2.inRange(hsv_frame, lower_red, upper_red)
 



    #lower_red = np.array([0,100,100])

    #upper_red = np.array([352,74,100])

   # mask2 = cv2.inRange(hsv_frame,lower_red,upper_red)
    kernel = np.ones((5, 5), np.uint8)
    
    ##BLUE MASK
    #low_blue = np.array([94, 80, 2])
    #high_blue = np.array([126, 255, 255])
    #blue_mask = cv2.inRange(hsv_frame, low_blue, high_blue)
    #blue = cv2.bitwise_and(img,img, mask=blue_mask)
    
    #GREEN MASK
    low_green = np.array([25, 52, 72])
    high_green = np.array([102, 255, 255])
    green_mask = cv2.inRange(hsv_frame, low_green, high_green)
    green = cv2.bitwise_and(img, img, mask=green_mask)
    blue=green

    cv2.circle(blue,(100,300), 70, (0,0,255), 1)
    cv2.circle(blue,(500,300), 70, (0,0,255), 1)
    font = cv2.FONT_HERSHEY_SIMPLEX 
    org = (50, 300) 
    fontScale = 1
    color = (200, 120, 50) 
    thickness = 2
    
    opening = cv2.morphologyEx(green_mask, cv2.MORPH_OPEN, kernel)
    closing = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel)

    ret, thresh = cv2.threshold(closing, 127, 255, 0)
    contours, hierarchy = cv2.findContours(thresh, 1, 2)
    contours = sorted(contours, key=lambda x: cv2.contourArea(x), reverse=True)
    #contours=contours[0]
    
    
    for cnt in contours:
        
        (x, y, w, h) = cv2.boundingRect(cnt)
            
        #cv2.drawContours(blue, [cnt], -1, (0, 0, 255), 1)
        cv2.rectangle(blue, (x, y), (x + w, y + h), (0, 255, 0), 1)
        print(x,y)
        flag=0
        if(x>45 and x<150 ) and (y>250 and y<350):
            
            print("inside")
            flag=1
            from playsound import playsound
            playsound('smash.wav')
        
        if(x>425 and x<550 ) and (y>250 and y<350):
            from playsound import playsound
            playsound('lowSnare.wav')
            
            
        
    
    
    
    blue= cv2.putText(blue, 'snare', org, font,  
                   fontScale, color, thickness, cv2.LINE_AA) 
    blue= cv2.putText(blue, 'other drum', (400,300), font,  
                   0.5, color, thickness, cv2.LINE_AA) 
    blue= cv2.putText(blue, 'stuff', (420,320), font,  
                   1, color, thickness, cv2.LINE_AA) 
    #red_mask=mask1+mask2
    
    #final=cv2.bitwise_and(img,img,mask=mask2)
   
    cv2.imshow('webcam',img)
    cv2.imshow('hsv',blue)
 
    key=cv2.waitKey(1)
    if key==27:
        break
cap.release()
cv2.destroyAllWindows()
