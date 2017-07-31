# -*- coding: utf-8 -*-
"""
Created on Mon Mar  6 18:59:20 2017

@author: Shabaka
"""

# Code for correelate function is copied from pupil labs git @
# https://github.com/pupil-labs/pupil/wiki/Data-Format


def correlate_data(data, timestamps):
    '''
    data:  list of data :
        each datum is a dict with at least:
            timestamp: float

    timestamps: timestamps list to correlate  data to

    this takes a data list and a timestamps list and makes a new list
    with the length of the number of timestamps.
    Each slot contains a list that will have 0, 1 or more associated
    data points.

    Finally we add an index field to the datum with the associated index
    '''
    timestamps = list(timestamps)
    data_by_frame = [[] for i in timestamps]

    frame_idx = 0
    data_index = 0

    data.sort(key=lambda d: d['timestamp'])

    while True:
        try:
            datum = data[data_index]
            # we can take the midpoint between two frames in time:
            # More appropriate for SW timestamps
            ts = (timestamps[frame_idx]+timestamps[frame_idx+1]) / 2.
            # or the time of the next frame:
            # More appropriate for Sart Of Exposure Timestamps (HW timestamps).
            # ts = timestamps[frame_idx+1]
        except IndexError:
            # we might loose a data point at the end but we don't care
            break

        if datum['timestamp'] <= ts:
            datum['index'] = frame_idx
            data_by_frame[frame_idx].append(datum)
            data_index += 1
        else:
            frame_idx += 1

    return data_by_frame