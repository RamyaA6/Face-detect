import cv2
#Trained dataset
taset=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
#Read a image
img = cv2.imread("images/nick.jpeg")
# covert into grayscale
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
faces=taset.detectMultiScale(gray)
print(faces)
for x,y,w,h in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0) ,2)
cv2.imshow("Ramya",img)
# cv2.imshow("grays",gray)
cv2.waitKey()