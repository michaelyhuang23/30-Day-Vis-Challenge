import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
import re
import numpy as np

data = pd.read_csv('Spells.csv', encoding="ISO-8859-1")

hist = {'charm' : Counter(), 'hex' : Counter(), 'jinx' : Counter(), 'curse' : Counter()}
cc = Counter()
for i, row in data.iterrows():
    if not isinstance(row['Light'], str) : continue
    if not isinstance(row['Type'], str) : continue
    colors = row['Light'].lower()
    colors = re.split('[^a-zA-Z]', colors)
    types = row['Type'].lower()
    types = re.split('[^a-zA-Z]', types)
    if 'dark' in types or 'curse' in types:
        t = 'curse'
    elif 'charm' in types:
        t = 'charm'
    elif 'hex' in types:
        t = 'hex'
    elif 'jinx' in types:
        t = 'jinx'
    else: continue

    for c in colors:
        if c == '': continue
        cc[c]+=1
        hist[t][c]+=1


spells = ['charm', 'hex', 'jinx', 'curse']
prev_heights = np.zeros((4))

lc = cc.most_common()[:7]
print(lc)

for c, _ in lc:
    heights = np.array([hist[i][c] for i in spells])
    if c == 'none':
        c = 'black'
    if c == 'white':
        c = 'silver'
    plt.bar(spells, heights, bottom = prev_heights, color = c)
    prev_heights += heights

plt.title("Different types of spells and the colors they use. Black stands for invisible spells.")
plt.show()
