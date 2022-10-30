import pandas as pd
import _pickle as pi
import bz2, json
import os


def generate_dataframe(file):
    maxes = []
    time = []
    integral = []
    time_of_threshold = []
    intns = []
    for wf in file:
        atrl = json.loads(wf['ATTR'])
        maxes.append(wf['MAX'])
        time.append(atrl['tend'])
        integral.append(sum(wf['DATA']))
        time_of_threshold.append((wf['END']-wf['START'])*8)
        intns.append(sum(wf['DATA']))
    return {"Max": maxes,
            "Time": time,
            "Integral": integral,
            "Time Of Threshold": time_of_threshold,
            "INTNS": intns}


# Pickle opening
FILE_NAME = os.path.join(os.path.abspath(__file__), "..", "Pickle_Files", "2022-09-07.pbz2")
data = pi.load(bz2.BZ2File(FILE_NAME, 'rb'))

res = generate_dataframe(data)

df = pd.DataFrame(res)
df.to_csv("Plottings/result1.csv", index=False)
print("Converted")