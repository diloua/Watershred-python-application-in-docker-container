import numpy as np 
from scipy.ndimage import gaussian_filter
from scipy.signal import medfilt2d
from numpy import genfromtxt
import sys

gaussian_data = genfromtxt("input/pre-gaussian.txt", delimiter=',', dtype='uint8')
gaussian_image = gaussian_filter(gaussian_data, sigma=2)

median_data = genfromtxt("input/pre-median.txt", delimiter=',', dtype='uint8')
median_image = medfilt2d(median_data, 3)

thresholding_data = genfromtxt("input/pre-th.txt", delimiter=',', dtype='uint8')
thresholding_image = ( thresholding_data > 100 ) * thresholding_data
np.savetxt('output/gaussian_filter.csv', gaussian_image, delimiter=',', fmt='%d')
np.savetxt('median_filter.csv', median_image, delimiter=',', fmt='%d')
np.savetxt('threshholding.csv', thresholding_image, delimiter=',', fmt='%d')

