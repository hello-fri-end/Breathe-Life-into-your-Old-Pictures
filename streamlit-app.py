import streamlit as st
import numpy as np
from PIL import Image
#import Restoration methods
from Colorization import colorize
from InPainting import inpaint
from Denoising import denoise
from histogramEqulization import equalize_histogram
from adaptiveHistogramEqualization import CLAHE
from SuperRez import superRez
from Download import getImageLink

def main():
    st.set_page_config(layout="wide")
    st.title("Bring your old pictures back to life!")

    #define states of the app
    uploadPage = "Upload a new image"
    colorizationPage = "Image Colorization"
    inpaintingPage = "Image Inpainting"
    denoisingPage = "Image Denoising"
    histogramEqPage = "Histogram Equalization"
    adapHistogramEqPage = " Constrast Limited Adaptive Histogram Equalization"
    superRezPage = "Super Resolution"
    comparisonPage = "Compare with original image"

    appMode = st.sidebar.selectbox(
            "Choose the app mode",
            [
             uploadPage,
             colorizationPage,
             inpaintingPage,
             denoisingPage,
             histogramEqPage,
             adapHistogramEqPage,
             superRezPage,
             comparisonPage
             ])

    st.header(appMode)

    if appMode == uploadPage:
      imgFile = st.file_uploader("Choose an image file")
      if imgFile is None:
          st.text("You haven't uploaded an image file")
      else:
          image = Image.open(imgFile)
          image = image.convert(mode="RGB")
          st.session_state['current'] = image 
          st.session_state['original'] = image
          st.image(image)

    # run the python script corresponding to appMode
    result = None

    # image colorization
    if appMode == colorizationPage:
      result = None
      result = colorize.colorize(st.session_state['current'])

    # image inpainting
    if appMode == inpaintingPage:
      inpaint.inpaint(st.session_state["current"])


    # image denoising
    if appMode == denoisingPage:
      # get the paramters for denoising
      h = st.sidebar.slider("Filter Strength", 1, 25, 10)
      photo_render = st.sidebar.slider("Color Filter Strength", 1, 25, 10)
      search_window = st.sidebar.slider("Search Window Size", 1, 50, 21)
      block_size = st.sidebar.slider("Block Size", 1, 25, value = 7, step = 2)
      #get the denoised image
      result = denoise.denoise(st.session_state['current'], h, photo_render, search_window, block_size)

    # comparison page
    if appMode == comparisonPage:
      result = None
      original, current = st.columns(2)

      original.header("Original Image")
      original.image(st.session_state["original"], use_column_width = True)

      current.header("Result Image")
      current.image(st.session_state["current"], use_column_width = True)
      if st.button("Generate Download Link") :
      	st.markdown(getImageLink.getImageLink(st.session_state["current"]), unsafe_allow_html=True)

    if appMode == histogramEqPage:
        result = equalize_histogram.equalize_histogram(st.session_state["current"])


    if appMode == adapHistogramEqPage:
        result = CLAHE.CLAHE(st.session_state["current"])
    
    if appMode == superRezPage:
    	status = st.radio("Select Scaling factor: ", ('2x', '3x', '4x'))
    	temp = superRez.superRez(st.session_state["current"], 2)
    	if status == '3x':
    		temp = superRez.superRez(st.session_state["current"], 3)
    	elif status == '4x':
    		temp = superRez.superRez(st.session_state["current"], 4)
    	else:
    		temp = superRez.superRez(st.session_state["current"], 2)
    	if temp.size < 20000000:
    		result = temp
    	else:
    		st.warning("Image size will become too big")
    
    #display the result
    if result is not None:
        previous, current = st.columns(2)

        previous.header("Original Image")
        previous.image(st.session_state["current"], use_column_width=True)
        
        current.header("Result Image")
        current.image(result, use_column_width=True)
        if st.button("Save Changes"):
            st.session_state["current"] = result

if __name__ == '__main__':
    main()
