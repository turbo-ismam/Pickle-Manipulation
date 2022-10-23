import numpy as np
import matplotlib.pyplot as plt
import _pickle as pi
import bz2, json
import os


def read_d_arrays(filename):
    i = 0  # index for every wf
    j = 0  # index for rate
    secs = 60
    n_files = 0
    told = 0
    count = 0
    print(filename)
    Temp = np.zeros(11000)
    Max = np.zeros(11000)
    Int = np.zeros(11000)
    ToT = np.zeros(11000)
    Time = np.zeros(11000)
    RTime = np.zeros(11000)
    ff = np.zeros(11000)
    intns = np.zeros(11000)
    light_curves = [None] * 11000
    if os.path.getsize(filename) < 100:
        return
    n_files = n_files + 1
    # if (n_files<30) :
    # continue

    data = pi.load(bz2.BZ2File(filename, 'rb'))
    # print(filename)
    LightCurve = np.zeros(1000, dtype=int)
    for wf in data:
        atrl = json.loads(wf['ATTR'])
        tnew = atrl['tend']
        Time[i] = tnew
        Max[i] = wf['MAX']
        LightCurve[int(Max[i] - 1)] = LightCurve[int(Max[i] - 1)] + 1
        Int[i] = sum(wf['DATA'])
        ToT[i] = (wf['END'] - wf['START']) * 8
        if (wf['MAX'] < 1000):
            intns[i] = sum(wf['DATA'])
        i = i + 1
        ################## Riseva nuovo spazio
        if (i == len(Int)):
            tmp = np.zeros(2 * len(Int))
            tmp[:Int.shape[0]] = Int
            Int = tmp
            tmp = np.zeros(2 * len(intns))
            tmp[:intns.shape[0]] = intns
            intns = tmp
            tmp = np.zeros(2 * len(Max))
            tmp[:Max.shape[0]] = Max
            Max = tmp
            tmp = np.zeros(2 * len(ToT))
            tmp[:ToT.shape[0]] = ToT
            ToT = tmp
            tmp = np.zeros(2 * len(Time))
            tmp[:Time.shape[0]] = Time

        if ((tnew - told) >= secs):
            T = (tnew + told) / 2
            LightCurve = LightCurve / secs
            LightCurve[0] = T
            light_curves[j] = LightCurve
            LightCurve = np.zeros(1000, dtype=int)
            ff[j] = count / secs
            RTime[i] = (tnew + told) / 2
            count = 0
            told = tnew
            j = j + 1
            if (j == len(ff)):
                tmp = np.zeros(2 * len(ff))
                tmp[:ff.shape[0]] = ff
                ff = tmp
                tmp = np.zeros(2 * len(RTime))
                tmp[:RTime.shape[0]] = RTime
                RTime = tmp
                tmp = [None] * 2 * len(light_curves)
                tmp[:len(light_curves)] = light_curves
                light_curves = tmp
            # tmp=np.zeros(2*len(Temp))
            # tmp[:Temp.shape[0]]=Temp
            # Temp=tmp
        count = count + 1
    light_curves = list(filter(lambda item: item is not None, light_curves))
    print(len(Max[Max > 0]))
    return (Max, Int, intns, ToT, Time, ff, RTime, light_curves)

FILE_PATH = r"C:\Users\Ismam\Desktop\tesi\dati\Pickle\test.pbz2"
Result = read_d_arrays(FILE_PATH)

(Max, Int, Intns, ToT, Time, FF, RTime, LighCurves) = Result

(cMax, cInt, cIntns, cToT, cTime, cFF, cRTime, cLighCurves) = Result
Max = np.concatenate((Max, cMax))
Int = np.concatenate((Int, cInt))
Intns = np.concatenate((Intns, cIntns))
ToT = np.concatenate((ToT, cToT))
Time = np.concatenate((Time, cTime))
FF = np.concatenate((FF, cFF))
RTime = np.concatenate((RTime, cRTime))
LighCurves = LighCurves + cLighCurves

FF = [x for _, x in sorted(zip(RTime, FF))]

RTime = sorted(RTime)

FF = np.array(FF)
RTime = np.array(RTime)
RTime = RTime[FF > 0]
FF = FF[FF > 0]
FF = FF[RTime > 0]
RTime = RTime[RTime > 0]
Result = (Max, Int, Intns, ToT, Time, FF, RTime)
with bz2.BZ2File("data.pbz2", 'w') as fp:
    pi.dump((Max, Int, Intns, ToT, Time, FF, RTime, LighCurves), fp)

# leggo una sola colonna (dei max)
# time = trigger time
#
plt.yscale('log', base=10)
plt.style.use('seaborn-whitegrid')
plt.hist(Max[Max > 0], 200)
plt.title(" Max Spectrum ")
plt.xlabel("Max Amplitude mV")
plt.ylabel("Events")
# plt.savefig(sdir+'Max_spectrum.png', dpi=300)
plt.show()
plt.figure()
plt.yscale('log', base=10)
plt.style.use('seaborn-whitegrid')
plt.title(" Integrated Signal Spectrum ")
plt.xlabel("Integrated Charge fC")
plt.ylabel("Events")
plt.hist(Int[Int > 0] * 8 / 50, 200)
# plt.savefig(sdir+'Integral_spectrum.png', dpi=300)
plt.show()
plt.figure()
plt.yscale('log', base=10)
plt.style.use('seaborn-whitegrid')
plt.title(" Integrated Signal Spectrum for max<1V")
plt.xlabel("Integrated Charge fC")
plt.ylabel("Events")
plt.hist(Intns[Intns > 0] * 8 / 50, 200)
# plt.savefig(sdir+'Integral_spectrum_ns.png', dpi=300)
plt.show()
plt.figure()
plt.style.use('seaborn-whitegrid')
plt.plot(Int, Max, '.', color='black')
plt.title(" Signal Max vs Integral  ")
plt.ylabel("Signal Max mV")
plt.xlabel("Integrated Signag fC")
# plt.savefig(sdir+'Int_vs_Max.png', dpi=300)
plt.show()
plt.figure()
plt.yscale('log', base=10)
plt.style.use('seaborn-whitegrid')
plt.hist(ToT[ToT > 0], 200)
plt.title(" Time over Threshold spectrum ")
plt.xlabel("Time over Threshold ns")
plt.ylabel("Events")
# plt.savefig(sdir+'ToT.png', dpi=300)
plt.show()
plt.figure()
plt.style.use('seaborn-whitegrid')
plt.title(" Time over Threshold vs Integral  ")
plt.ylabel("Time over Threshold ns")
plt.xlabel("Integrated Signag fC")
plt.plot(Int * 8 / 50, ToT, '.', color='black')
# plt.savefig(sdir+'Int_vs_ToT.png', dpi=300)
plt.show()
plt.figure()
x = np.linspace(0., len(FF), len(FF))
plt.plot(RTime, FF)
plt.title(" Rate per Minute ")
plt.xlabel("Time Elapsed (h)")
plt.ylabel("Hz")
# plt.savefig(sdir+'Rate.png', dpi=300)
plt.show()
plt.figure()
