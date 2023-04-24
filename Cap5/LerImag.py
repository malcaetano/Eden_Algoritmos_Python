import numpy as np
import cv2
import os 
import glob 

#img_dir="D:\Pictures\Nikon Transfer 2\Blend" # Enter Directory of all images  
#data_path = os.path.join('*ng') 
#files = glob.glob(data_path) 
data = [] 
#for f1 in files: 
img = cv2.imread('Num1.png')
linhas,col,elem=np.array(img).shape 
img2=np.ones([linhas,col,elem])*255
for i in range(linhas):
    for j in range(col):
        for k in range(elem):
                   if img2[i,j,k]>img[i,j,k]:
                       img2[i,j,k]=0.5
                
            
#img2=np.ones([linhas,col,elem])
#img3=img+img2
    
cv2.imshow("Output",img2)
#cv2.imwrite('SaidaF.jpg', im_blend)

