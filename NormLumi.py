import cv2
import numpy as np
import glob
import os,sys




inputfolder=(r'C:\') #your input folder 
list = os.listdir(inputfolder)
number_files = len(list)
print( " number of file at input folder==",number_files)

os.mkdir('output') #output folder
i=0

for img in glob.glob(inputfolder + "/*.*"):  


   image=cv2.imread(img)
   hsv=cv2.cvtColor(image,cv2.COLOR_RGB2HSV)
   normalizedImg = np.zeros((1200, 1200),dtype=np.uint8)
   hsv[:,:,2]=cv2.normalize(hsv[:,:,2],normalizedImg,0,255,cv2.NORM_MINMAX)

   test = cv2.cvtColor(hsv, cv2.COLOR_HSV2RGB)


   cv2.imwrite("output/image%04i.bmp"%i,test)  #desired format. I selected BMP which is perfect works with E-Prime 3.0 and E-Prime 2.0.
   i +=1


   cv2.waitKey(0)
