from colordescriptor import colordescriptor
from searcher import Searcher
import argparse
import cv2

argument = argparse.ArgumentParser()
argument.add_argument("-i", "--index", required = True, help = "Path of index csv")
argument.add_argument("-q", "--query", required = True, help = "Path to the query image")
argument.add_argument("-r", "--result", required = True, help = "Path to the result image")
args = vars(argument.parse_args())

cd = colordescriptor((10, 10, 10))

query = cv2.imread(args["query"])
features = cd.describe(query)

searcher = Searcher(args["index"])
results = searcher.search(features)

cv2.imshow("Query Image", query)

for (value, imageID) in results:
	output = cv2.imread(imageID)
	cv2.imshow("Searched Image", output)
	cv2.waitKey(1000)