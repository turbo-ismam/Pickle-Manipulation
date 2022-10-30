import bz2, json, glob
import os, datetime
from joblib import Parallel, delayed

import _pickle as pi
import numpy as np
import matplotlib.pyplot as plt


def read_arrays(file_name):
    i = 0  # index for every wf
    j = 0  # index for rate
    Secs = 60
    n_files = 0
    told = 0
    count = 0
    print(file_name)
    np.zeros(11000)
    maximus = np.zeros(11000)
    integral = np.zeros(11000)
    time_of_threshold = np.zeros(11000)
    time = np.zeros(11000)
    r_time = np.zeros(11000)
    ff = np.zeros(11000)
    intns = np.zeros(11000)
    light_curves = [None] * 11000
    if os.path.getsize(file_name) < 100:
        return
    n_files = n_files + 1

    data = pi.load(bz2.BZ2File(file_name, 'rb'))
    # print(filename)
    LightCurve = np.zeros(1000, dtype=int)
    for wf in data:
        atrl = json.loads(wf['ATTR'])
        t_new = atrl['tend']
        time[i] = t_new
        maximus[i] = wf['MAX']
        LightCurve[int(maximus[i] - 1)] = LightCurve[int(maximus[i] - 1)] + 1
        integral[i] = sum(wf['DATA'])
        time_of_threshold[i] = (wf['END'] - wf['START']) * 8
        if wf['MAX'] < 1000:
            intns[i] = sum(wf['DATA'])
        i = i + 1
        # Riserva nuovo spazio
        if i == len(integral):
            tmp = np.zeros(2 * len(integral))
            tmp[:integral.shape[0]] = integral
            integral = tmp
            tmp = np.zeros(2 * len(intns))
            tmp[:intns.shape[0]] = intns
            intns = tmp
            tmp = np.zeros(2 * len(maximus))
            tmp[:maximus.shape[0]] = maximus
            maximus = tmp
            tmp = np.zeros(2 * len(time_of_threshold))
            tmp[:time_of_threshold.shape[0]] = time_of_threshold
            time_of_threshold = tmp
            tmp = np.zeros(2 * len(time))
            tmp[:time.shape[0]] = time

        if (t_new - told) >= Secs:
            T = (t_new + told) / 2
            LightCurve = LightCurve / Secs
            LightCurve[0] = T
            light_curves[j] = LightCurve
            LightCurve = np.zeros(1000, dtype=int)
            ff[j] = count / Secs
            r_time[i] = (t_new + told) / 2
            count = 0
            told = t_new
            j = j + 1
            if j == len(ff):
                tmp = np.zeros(2 * len(ff))
                tmp[:ff.shape[0]] = ff
                ff = tmp
                tmp = np.zeros(2 * len(r_time))
                tmp[:r_time.shape[0]] = r_time
                r_time = tmp
                tmp = [None] * 2 * len(light_curves)
                tmp[:len(light_curves)] = light_curves
                light_curves = tmp

        count = count + 1
    light_curves = list(filter(lambda item: item is not None, light_curves))
    print(len(maximus[maximus > 0]))
    return maximus, integral, intns, time_of_threshold, time, ff, r_time, light_curves


FILE_NAME = os.path.join(os.path.abspath(__file__), "..", "..", "Pickle_Files", "2022-09-07.pbz2")
res = read_arrays(FILE_NAME)

