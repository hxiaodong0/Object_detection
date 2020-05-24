import args as args
import cv2

face_cascade = cv2.CascadeClassifier("/Users/xiaodonghuo/PycharmProjects/computer_vision/haarcascade_frontalface_default.xml")

img = cv2.imread("/Users/xiaodonghuo/PycharmProjects/computer_vision/photo1.jpg")
img = cv2.resize(img, (int(img.shape[1]* 0.5), int(img.shape[0]*0.5)))
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

face = face_cascade.detectMultiScale(gray_img , scaleFactor= 1.05, minNeighbors = 5)

#[[157  84 379 379]]   [[column   row , length, length]]
cnts = cv2.findContours(gray_img,mode=cv2.RETR_EXTERNAL, method=cv2.CHAIN_APPROX_SIMPLE)[0]

for contours in cnts:
    print(contours)
    cv2.drawContours(img, contours, -1, (255, 255, 0), 3)
for x, y, w,h in face:
    img = cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 3 )  #blue,greed, red, weith of the rectangle

resize = cv2.resize(img,((int(img.shape[1]* 0.5), int(img.shape[0]*0.5))))
cv2.imshow("gray",resize)
cv2.waitKey(0)
cv2.destroyAllWindows()

# cascade_fn = args.get('--cascade', "/Users/xiaodonghuo/PycharmProjects/computer_vision/haarcascade_frontalface_default.xml")
# nested_fn  = args.get('--nested-cascade', "/Users/xiaodonghuo/PycharmProjects/computer_vision/haarcascade_frontalface_default.xml")
