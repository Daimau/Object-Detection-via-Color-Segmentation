import cv2

image = cv2.imread('Containers.png')
original_image = image

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

edges = cv2.Canny(gray, 50, 200)

contours, hierarchy = cv2.findContours(edges.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

cv2.destroyAllWindows()


def get_contour_areas(contours):
    all_areas = []

    for cnt in contours:
        area = cv2.contourArea(cnt)
        all_areas.append(area)

    return all_areas


sorted_contours = sorted(contours, key=cv2.contourArea, reverse=True)

largest_item = sorted_contours[0]

cv2.drawContours(original_image, largest_item, -1, (255, 0, 0), 10)
cv2.waitKey(0)
cv2.imshow('Largest Object', original_image)

cv2.waitKey(0)
cv2.destroyAllWindows()

import cv2

image = cv2.imread('Containers.png')
original_image = image

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

edges = cv2.Canny(gray, 50, 200)

contours, hierarchy = cv2.findContours(edges.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
print('Number of contours found = ', len(contours))


def get_contour_areas(contours):
    all_areas = []

    for cnt in contours:
        area = cv2.contourArea(cnt)
        all_areas.append(area)

    return all_areas


sorted_contours = sorted(contours, key=cv2.contourArea, reverse=False)

smallest_item = sorted_contours[0]

cv2.drawContours(original_image, smallest_item, -1, (255, 0, 0), 10)
cv2.waitKey(0)
cv2.imshow('Smallest Object', original_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
#
# # import the necessary packages
# import cv2
#
#
# class ShapeDetector:
#     def _init_(self):
#         pass
#
#     def detect(self, c):
#         # initialize the shape name and approximate the contour
#         shape = "unidentified"
#         peri = cv2.arcLength(c, True)
#         approx = cv2.approxPolyDP(c, 0.04 * peri, True)
#
#         # if the shape is a triangle, it will have 3 vertices
#         if len(approx) == 3:
#             shape = "triangle"
#         # if the shape has 4 vertices, it is either a square or
#         # a rectangle
#         elif len(approx) == 4:
#             # compute the bounding box of the contour and use the
#             # bounding box to compute the aspect ratio
#             (x, y, w, h) = cv2.boundingRect(approx)
#             ar = w / float(h)
#             # a square will have an aspect ratio that is approximately
#             # equal to one, otherwise, the shape is a rectangle
#             shape = "square" if ar >= 0.95 and ar <= 1.05 else "rectangle"
#         # if the shape is a pentagon, it will have 5 vertices
#         elif len(approx) == 5:
#             shape = "pentagon"
#         # otherwise, we assume the shape is a circle
#         else:
#             shape = "circle"
#         # return the name of the shape
#         return shape
#
#
# # import the necessary packages
# from pyimagesearch.shapedetector import ShapeDetector
# import argparse
# import imutils
# import cv2
#
# # construct the argument parse and parse the arguments
# ap = argparse.ArgumentParser()
# ap.add_argument("-i", "--image", required=True,
#                 help="path to the input image")
# args = vars(ap.parse_args())
#
# # load the image and resize it to a smaller factor so that
# # the shapes can be approximated better
# image = cv2.imread(args["image"])
# resized = imutils.resize(image, width=300)
# ratio = image.shape[0] / float(resized.shape[0])
# # convert the resized image to grayscale, blur it slightly,
# # and threshold it
# gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
# blurred = cv2.GaussianBlur(gray, (5, 5), 0)
# thresh = cv2.threshold(blurred, 60, 255, cv2.THRESH_BINARY)[1]
# # find contours in the thresholded image and initialize the
# # shape detector
# cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
#                         cv2.CHAIN_APPROX_SIMPLE)
# cnts = imutils.grab_contours(cnts)
# sd = ShapeDetector()
#
# # loop over the contours
# for c in cnts:
#     # compute the center of the contour, then detect the name of the
#     # shape using only the contour
#     M = cv2.moments(c)
#     cX = int((M["m10"] / M["m00"]) * ratio)
#     cY = int((M["m01"] / M["m00"]) * ratio)
#     shape = sd.detect(c)
#     # multiply the contour (x, y)-coordinates by the resize ratio,
#     # then draw the contours and the name of the shape on the image
#     c = c.astype("float")
#     c *= ratio
#     c = c.astype("int")
#     cv2.drawContours(image, [c], -1, (0, 255, 0), 2)
#     cv2.putText(image, shape, (cX, cY), cv2.FONT_HERSHEY_SIMPLEX,
#                 0.5, (255, 255, 255), 2)
#     # show the output image
#     cv2.imshow("Image", image)
#     cv2.waitKey(0)
# $ python detect_shapes.py --image shapes_and_colors.png