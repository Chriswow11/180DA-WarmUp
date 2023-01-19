# https://code.likeagirl.io/finding-dominant-colour-on-an-image-b4e075f98097
# https://machinelearningprojects.net/most-dominant-colors-in-an-image/
# https://medium.com/buzzrobot/dominant-colors-in-an-image-using-k-means-clustering-3c7af4622036

import cv2
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

clusters = 2
const_width = 500
const_height = 250

cap = cv2.VideoCapture(0)

while(True):
	__, frame = cap.read()
	frame = cv2.flip(frame, 1)

	width = cap.get(3)
	height = cap.get(4)

	c_width = int(width/2)
	c_height = int(height/2)

	rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

	rgb_rect = rgb[(c_height-const_height,c_height+const_height),(c_width-const_width,c_width+const_width)]

	kmeans = KMeans(n_clusters = clusters)
	kmeans.fit(rgb_rect)

	colors = np.array(kmeans.cluster_centers_,dtype='uint')

	(hist, _) = np.histogram(colors, bins = clusters)
	hist = hist.astype("float")
	hist /= hist.sum()

	colors = colors[(-hist).argsort()]

	dom_color = colors[0]

	print(dom_color)

	frame = cv2.rectangle(frame,(c_width-const_width,c_height-const_height), (c_width+const_width,c_height+const_height),(int(dom_color[2]),int(dom_color[1]),int(dom_color[0])), 15)

	cv2.imshow('frame',frame)

	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()