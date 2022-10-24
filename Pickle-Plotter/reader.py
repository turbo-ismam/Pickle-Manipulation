import _pickle as pi
import bz2, json
import os


def print_data(file):
    count = 0
    for wf in file:
        atrl = json.loads(wf['ATTR'])
        time = atrl['tend']
        maximus = wf['MAX']
        integral = sum(wf['DATA'])
        time_of_threshold = (wf['END'] - wf['START']) * 8
        count = count + 1
        print(f"ATRL: {atrl} \n"
              f"Time: {time}\n"
              f"Max: {maximus}\n"
              f"Integral: {integral}\n"
              f"ToT: {time_of_threshold}\n")
    print("Original Data Count:", count)


def filter_data(file, min_time, max_time):
    res = [[]]
    for wf in file:
        atrl = json.loads(wf['ATTR'])
        time = atrl['tend']
        maximus = wf['MAX']
        integral = sum(wf['DATA'])
        time_of_threshold = (wf['END'] - wf['START']) * 8

        if min_time < time < max_time:
            res.append([time, time_of_threshold])
    return res


FILE_NAME = os.path.join(os.path.abspath(__file__), "..", "Pickle_Files", "2022-09-07.pbz2")
data = pi.load(bz2.BZ2File(FILE_NAME, 'rb'))
# 1662555526.6410446
# 1662555528.4417448
print_data(data)
print("\nCount After filter: ", len(filter_data(data, 1662555526, 1662555529)), "\n", filter_data(data, 1662555526,
                                                                                                  1662555529))
