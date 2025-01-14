import numpy as np
import cv2
from matplotlib import pyplot as plt


img = cv2.imread('DJI_0002.jpg')
mask = np.zeros(img.shape[:2],np.uint8)
bgdModel = np.zeros((1,65),np.float64)
fgdModel = np.zeros((1,65),np.float64)
rect = (0,500,3000,2000)#划定区域
cv2.grabCut(img,mask,rect,bgdModel,fgdModel,5,cv2.GC_INIT_WITH_RECT)#函数返回值为mask,bgdModel,fgdModel
mask2 = np.where((mask==2)|(mask==0),0,1).astype('uint8')#0和2做背景

img = img*mask2[:,:,np.newaxis]#使用蒙板来获取前景区域



cv2.imshow('p',img)
cv2.imwrite('result.tif',img)
cv2.waitKey(0)
