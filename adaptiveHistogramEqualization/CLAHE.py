import cv2
import streamlit as st
import numpy as np

def CLAHE(image):
    try:
        image = np.array(image, dtype='uint8')
    except:
        pass
    # convert the image to YCRCB SPACE
    # in a future version add options for differnt color spaces
    imgCopy = image.copy()
    ycrcb = cv2.cvtColor(imgCopy,cv2.COLOR_RGB2YCR_CB)
    channels = cv2.split(ycrcb)
    channels = list(channels)

    clipLimit = st.sidebar.slider("Clip Limit", 1, 25, 2)
    tileGridRows = st.sidebar.slider("Tile Grid Rows", 1, 25, 8) 
    tileGridColumns = st.sidebar.slider("Tile Grid Columns", 1, 25, 8) 

    clahe = cv2.createCLAHE(clipLimit=clipLimit, tileGridSize=(tileGridRows, tileGridColumns))
    channels[0] = clahe.apply(channels[0])
    cv2.merge(channels,ycrcb)
    cv2.cvtColor(ycrcb,cv2.COLOR_YCR_CB2RGB,imgCopy)
    return imgCopy
