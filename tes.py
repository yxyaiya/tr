import cv2
import os

from sklearn.feature_extraction import img_to_graph
a=[520,13,14]*1000
print(a)
path = r'C:\Users\Administrator\Desktop\新建文件夹 (3)\1.jpg'
img =cv2.imread('1.jpg,2.jpg,3.jpg',cv2.IMREAD_UNCHANGED)
for i in range (3):
                cv2.imshow ('IMAG',img)
                K=cv2.waitKey(0)



