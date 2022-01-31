import matplotlib.pyplot as plt
from collections import Counter

import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')
st_words = stopwords.words('english')
text = "We have pioneered a new method for the measurement of extragalactic distances. This method uses the time-lag between variations in the short wavelength and long wavelength light from an active galactic nucleus (AGN), based on a quantitative physical model of dust reverberation that relates\
the time-lag to the absolute luminosity of the AGN. We use the large homogeneous data set from\
intensive monitoring observations in optical and near-infrared wavelength bands with the dedicated\
2-m MAGNUM telescope to obtain the distances to 17 AGNs in the redshift range z = 0.0024 to\
z = 0.0353. These distance measurements are compared with distances measured using Cepheid\
variable stars, and are used to infer that H0 = 73 ± 3 (random) km s−1 Mpc−1 . The systematic error\
in H0 is examined, and the uncertainty in the size distribution of dust grains is the largest source of\
the systematic error, which is much reduced for a sample of AGNs for which their parameter values\
in the model of dust reverberation are individually measured. This AGN time-lag method can be\
used beyond 30 Mpc, the farthest distance reached by extragalactic Cepheids, and can be extended\
to high-redshift quasi-stellar objects.\
Subject headings: cosmological parameters — dust, extinction — galaxies: active — galaxies: Seyfert"

words = text.lower().split()
words = [word for word in words if word.isalpha() and word not in st_words]

cc = Counter(words)

wcc = cc.most_common()[:10]

xs = [word for word, c in wcc]
ys = [c for word, c in wcc]

plt.plot(xs, ys)
plt.title("frequency of words in the Abstract of the A New Method of Determining Distance to Galaxies paper")
plt.show()