import cv2
image = cv2.imread('gopal.jpg')
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

(humans,_) = hog.detectMultiScale(image,winStride=(10,10),padding=(32,32),scale=1.1)
print('Human detected : ',len(humans))
for(x,y,w,h)in humans:
    pad_w,pad_h = int(0.15 * w),int(0.01*h)
    cv2.rectangle(image, (x + pad_w, y + pad_h), (x+w - pad_w, y + h-pad_h), (0,255,0),2)
    
    cv2.imshow("Image",image)
    cv2.waitkey(0)
    cv2.destroyAllWindows()
