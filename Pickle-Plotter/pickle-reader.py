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

    # Filtro per prendere solo dati compresi tra i 2 valori
    if 1662555526.6410446 < time < 1662555528.4417448:
        pairs.append([time, integral[0]])
    # print(atrl)

    """"print(f"ATRL: {atrl} \n"
          f"Time: {time}\n"
          f"Max: {maximus}\n"
          f"Integral: {integral}\n"
          f"ToT: {time_of_threshold}")"""

# 1662555526.6410446, 5180.930289341738
# 1662555528.4417448, 17977.414235135326

print("Res vector size: ", len(pairs))

# 125 vector size
delta_t = pairs[124][0] - pairs[0][0]
print("Delta T ", delta_t)

# lista di partenza
input_list = []
for elem in pairs:
    input_list.append(elem[0])
print("Input list: ", input_list)

# Divido l'array pair in 18 parti per vedere il numero di campionamenti nell'unità di tempo
spacing = delta_t / 18
print("Spacing: ", spacing)

bins = []
for i in range(19):
    if i != 0:
        bins.append(spacing * i + input_list[0])
print("Bins: ", bins)

# creo un array con i risultati che voglio e il relativo conteggio
res = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
for elem in input_list:
    if elem <= bins[0]:
        res[0].append(elem)
    elif bins[0] < elem <= bins[1]:
        res[1].append(elem)
    elif bins[1] < elem <= bins[2]:
        res[2].append(elem)
    elif bins[2] < elem <= bins[3]:
        res[3].append(elem)
    elif bins[3] < elem <= bins[4]:
        res[4].append(elem)
    elif bins[4] < elem <= bins[5]:
        res[5].append(elem)
    elif bins[5] < elem <= bins[6]:
        res[6].append(elem)
    elif bins[6] < elem <= bins[7]:
        res[7].append(elem)
    elif bins[7] < elem <= bins[8]:
        res[8].append(elem)
    elif bins[8] < elem <= bins[9]:
        res[9].append(elem)
    elif bins[9] < elem <= bins[10]:
        res[10].append(elem)
    elif bins[10] < elem <= bins[11]:
        res[11].append(elem)
    elif bins[11] < elem <= bins[12]:
        res[12].append(elem)
    elif bins[12] < elem <= bins[13]:
        res[13].append(elem)
    elif bins[13] < elem <= bins[14]:
        res[14].append(elem)
    elif bins[14] < elem <= bins[15]:
        res[15].append(elem)
    elif bins[15] < elem <= bins[16]:
        res[16].append(elem)
    elif bins[16] < elem <= bins[17]:
        res[17].append(elem)

"""for elem in res:
    print(elem)"""

res_x = []
for elem in res:
    res_x.append(len(elem)+1)
print(res_x)

plt.hist(input_list, bins=18)
plt.show()
