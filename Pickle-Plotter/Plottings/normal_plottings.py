import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("result1.csv")
# print(df)

plt.yscale('log', base=10)
plt.style.use('seaborn-whitegrid')
plt.hist(df["Max"], 200)
plt.title(" Max Spectrum ")
plt.xlabel("Max Amplitude mV")
plt.ylabel("Events")
plt.show()
plt.figure()

# Questa cosa ha problemi, l'integrale è un vettore wtf ??
"""plt.yscale('log', base=10)
plt.style.use('seaborn-whitegrid')
plt.title(" Integrated Signal Spectrum ")
plt.xlabel("Integrated Charge fC")
plt.ylabel("Events")
multiplied_list = []

tmp_vec = []
for i in range(500):
    tmp_vec.append(df["Integral"][i])
print(tmp_vec)
plt.hist(tmp_vec, 200)
plt.show()
plt.figure()"""

plt.yscale('log', base=10)
plt.style.use('seaborn-whitegrid')
plt.hist(df["Time Of Threshold"], 200)
plt.title(" Time over Threshold spectrum ")
plt.xlabel("Time over Threshold ns")
plt.ylabel("Events")
plt.show()
plt.figure()
