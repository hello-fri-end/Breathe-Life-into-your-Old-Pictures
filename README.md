
# Breathe Life into your Old Pictures 

![Screenshot from 2021-11-20 11-28-47](https://user-images.githubusercontent.com/43880587/142716543-9ef6f478-7cca-43c6-b9cb-ce73902d0b11.png)



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li>
      <a href="#project-structure">Project Structure</a>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
      </ul>
    </li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

This is a tool to enhance your old/damaged pictures built using python & opencv. At the moment, the tool contains the following modules:
* Image Colorization: Passes your image through a pretrained CNN that colorizes the image ( it can even colorize colored images!). 
* Image Inpainting: Use the tool to draw over damaged parts of image & it will use Fast Marching Method to heal those regions.
* Image Denoising: Remove the noise in your image with openCV's fastNlMeansDenoising() method.
* Histogram Equalization: Poor contrast in your image? Don't worry, we've got you covered!
* Contrast Limited Histogram Equalization: Histogram Equalization not working out for you? Try this!
* Image Super-Resolution: Want to be able to display your images on a large screen? We've got you covered !  


## Project Structure
```
.
├── adaptiveHistogramEqualization
│   ├── CLAHE.py
├── Colorization
│   ├── colorize.py
│   ├── greyscaleImage.png
│   ├── output.png
├── Denoising
│   ├── denoise.py
├── Dockerfile
├── Download
│   ├── getImageLink.py
├── histogramEqulization
│   ├── equalize_histogram.py
├── InPainting
│   ├── inpaint.py
├── models
│   ├── colorization_deploy_v2.prototxt
│   ├── colorization_release_v2.caffemodel
│   ├── ESPCN_x2.pb
│   ├── ESPCN_x3.pb
│   ├── ESPCN_x4.pb
│   └── pts_in_hull.npy
├── README.md
├── requirements.txt
├── streamlit-app.py
└── SuperRez
    └── superRez.py
```

<!-- GETTING STARTED -->
## Getting Started

### Prerequisites
#### 1. Using pip to install the dependencies:
``` bash
pip install -r requirements.txt
```
Once the dependencies have been installed, use the following command to deploy the app locally:
```bash
streamlit run streamlit-app.py
```

#### 2. Building the app locally with Docker:
Assuming docker is running on your machine and you have a docker account, do the following:
- Build the image

``` bash
docker build -t <USERNAME>/<YOUR_IMAGE_NAME> .
```

- Run the image

``` bash
docker run -p 8501:8501 <USERNAME>/<YOUR_IMAGE_NAME>
```
- Open your browser and go to `http://localhost:8501/`


3. #### You can also use the hosted version
https://share.streamlit.io/hello-fri-end/breathe-life-into-your-old-pictures/streamlit-app.py


<!-- CONTACT -->
## Contact

Anwaar Khalid- [LinkedIn](https://www.linkedin.com/in/anwaar-khalid/) 
