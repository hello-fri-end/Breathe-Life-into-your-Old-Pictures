import cv2
import numpy as np

def superRez(img, scale):
    #convert the PIL image to a numpy array
    img = np.array(img)
    
    if scale==3:
        sr = cv2.dnn_superres.DnnSuperResImpl_create()
        path = "./models/ESPCN_x3.pb"
        sr.readModel(path)
        sr.setModel("espcn",3)
        result = sr.upsample(img)
        return result
    elif scale==4:
        sr = cv2.dnn_superres.DnnSuperResImpl_create()
        path = "./models/ESPCN_x4.pb"
        sr.readModel(path)
        sr.setModel("espcn",4)
        result = sr.upsample(img)
        return result
    else:
        sr = cv2.dnn_superres.DnnSuperResImpl_create()
        path = "./models/ESPCN_x2.pb"
        sr.readModel(path)
        sr.setModel("espcn",2)
        result = sr.upsample(img)
        return result
