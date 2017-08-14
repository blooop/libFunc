# http://www.pyimagesearch.com/2015/04/06/zero-parameter-automatic-canny-edge-detection-with-python-and-opencv/
import cv2
import numpy as np
from matplotlib import pyplot as plt
import glob
import time
import os
import cPickle as pickle
from libfunc import *

#test
def loadImgAsGrayscale(path):
    img = cv2.imread(path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # Converting to GrayScale
    return gray


def auto_canny(image, sigma=0.33):
    # compute the median of the single channel pixel intensities
    v = np.median(image)
    print v

    # apply automatic Canny edge detection using the computed median
    lower = int(max(0, (1.0 - sigma) * v))
    upper = int(min(255, (1.0 + sigma) * v))
    print "lower", lower
    print "upper", upper
    edged = cv2.Canny(image, lower, upper)

    # return the edged image
    return edged


def thres():
    # Set threshold and maxValue
    thresh = 20
    maxValue = 255
    # th, dst = cv2.threshold(img, thresh, maxValue, cv2.THRESH_BINARY)


def mser(image):
    vis = image.copy()
    mser = cv2.MSER_create()
    regions = mser.detectRegions(image, None)
    hulls = [cv2.convexHull(p.reshape(-1, 1, 2)) for p in regions]
    cv2.polylines(vis, hulls, 1, (0, 255, 0))
    return vis


def plotSideBySide(img1, img2):
    plt.subplot(121), plt.imshow(img1, cmap='gray')
    plt.title('Original Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(122), plt.imshow(img2, cmap='gray')
    plt.title('Processed Image'), plt.xticks([]), plt.yticks([])
    mng = plt.get_current_fig_manager()
    mng.window.showMaximized()
    plt.show()


def getTifInfolder(folder, filter):
    output = []
    paths = []
    for imagePath in glob.glob("Neurons" + "/*.tif"):
        if filter in imagePath:
            paths.append(imagePath)
            output.append(loadImgAsGrayscale(imagePath))
    return output, paths


def createHist(control, experiments):
    minbin = 0
    maxbin = 256

    histControl = cv2.calcHist(controls, [0], None, [maxbin - minbin], [minbin, maxbin])
    histExperiment = cv2.calcHist(experiments, [0], None, [maxbin - minbin], [minbin, maxbin])

    # histControl,binsC = np.histogram(controls[0].ravel(),256,[minbin,256])
    # histExperiment,binsE = np.histogram(experiments[0].ravel(),256,[minbin,256])

    plt.subplot(2, 1, 1)
    plt.title("Control & Experiment mean histogram")
    plt.plot(histControl, label='Control')
    plt.plot(histExperiment, label='Experiment')
    plt.legend()
    plt.subplot(2, 1, 2)
    plt.title("Mean Histogram Difference")
    plt.title("Difference")
    plt.plot(histExperiment - histControl)
    plt.show()


def plotThreshMasked(imagelist):
    rawIntegratedDen = []
    area = []
    subplot_n = 1
    subplot_thresh = 2
    for i in range(len(imagelist)):
        img = imagelist[i]
        th, dst = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        masked = cv2.bitwise_and(img, img, mask=dst)
        # This is to show images and masked img:
        plt.subplot(4, len(imagelist) / 2, subplot_n), plt.imshow(img, cmap='gray')
        subplot_n += 2
        plt.title('Original Image'), plt.xticks([]), plt.yticks([])
        plt.subplot(4, len(imagelist) / 2, subplot_thresh), plt.imshow(dst, cmap='gray')
        subplot_thresh += 2
        plt.title('Processed Image'), plt.xticks([]), plt.yticks([])

    mng = plt.get_current_fig_manager()
    mng.window.showMaximized()
    plt.show()


def calculateRIDandArea(imagelist):
    rawIntegratedDen = []
    area = []
    for i in range(len(imagelist)):
        img = imagelist[i]
        th, dst = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        masked = cv2.bitwise_and(img, img, mask=dst)
        rawIntegratedDen.append(cv2.sumElems(masked)[0])
        area.append(cv2.sumElems(dst)[0] / 255)
    return rawIntegratedDen, area
    # This is to show images and masked img
    #     plt.subplot(4, len(imagelist) / 2, i + 1), plt.imshow(img, cmap='gray')
    #     plt.title('Original Image'), plt.xticks([]), plt.yticks([])
    #     plt.subplot(4, len(imagelist) / 2, i + 1 + len(imagelist)), plt.imshow(masked, cmap='gray')
    #     plt.title('Processed Image'), plt.xticks([]), plt.yticks([])
    #
    # mng = plt.get_current_fig_manager()
    # mng.window.showMaximized()
    # plt.show()

