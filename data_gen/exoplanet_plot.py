import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('exoplanet.csv')

print(data.head())

np_data = []

for i, row in data.iterrows():
    if row['LABEL'] != 1 : continue
    row_data = row.to_numpy()
    row_data = (row_data - np.mean(row_data))/np.std(row_data)
    for j in range(len(row_data)):
        if abs(row_data[j])>3:
            row_data[j] = 0
    np_data.append(row_data[::20])

for data_ptr in np_data[3:7]:
    plt.plot(list(range(len(data_ptr))), data_ptr)

plt.xlabel('time')
plt.ylabel('normalized light intensity')

plt.savefig('../images/otherplanet.png', dpi=300)
    
plt.show()
