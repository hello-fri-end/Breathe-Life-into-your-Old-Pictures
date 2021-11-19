from PIL import Image
import io
import base64
import numpy as np

def getImageLink(img):
	buffered = io.BytesIO()
	if isinstance(img, np.ndarray):
		img = Image.fromarray(img)
	img.save(buffered, format="JPEG")
	img_str = base64.b64encode(buffered.getvalue()).decode()
	href = f'<a href="data:file/jpg;base64,{img_str}">Download result</a>'
	return href
