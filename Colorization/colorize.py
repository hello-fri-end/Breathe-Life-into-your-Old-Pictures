#import the necessary packages
import numpy as np
import argparse
import cv2

# construct the argument parser & parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str , required=True,
        help = "path to input bnw image")
ap.add_argument("-p", "--prototxt", type=str, required=True,
        help = "path to Caffe prototxt file")
ap.add_argument("-m", "--model", type=str, required=True,
        help = "path to Caffe pre-trained model")
ap.add_argument("-c", "--points", type=str, required=True,
        help="path to cluster center points")
args = vars(ap.parse_args())

# load the model & cluster points from the disk
print("[INFO] loading model . . .")
print(args["prototxt"])
print(args["model"])
net = cv2.dnn.readNetFromCaffe(args["prototxt"], args["model"])
pts = np.load(args["points"])

# add the cluster centers as 1x1 convolutions to the model
class8 = net.getLayerId('class8_ab')
conv8 = net.getLayerId('conv8_313_rh')
pts = pts.transpose().reshape(2, 313, 1, 1)
net.getLayer(class8).blobs = [pts.astype("float32")]
net.getLayer(conv8).blobs = [np.full([1, 313], 2.606, dtype = "float32")]


# load the image
image = cv2.imread(args["image"])
# scale the image to have values between 0 & 1
scaled = image.astype("float32") / 255.0
# convert the image to lab color space
lab = cv2.cvtColor(scaled, cv2.COLOR_BGR2LAB)

# resize the image to 224x224 (the dimensions the
# colorization models accepts)
resized = cv2.resize(lab, (224, 224))
# split the L channel
L = cv2.split(resized) [0] 
# perform mean centering
L -= 50

# pass the L channel through the network which
# will predict the 'a' and 'b' channel values
print("[INFO] colorizing image . . .")
net.setInput(cv2.dnn.blobFromImage(L))
ab = net.forward()[0, :, :, :].transpose((1, 2, 0))

# resize the 'ab' volumne to the same dimensions as our
# input image
ab = cv2.resize(ab, (image.shape[1], image.shape[0]))

# grab the 'L' channel from the *original* input image
# and concatenate the original 'L' channel with the 
# predicted 'ab' channels
L = cv2.split(lab)[0]
colorized = np.concatenate((L[:, :, np.newaxis], ab), axis=2)

# convert to RGB
colorized = cv2.cvtColor(colorized, cv2.COLOR_LAB2BGR)
colorized = np.clip(colorized, 0, 1)

# currently the colorized image is represented as a floating point
# data type in the range(0,1) -- let's convert to an unsigned 
# 8-bit inter representation in the range [0,255]
colorized = (255 * colorized).astype("uint8")

#show the original & output colorized images
#cv2.imshow("Original", image)
#cv2.imshow("Colorized", colorized)
#cv2.waitkey(0)

outputFile = 'output.png'
cv2.imwrite(outputFile, (colorized))
print('Colorized image saved')

