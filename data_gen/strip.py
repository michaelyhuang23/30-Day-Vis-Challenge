import matplotlib.pyplot as plt

times = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]
mags = [0.23, 0.04, -0.23, -0.2, -0.05, 0.17, 0.05, -0.18, -0.23, -0.05, 0.24]

mags2D = [mags for i in range(10)]

plt.pcolormesh(times,list(range(10)),mags2D)

ax = plt.gca()
ax.get_yaxis().set_visible(False)

plt.show()
