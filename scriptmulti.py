import glob
import cv2

images=glob.glob('*.jpg')

for image in images:
    img=cv2.imread(image,0)
    img=cv2.resize(img,(100,100))
    cv2.imshow("hey",img)
    cv2.waitKey(1000)
    cv2.destroyAllWindows
    cv2.imwrite('image'+image,img)