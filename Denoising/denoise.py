import numpy as np
import cv2

def denoise(img, h, photo_render, search_window, block_size):
    img = np.array(img)
    return cv2.fastNlMeansDenoisingColored(img, None, h, photo_render, search_window, block_size )
