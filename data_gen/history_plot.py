import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter

data = pd.read_csv('top10s.csv', encoding="ISO-8859-1")

counters = [Counter() for i in range(10)]
for i, row in data.iterrows():
    yeari = row['year'] - 2010
    counters[yeari][row['artist']]+=1


singers = Counter()

for counter in counters:
    singers.update(counter) 

singers = singers.most_common()[:5]
for singer, _ in singers:
    ydata = [counters[i][singer] for i in range(10)]
    xdata = list(range(2010,2020))
    plt.plot(xdata, ydata, label=singer)
plt.legend()
plt.ylim(0,10)
plt.show()
