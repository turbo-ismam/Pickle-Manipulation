import numpy as np
import matplotlib.pyplot as plt
import _pickle as pi
import bz2, json
import os

FILE_NAME = os.path.join(os.path.abspath(__file__), "..", "Pickle_Files", "2022-09-07.pbz2")

data = pi.load(bz2.BZ2File(FILE_NAME, 'rb'))

pairs = []

for wf in data:
    atrl = json.loads(wf['ATTR'])
    time = atrl['tend']
    maximus = wf['MAX']
    integral = sum(wf['DATA'])
    time_of_threshold = (wf['END'] - wf['START']) * 8

    if 1662555526.6410446 < time < 1662555528.4417448:
        pairs.append([time, integral[0]])
    # print(atrl)

    """"print(f"ATRL: {atrl} \n"
          f"Time: {time}\n"
          f"Max: {maximus}\n"
          f"Integral: {integral}\n"
          f"ToT: {time_of_threshold}")"""

print(pairs)

# 1662555526.6410446, 5180.930289341738

# 1662555528.4417448, 17977.414235135326

# filtered_list = filter(lambda t: t > 1662555526.6410446 & t < 1662555528.4417448, pairs[0:])
# print(filtered_list)

np.random.seed(42)
x = np.random.normal(size=1000)
print(x)

plt.hist(x, density=True, bins=18)  # density=False would make counts
plt.ylabel('Probability')
plt.xlabel('Data')
plt.show()

x_length = 1662555528.4417448 - 1662555526.6410446
print(x_length)
x_length_slice = x_length / 18  # per avere dei bins di DeltaT =  0.1 microsecondi
print(x_length_slice)


