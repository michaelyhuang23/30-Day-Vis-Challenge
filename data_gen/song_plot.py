import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sns.set(style = "darkgrid")

fig = plt.figure()
ax = fig.add_subplot(111, projection = '3d')


data = pd.read_csv('song_data.csv')

z = data['song_popularity']
y = data['acousticness']
x = data['energy']

ax.set_xlabel('energy of the song')
ax.set_ylabel('acousticness of the song')
ax.set_zlabel('popularity of the song')

ax.scatter(x,y,z)

plt.show()



