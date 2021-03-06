import math
import numpy as np

PIB2 = math.pi / 2.0
PIB4 = math.pi /4.0
PI = math.pi
PI2 = math.pi * 2.0

deg2rad = 180.0/math.pi
rad2deg = math.pi/180.0

def a2v(angle):
    return np.array([math.cos(angle), math.sin(angle)])

def v2a(vec):
    return math.atan2(vec[1],vec[0])

def v2ad(vec):
    return math.atan2(vec[1],vec[0])*deg2rad

def vecLen(vec):
    return math.sqrt(vec[0]*vec[0]+vec[1]*vec[1])

def lerp(value, inputLow, inputHigh, outputLow, outputHigh):
    inputLow = float(inputLow)
    return outputLow + ((float(value) - inputLow) / (float(inputHigh) - inputLow)) * (float(outputHigh) - outputLow)

def rolling_window(array, window, step_size=1):
    shape = array.shape[:-1] + (array.shape[-1] - window + 1 - step_size, window)
    strides = array.strides + (array.strides[-1] * step_size,)
    return np.lib.stride_tricks.as_strided(array, shape=shape, strides=strides)

