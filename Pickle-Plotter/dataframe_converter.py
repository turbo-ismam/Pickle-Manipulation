import pandas as pd
import _pickle as pi
import bz2, json
import os

"""
data = {'Name': ['Tom', 'Joseph', 'Krish', 'John'], 'Age': [20, 21, 19, 18]}
df = pd.DataFrame(data)

print(df)

df[["Name", "Age"]].to_csv("out.csv", index=False)
"""


def generate_dataframe(file):
    current_offset = []
    sample_no = []
    title = []
    trigger_offset = []
    time_end = []
    time_start = []
    u_sec = []
    time_of_threshold = []
    for wf in file:
        atrl = json.loads(wf['ATTR'])
        current_offset.append(atrl['CurrentOffset'])
        sample_no.append(atrl['SampleNo'])
        title.append(atrl['TITLE'])
        trigger_offset.append(atrl['TriggerOffset'])
        time_end.append(atrl["tend"])
        time_start.append(atrl["tstart"])
        u_sec.append(atrl['usec'])
        time_of_threshold.append((wf['END'] - wf['START']) * 8)

    return {"Current Offset": current_offset,
            "Sample Number": sample_no,
            "Title": title,
            "Trigger Offset": trigger_offset,
            "Time End": time_end,
            "Time Start": time_start,
            "U Sec": u_sec,
            "Time Of Threshold": time_of_threshold}


# Pickle opening
FILE_NAME = os.path.join(os.path.abspath(__file__), "..", "Pickle_Files", "2022-09-07.pbz2")
data = pi.load(bz2.BZ2File(FILE_NAME, 'rb'))

res = generate_dataframe(data)

df = pd.DataFrame(res)
df.to_csv("DF_Conversion/result.csv", index=False)

