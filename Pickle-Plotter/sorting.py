data = [1.3, 1.4, 1.45, 1.7, 3.4, 4.2, 5.5, 7.1, 8.7]  # len = 9

# voglio dividerlo in 3
unity = (data[len(data) - 1] - data[0]) / 3
print(unity)
rounded_unity = round(unity) + 1
print("Normal: ", unity, "\nRounded: ", rounded_unity)

bins = [data[0]]
for i in range(4):
    if i > 0:
        bins.append(bins[i - 1] + unity)
print(bins)

# 1.3 - 3.77 | 3.77 - 6.23 | 6.23 - 8.7
res = [[], [], []]

for elem in data:
    if bins[0] < elem <= bins[1]:
        res[0].append(elem)
    elif bins[1] < elem <= bins[2]:
        res[1].append(elem)
    elif bins[2] < elem <= bins[3]:
        res[2].append(elem)


print("Res Len: ", len(res), "\nBins Len: ", len(bins), "\n", res)
