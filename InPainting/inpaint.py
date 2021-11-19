import numpy as np
from PIL import Image
from streamlit_drawable_canvas import st_canvas
import streamlit as st
import cv2

def inpaint(image):
    stroke_width = st.sidebar.slider("Stroke Width: ", 1, 25, 3)
    inpaintRadius = st.sidebar.slider("Inpaint Radius: ", 1, 25, 3)
    drawing_mode = st.sidebar.selectbox(
            "Drawing tool:", ("freedraw", "line", "rect", "circle", "transform"))
    realtime_update = st.sidebar.checkbox("Update in realtime", True)
    try:
        image = Image.fromarray(image.astype('uint8'), 'RGB')
    except:
        pass

    canvas_result = st_canvas(
            stroke_color='#fff',
            stroke_width=stroke_width,
            background_color='#000',
            background_image=image,
            height=image.size[1],
            width=image.size[0],
            update_streamlit=realtime_update,
            drawing_mode = drawing_mode,
            key = "canvas",
            )

    if st.button("INPAINT"):
        image = np.array(image, dtype = 'uint8')
        mask = np.array(canvas_result.image_data, dtype = 'uint8')
        mask = cv2.cvtColor(mask[:, :, :3], cv2.COLOR_RGB2GRAY)
        st.image(mask)
        res = cv2.inpaint(src = image, inpaintMask = mask, inpaintRadius = inpaintRadius, flags = cv2.INPAINT_TELEA)
        previous, current = st.columns(2)

        previous.header("Original Image")
        previous.image(st.session_state["current"], use_column_width=True)
        
        current.header("Result Image")
        current.image(res, use_column_width=True)
        st.session_state["inpaint"] = res

    if st.button("Save Changes"):
        st.session_state["current"] = st.session_state["inpaint"]
