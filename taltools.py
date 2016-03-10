# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 14:53:04 2016

@author: 3000120
"""

import numpy as np
from scipy.sparse import lil_matrix

def string2trigram(s):
    size = len(s)
    nps = np.fromstring(s, dtype=np.uint8).astype(int) % 128
    tab3G = np.zeros((size+2, 3), int)
    
    tab3G[:-2, 0] = nps * 128**2
    tab3G[1:-1, 1] = nps * 128
    tab3G[2:, 2] = nps
    
    tab3G = tab3G.sum(axis=1)
    
    return lil_matrix(np.bincount(tab3G, minlength=128**3)).astype(np.uint32)