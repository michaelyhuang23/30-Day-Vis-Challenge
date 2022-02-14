import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


data = pd.read_csv('pirate-warm.csv')

print(data)


temps = data['global-average-temperature'].to_numpy()
pirates = data['number-of-pirates'].to_numpy()

temps = (temps-np.mean(temps))/np.std(temps)
pirates = -pirates
pirates = (pirates-np.mean(pirates))/np.std(pirates)

times = data['Year'].to_numpy()

plt.plot(times, temps, label='global temperature')
plt.plot(times, pirates, label='negation of the number of pirates')

ax = plt.gca()
ax.get_yaxis().set_visible(False)
plt.legend()

plt.show()



