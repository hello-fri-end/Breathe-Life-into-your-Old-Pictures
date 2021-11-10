import numpy as np
from streamlit_drawable_canvas import st_canvas
import streamlit as st
import cv2

def inpaint(image):
    stroke_width = st.sidebar.slider("Stroke Width: ", 1, 25, 3)
    inpaintRadius = st.sidebar.slider("Inpaint Radius: ", 1, 25, 3)
    drawing_mode = st.sidebar.selectbox(
            "Drawing tool:", ("freedraw", "line", "rect", "circle", "transform"))
    realtime_update = st.sidebar.checkbox("Update in realtime", True)

    canvas_result = st_canvas(
            stroke_color='#fff',
            stroke_width=stroke_width,
            background_color='#000',
            background_image=image.copy(),
            height = image.size[1],
            width = image.size[0],
            update_streamlit=realtime_update,
            drawing_mode = drawing_mode,
            key = "canvas",
            )

    if st.button("INPAINT"):
        image = np.array(image, dtype = 'uint8')
        mask = np.array(canvas_result.image_data, dtype = 'uint8')
        mask = cv2.cvtColor(mask[:, :, :3], cv2.COLOR_RGB2GRAY)
        st.image(mask)
        res1 = cv2.inpaint(src = image, inpaintMask = mask, inpaintRadius = inpaintRadius, flags = cv2.INPAINT_TELEA)
        res2 = cv2.inpaint(src = image, inpaintMask = mask, inpaintRadius = inpaintRadius, flags = cv2.INPAINT_NS)
        return res1, res2
    else:
        return None, None
