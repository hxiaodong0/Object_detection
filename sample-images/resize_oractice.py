import cv2
import glob
#load, resize, import, export
images = glob.glob("*.jpg")

for item in images:
    img = cv2.imread(item,0)
    resized = cv2.resize(img,(500,500))
    cv2.imshow("show",resized)
    cv2.waitKey(2000)
    cv2.destroyAllWindows()
    cv2.imwrite()