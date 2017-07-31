# -*- coding: utf-8 -*-
"""
Created on Sun Mar 12 22:07:58 2017

@author: Shabaka
"""

import numpy as np


def bootstrap_replicate_1d(data, func):
    """Generate bootstrap replicate of 1D Data"""
    bs_sample = np.random.choice(data, len(data))

    return func(bs_sample)

# def boostrap_replicate_1d(data, func):  
#    return func(np.random.choice(data, size=len(data)))


def draw_bs_reps(data, func, size=1):
    """Draw bootstrap replicates."""

    # Initialize array of replicates: bs_replicates
    bs_replicates = np.empty(size)

    # Generate replicates
    for i in range(size):
        bs_replicates[i] = bootstrap_replicate_1d(data, func)

    return bs_replicates