# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 21:02:29 2016

@author: charles
"""

from struct import *
import numpy as np

def binaryToFloatArray(binary):
    nbFloats = len(binary)/4
    return np.array(unpack(str(nbFloats) + 'f', binary))