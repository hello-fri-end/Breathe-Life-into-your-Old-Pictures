import streamlit as st
import numpy as np
from PIL import Image
#import Restoration methods
from Colorization import colorize
from ImproveLighting import  night_images
from InPainting import inpaint
from Denoising import denoise


def main():
    st.title("Image Restoration")

    #define states of the app
    colorizationPage = "Image Colorization"
    inpaintingPage = "Image Inpainting"
    enhancementPage = "Image Enhacement"
    denoisingPage = "Image Denoising"

    appMode = st.sidebar.selectbox(
            "Choose the app mode",
            [
             colorizationPage,
             inpaintingPage,
             enhancementPage,
             denoisingPage
             ])

    st.header(appMode)
    
    # prompt for uploading an image
    imgFile = st.file_uploader("Choose an image file")
    if imgFile is None:
        st.text("You haven't uploaded an image file")
    else:
        image = Image.open(imgFile)

        # run the python script corresponding to appMode

        # image colorization
        if appMode == colorizationPage:
            original, colorized = st.columns(2)
            # get the colorized image
            result = colorize.colorize(image)
            #display the images side by side
            original.header("Original")
            original.image(image, use_column_width = True)
            colorized.header("Colorized")
            colorized.image(result, use_column_width = True)

        # image enhancement
        if appMode == enhancementPage:
            original, enhanced = st.columns(2)
            # get the enhanced image
            res = night_images.enhance(image)
            # display the images
            original.header("Original Image")
            original.image(image, use_column_width = True)

            enhanced.header("Denoised Image")
            enhanced.image(res, use_column_width = True)

        # image inpainting
        if appMode == inpaintingPage:
            image1, image2 = st.columns(2)
            # get the inpainted images

            res1,res2 = inpaint.inpaint(image)
            if res1 is not None:
                image1.header("Using Fast Marching Method")
                image1.image(res1, use_column_width = True)

                image2.header("Using Navier Stokes Method")
                image2.image(res2, use_column_width = True)

        # image denoising
        if appMode == denoisingPage:
            original, denoised = st.columns(2)
            # get the paramters for denoising
            h = st.sidebar.slider("Filter Strength", 1, 25, 10)
            photo_render = st.sidebar.slider("Color Filter Strength", 1, 25, 10)
            search_window = st.sidebar.slider("Search Window Size", 1, 50, 21)
            block_size = st.sidebar.slider("Block Size", 1, 25, value = 7, step = 2)
            #get the denoised image
            res = denoise.denoise(image, h, photo_render, search_window, block_size)
            #display the images
            original.header("Original Image")
            original.image(image, use_column_width = True)

            denoised.header("Denoised Image")
            denoised.image(res, use_column_width = True)






if __name__ == '__main__':
    main()
