import cv2
import numpy as np

def equalize_histogram(image):
    try:
        image = np.array(image)
    except:
        pass
    # convert the image to YCRCB SPACE
    # in a future version add options for differnt color spaces
    imgCopy = image.copy()
    ycrcb=cv2.cvtColor(imgCopy,cv2.COLOR_RGB2YCR_CB)
    channels=cv2.split(ycrcb)
    cv2.equalizeHist(channels[0],channels[0])
    cv2.merge(channels,ycrcb)
    cv2.cvtColor(ycrcb,cv2.COLOR_YCR_CB2RGB,imgCopy)
    return imgCopy
