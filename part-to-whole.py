import matplotlib.pyplot as plt
import seaborn as sns

#define data
# data = [48019985, 35732180, 34699567]
# labels = ['Democrat', 'Republican', 'Independent']
# 
# #define Seaborn color palette to use
# colors = sns.color_palette('pastel')[0:3]
# 
# #create pie chart
# plt.pie(data, labels = labels, colors = colors, autopct='%.0f%%')
# plt.show()
# 
#define data
data = [4924144, 1914856]
labels = ['Vaccinated', 'Not Yet Vaccinated']

#define Seaborn color palette to use
colors = sns.color_palette('pastel')[0:2]

#create pie chart
plt.pie(data, labels = labels, colors = colors, autopct='%.0f%%')
plt.show()
