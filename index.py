from colordescriptor import colordescriptor
import argparse
import glob
import cv2
import os

argument = argparse.ArgumentParser()
argument.add_argument("-d", "--dataset", required = True,help = "Path to the dataset folder")
argument.add_argument("-i", "--index", required = True,help = "Path to where the index csv will be stored")
args = vars(argument.parse_args())

cd = colordescriptor((10, 10, 10))

file = open(args["index"], "w")

for image_path in glob.glob(args["dataset"] + "/*.jpg"):
    img = cv2.imread(image_path)
    features = cd.describe(img)
    features = [str(details) for details in features]
    file.write("%s,%s\n" % (image_path, ",".join(features)))

file.close()
