from matplotlib import pyplot as plt
from numpy import *
from scipy.stats import norm
import numpy as np

def count_possibilities(k):
    for i in range(1, 7):
        throws[k-1] = i
        if k > 1:
            count_possibilities(k-1)
        else:
            total.append(sum(throws))

total = []
k = 4
throws = [0 for _ in range(k)]
count_possibilities(k)
distribution = norm(mean(total), std(total))
values = np.unique(total)
probabilities = [distribution.pdf(value) for value in values]
cdf = np.cumsum(probabilities)
plt.bar(values, probabilities, label='gęstość')
plt.grid(True)
plt.legend()

bars = values
y_pos = np.arange(len(cdf))
plt.figure(figsize=(10, 5))
plt.bar(y_pos, cdf, label='dystrybuanta', color='#969696')
plt.xticks(y_pos, bars)
plt.legend()
plt.savefig("wykres")
plt.show()