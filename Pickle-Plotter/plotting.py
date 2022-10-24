import matplotlib.pyplot as plt

input_list = [1662555526.6449723, 1662555526.6499524, 1662555526.66144, 1662555526.672741, 1662555526.7062743,
              1662555526.719832, 1662555526.7724233, 1662555526.8005626, 1662555526.804589, 1662555526.818847,
              1662555526.8290315, 1662555526.8383932, 1662555526.8520596, 1662555526.8581963, 1662555526.8638203,
              1662555526.8684902, 1662555526.8883462, 1662555526.904715, 1662555526.926407, 1662555526.9356573,
              1662555526.9412751, 1662555526.9465091, 1662555526.9594948, 1662555526.9636858, 1662555526.968544,
              1662555526.9750273, 1662555526.9796865, 1662555526.9960485, 1662555527.0014246, 1662555527.0056221,
              1662555527.0098686, 1662555527.0143147, 1662555527.0279357, 1662555527.0321338, 1662555527.0598583,
              1662555527.0726779, 1662555527.0726779, 1662555527.091831, 1662555527.1013024, 1662555527.1101189,
              1662555527.1101189, 1662555527.136546, 1662555527.156833, 1662555527.1604257, 1662555527.1675458,
              1662555527.1713636, 1662555527.192542, 1662555527.2233236, 1662555527.235153, 1662555527.243075,
              1662555527.2707617, 1662555527.2782679, 1662555527.3220704, 1662555527.3258653, 1662555527.330495,
              1662555527.343723, 1662555527.3527043, 1662555527.36184, 1662555527.3756862, 1662555527.4159167,
              1662555527.4333007, 1662555527.4382339, 1662555527.4426975, 1662555527.4478302, 1662555527.4608493,
              1662555527.4667733, 1662555527.4708154, 1662555527.485704, 1662555527.4951236, 1662555527.4984095,
              1662555527.5065362, 1662555527.5314589, 1662555527.5628467, 1662555527.590685, 1662555527.6042018,
              1662555527.6227758, 1662555527.6327293, 1662555527.6363158, 1662555527.6520805, 1662555527.711506,
              1662555527.7165017, 1662555527.7486918, 1662555527.7671263, 1662555527.811525, 1662555527.8241422,
              1662555527.8498828, 1662555527.8547468, 1662555527.8638206, 1662555527.8829322, 1662555527.8903165,
              1662555527.8940098, 1662555527.9114642, 1662555527.9183543, 1662555527.9410393, 1662555527.9710605,
              1662555527.9906178, 1662555528.0066774, 1662555528.043537, 1662555528.0480418, 1662555528.0855129,
              1662555528.0910943, 1662555528.0973687, 1662555528.113314, 1662555528.1258433, 1662555528.141113,
              1662555528.152755, 1662555528.1564004, 1662555528.1735284, 1662555528.1840975, 1662555528.2166257,
              1662555528.2404692, 1662555528.2611184, 1662555528.268555, 1662555528.2771478, 1662555528.2911136,
              1662555528.301882, 1662555528.305123, 1662555528.3151538, 1662555528.3294203, 1662555528.3362272,
              1662555528.3419063, 1662555528.3878586, 1662555528.3956552, 1662555528.429505, 1662555528.434482]

plt.hist(input_list, bins=18)
plt.show()
