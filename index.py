from colordescriptor import colordescriptor
import argparse
import glob
import cv2
import os
# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-d", "--dataset", required = True,help = "Path to the directory that contains the images to be indexed")
ap.add_argument("-i", "--index", required = True,help = "Path to where the computed index will be stored")
args = vars(ap.parse_args())
# initialize the color descriptor
cd = colordescriptor((20, 2, 4))

# open the output index file for writing
output = open(args["index"], "w")
# use glob to grab the image paths and loop over them
folder = 'dataset'
for filename in os.listdir(folder):
    name,ext = os.path.splitext(filename)
    for imagePath in glob.glob(args["dataset"] + "/*" + ext):
        # extract the image ID (i.e. the unique filename) from the image
        # path and load the image itself
        imageID = imagePath[imagePath.rfind("/") + 1:]
        image = cv2.imread(imagePath)
        # describe the image
        features = cd.describe(image)
        # write the features to file
        features = [str(f) for f in features]
        output.write("%s,%s\n" % (imageID, ",".join(features)))
# close the index file
output.close()
rows = open('index.csv').read().split('\n')
newrows = []
for row in rows:
    if row not in newrows:
        newrows.append(row)

f = open('index1.csv', 'w')
f.write('\n'.join(newrows))
f.close()